import resvg_py, io, re, glob, os, numpy as np
from PIL import Image
D=r"F:\TRABAJOS CLAUDE\IPADECP\CERTIFICADOS - PROPUESTAS"
FD=r"F:\TRABAJOS CLAUDE\IPADECP\BRANDING\07 TIPOGRAFIAS\INSTALAR\ESTATICAS (una por peso)"
ims=[]
for f in sorted(glob.glob(os.path.join(D,"SVG EDITABLE (texto vivo)","*.svg"))):
    s=open(f,encoding='utf-8').read()
    s=s.replace('width="297mm" height="210mm"','width="2970" height="2100"')
    im=Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=s,width=1485,font_dirs=[FD],skip_system_fonts=True)))).convert('RGB')
    ref=Image.open(os.path.join(D,"PNG",os.path.basename(f).replace("-editable.svg",".png"))).convert('RGB').resize(im.size)
    print(os.path.basename(f), 'diff', round(float(np.abs(np.asarray(im,float)-np.asarray(ref,float)).mean()),2), 'textos', s.count('<text'))
    ims.append(im)
w=Image.new('RGB',(1485*2,1050),'white'); w.paste(ims[0],(0,0)); w.paste(ims[4],(1485,0)); w.resize((1600,566)).save('c_ed.png')
