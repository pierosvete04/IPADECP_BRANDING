import numpy as np, cv2
from PIL import Image
a=np.array(Image.open('m4k.png')).astype(np.float32)
H,W=a.shape[:2]
rgb=a[...,:3]; al=a[...,3]
sil=(al>128).astype(np.uint8)
r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]
mx=rgb.max(-1)
black=(mx<95)
red=(~black)&(r>110)&(r>g+50)&(r>b+40)
blue=(~black)&(~red)
k=np.ones((5,5),np.uint8)
def lay(m):
    m=(m&(al>20)).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
    return m
B=lay(blue); R=lay(red); K=lay(black)
# stacking: blue bottom (dilated), red, black on top; clip to silhouette
Bd=cv2.dilate(B,k)&sil; Rd=cv2.dilate(R,np.ones((3,3),np.uint8))&sil; Kd=K&sil
def paths(m,eps=0.55):
    cs,h=cv2.findContours(m,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    out=[]
    for c in cs:
        if cv2.contourArea(c)<6: continue
        c=cv2.approxPolyDP(c,eps,True).reshape(-1,2)
        if len(c)<3: continue
        out.append('M'+' '.join(f'{x},{y}' for x,y in c)+'Z')
    return out
def comps_grad(m):
    n,lab,st,cen=cv2.connectedComponentsWithStats(m,8)
    defs=[];body=[]
    for i in range(1,n):
        if st[i,4]<8: continue
        x0,y0,w,h=st[i,:4]
        sub=(lab[y0:y0+h,x0:x0+w]==i).astype(np.uint8)
        ps=paths(sub)
        if not ps: continue
        ys,xs=np.nonzero(sub&(al[y0:y0+h,x0:x0+w]>60).astype(np.uint8))
        if len(xs)<4: ys,xs=np.nonzero(sub)
        cols=rgb[y0+ys,x0+xs]; alp=al[y0+ys,x0+xs]
        P=np.stack([xs,ys],1).astype(np.float32)
        Pc=P-P.mean(0)
        A=np.c_[Pc,np.ones(len(Pc))]
        J,_,_,_=np.linalg.lstsq(A,cols,rcond=None)
        G=J[:2].T  # 3x2
        u,s,vt=np.linalg.svd(G)
        d=vt[0]
        t=Pc@d
        lo,hi=np.percentile(t,1),np.percentile(t,99)
        d_str=' '.join(ps)
        tr=f'translate({x0},{y0})'
        if hi-lo<3 or s[0]*(hi-lo)<12:
            c=np.median(cols,0).astype(int)
            body.append(f'<path transform="{tr}" fill="#{c[0]:02x}{c[1]:02x}{c[2]:02x}" d="{d_str}"/>')
            continue
        nb=5; edges=np.linspace(lo,hi,nb+1); stops=[]
        for j in range(nb):
            sel=(t>=edges[j])&(t<=edges[j+1])
            if sel.sum()==0: continue
            c=np.median(cols[sel],0).astype(int); o=np.clip(np.median(alp[sel])/255,0,1)
            off=(j+0.5)/nb
            stops.append(f'<stop offset="{off:.2f}" stop-color="#{c[0]:02x}{c[1]:02x}{c[2]:02x}"'+('' if o>0.97 else f' stop-opacity="{o:.2f}"')+'/>')
        m0=P.mean(0); p1=m0+d*lo; p2=m0+d*hi
        gid=f'g{i}'
        defs.append(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}">'+''.join(stops)+'</linearGradient>')
        body.append(f'<path transform="{tr}" fill="url(#{gid})" d="{d_str}"/>')
    return defs,body
bd,bb=comps_grad(Bd)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">','<defs>'+''.join(bd)+'</defs>',
 '<g id="azules" fill-rule="evenodd">'+''.join(bb)+'</g>',
 '<g id="rojo" fill="#c6111a" fill-rule="evenodd"><path d="'+' '.join(paths(Rd))+'"/></g>',
 '<g id="negro" fill="#000000" fill-rule="evenodd"><path d="'+' '.join(paths(Kd))+'"/></g>','</svg>']
open('color-vec.svg','w').write('\n'.join(svg))
import resvg_py,io
png=resvg_py.svg_to_bytes(svg_string='\n'.join(svg))
im=np.array(Image.open(io.BytesIO(bytes(png))).convert('RGBA')).astype(np.float32)
def comp(x):
    return x[...,:3]*(x[...,3:]/255)+255*(1-x[...,3:]/255)
d=np.abs(comp(im)-comp(a)).mean()
print('mean abs diff',d, 'size',len('\n'.join(svg))/1e6,'MB')
Image.fromarray(comp(im).astype(np.uint8)).save('vec-render.png')
