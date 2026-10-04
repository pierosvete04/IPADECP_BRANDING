import numpy as np, cv2, io, sys
from PIL import Image
import resvg_py
EDGE=float(sys.argv[1]) if len(sys.argv)>1 else 260
a=np.array(Image.open('m4k.png')).astype(np.float32)
H,W=a.shape[:2]
rgb=a[...,:3]; al=a[...,3]
sil=(al>128).astype(np.uint8)
r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
black=(rgb.max(-1)<95)
red=(~black)&(r>110)&(r>g+50)&(r>b+40)
blue=(~black)&(~red)
def lay(m):
    m=(m&(al>20)).astype(np.uint8)
    return cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
R=lay(red); K=lay(black)
Rd=cv2.dilate(R,np.ones((3,3),np.uint8))&sil; Kd=K&sil
def paths(m,eps=0.55,dx=0,dy=0):
    cs,_=cv2.findContours(m,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    out=[]
    for c in cs:
        if cv2.contourArea(c)<6: continue
        c=cv2.approxPolyDP(c,eps,True).reshape(-1,2)
        if len(c)<3: continue
        out.append('M'+' '.join(f'{x+dx},{y+dy}' for x,y in c)+'Z')
    return out
def hexc(c): c=np.clip(c,0,255).astype(int); return f'#{c[0]:02x}{c[1]:02x}{c[2]:02x}'
cc=rgb*(al[...,None]/255)+255*(1-al[...,None]/255)
E=np.zeros(al.shape,np.float32)
for ch in range(3):
    E+=np.hypot(cv2.Sobel(cc[...,ch],cv2.CV_32F,1,0,ksize=3),cv2.Sobel(cc[...,ch],cv2.CV_32F,0,1,ksize=3))
alm=(al>25).astype(np.uint8)
Bfull=cv2.dilate(lay(blue)|(blue&(al>25)).astype(np.uint8),np.ones((5,5),np.uint8))&alm
core=Bfull&(E<EDGE).astype(np.uint8)
n,lab=cv2.connectedComponents(core,connectivity=4)
lab=lab.astype(np.int32)
for _ in range(6):
    grown=cv2.dilate(lab.astype(np.float32),np.ones((3,3),np.uint8)).astype(np.int32)
    fill=(lab==0)&(Bfull>0)&(grown>0)
    lab[fill]=grown[fill]
defs=[];body=[]
for i in range(1,n):
    m=(lab==i)
    ys,xs=np.nonzero(m)
    if len(xs)<10: continue
    y0,x0=ys.min(),xs.min(); y1,x1=ys.max()+1,xs.max()+1
    sub=m[y0:y1,x0:x1].astype(np.uint8)
    ps=paths(sub,dx=x0,dy=y0)
    if not ps: continue
    sel=(al[ys,xs]>60)
    if sel.sum()<4: sel[:]=True
    P=np.stack([xs[sel],ys[sel]],1).astype(np.float32); cols=rgb[ys[sel],xs[sel]]; alp=al[ys[sel],xs[sel]]
    alp_all=al[ys,xs]; Pall=np.stack([xs,ys],1).astype(np.float32)
    m0=P.mean(0); Pc=P-m0
    J,_,_,_=np.linalg.lstsq(np.c_[Pc,np.ones(len(Pc))],np.c_[cols,alp],rcond=None)
    u,s,vt=np.linalg.svd(J[:2].T)
    d=vt[0]; t=(Pall-m0)@d; tc=Pc@d
    lo,hi=np.percentile(t,0.5),np.percentile(t,99.5)
    dstr=' '.join(ps)
    if hi-lo<3 or s[0]*(hi-lo)<10:
        o=np.median(alp)/255
        body.append(f'<path fill="{hexc(np.median(cols,0))}"'+('' if o>.97 else f' fill-opacity="{o:.2f}"')+f' d="{dstr}"/>'); continue
    nb=6; ed=np.linspace(lo,hi,nb+1); st=[]
    for j in range(nb):
        sj=(tc>=ed[j])&(tc<=ed[j+1]); sa=(t>=ed[j])&(t<=ed[j+1])
        if sj.sum()>0: col=np.median(cols[sj],0)
        else: continue
        o=np.clip(np.median(alp_all[sa])/255 if sa.sum() else 1,0,1)
        st.append(f'<stop offset="{(j+.5)/nb:.3f}" stop-color="{hexc(col)}"'+('' if o>.97 else f' stop-opacity="{o:.2f}"')+'/>')
    p1=m0+d*lo; p2=m0+d*hi
    defs.append(f'<linearGradient id="g{i}" gradientUnits="userSpaceOnUse" x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}">'+''.join(st)+'</linearGradient>')
    body.append(f'<path fill="url(#g{i})" d="{dstr}"/>')
svg='\n'.join([f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">','<defs>'+''.join(defs)+'</defs>',
 '<g id="azules" fill-rule="evenodd">'+''.join(body)+'</g>',
 '<g id="rojo" fill="#c6111a" fill-rule="evenodd"><path d="'+' '.join(paths(Rd))+'"/></g>',
 '<g id="negro" fill="#000000" fill-rule="evenodd"><path d="'+' '.join(paths(Kd))+'"/></g>','</svg>'])
open('color-vec.svg','w').write(svg)
im=np.array(Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=svg)))).convert('RGBA')).astype(np.float32)
comp=lambda x:x[...,:3]*(x[...,3:]/255)+255*(1-x[...,3:]/255)
v=comp(im); print('comps',n,'diff',np.abs(v-comp(a)).mean(),'MB',len(svg)/1e6)
v=Image.fromarray(v.astype(np.uint8)); v.resize((1032,893)).save('v_small.png')
o=Image.fromarray(comp(a).astype(np.uint8)); box=(900,800,2300,2000)
w=Image.new('RGB',(2800,1200),'white'); w.paste(o.crop(box),(0,0)); w.paste(v.crop(box),(1400,0)); w.resize((1400,600)).save('cmp1.png')
