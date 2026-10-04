"""05 MOCKUPS (composiciones planas, vectoriales) + copia de fuentes y documentos."""
import os, base64, shutil, re
from brandlib import *
from build_assets import globo

M = os.path.join(OUT, "05 MOCKUPS")
SRC = os.path.join(HERE, "..", "branding")


def svg_img(path, x, y, w, h, rot=0, sombra=True):
    """Incrusta un SVG ya generado como imagen vectorial."""
    data = open(path, "rb").read()
    data = re.sub(rb'width="([\d.]+)mm" height="([\d.]+)mm"', lambda m: f'width="{float(m.group(1))*10:g}" height="{float(m.group(2))*10:g}"'.encode(), data, count=1)
    href = "data:image/svg+xml;base64," + base64.b64encode(data).decode()
    t = f' transform="rotate({rot} {x + w/2} {y + h/2})"' if rot else ""
    sh = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#0a1c38" opacity=".22" filter="url(#sombra)"/>' if sombra else "")
    return f'<g{t}>{sh}<image x="{x}" y="{y}" width="{w}" height="{h}" href="{href}" preserveAspectRatio="none"/></g>'


SOMBRA = '<filter id="sombra" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="28"/><feOffset dx="0" dy="26"/></filter>'
P = os.path.join(OUT, "03 PAPELERIA")


def guardar(nm, svg):
    pair(os.path.join(M, "SVG"), os.path.join(M, "PNG"), nm, svg, 3000)


def mockup_certificado():
    W, H = 3000, 2000
    b = [f'<rect width="{W}" height="{H}" fill="{C["navy100"]}"/>', globo(2600, 300, 900, C["cel700"], 4, .12)]
    b.append(svg_img(os.path.join(P, "SOBRE", "SVG", "sobre-dl-certificado-fisico.svg"), 1700, 1180, 1100, 550, -6))
    b.append(svg_img(os.path.join(P, "CERTIFICADO", "SVG", "certificado-a4-horizontal-plantilla.svg"), 260, 250, 1782, 1260, 3))
    b.append(svg_img(os.path.join(OUT, "02 SELLOS Y VERIFICACION", "SVG", "sello-verificable-rojo.svg"), 2150, 300, 520, 520, 8, False))
    guardar("mockup-certificado-y-sobre", svg_doc(W, H, "".join(b), SOMBRA))


def mockup_papeleria():
    W, H = 3000, 2000
    d, rect = fondo(W, H, "marca")
    b = [rect, globo(400, 1700, 900, C["celeste"], 4, .2)]
    b.append(svg_img(os.path.join(P, "HOJA MEMBRETADA", "SVG", "hoja-membretada-a4.svg"), 260, 180, 1150, 1626, -4))
    b.append(svg_img(os.path.join(P, "SOBRE", "SVG", "sobre-dl-certificado-fisico.svg"), 1480, 1180, 1300, 650, 5))
    b.append(svg_img(os.path.join(P, "TARJETA PERSONAL", "SVG", "tarjeta-personal-frente.svg"), 1990, 130, 850, 550, -7))
    b.append(svg_img(os.path.join(P, "TARJETA PERSONAL", "SVG", "tarjeta-personal-dorso.svg"), 1500, 560, 850, 550, 5))
    guardar("mockup-papeleria", svg_doc(W, H, "".join(b), d + SOMBRA))


def mockup_redes():
    W, H = 3000, 2000
    b = [f'<rect width="{W}" height="{H}" fill="{C["hueso"]}"/>']
    R = os.path.join(OUT, "08 REDES SOCIALES")
    for i, nm in enumerate(["post-marca-1080x1350", "post-verificacion-1080x1350", "post-curso-1080x1350"]):
        b.append(svg_img(os.path.join(R, "POSTS 4x5", "SVG", nm + ".svg"), 240 + i * 860, 300, 800, 1000))
    b.append(text_path("Publicaciones 4:5 · plantillas", 240, 1500, 64, "hanken", 800, C["navy500"]))
    b.append(text_path("Marca, verificación y curso. Los textos entre corchetes se cambian antes de publicar.", 240, 1580, 38, "inter", 400, C["gris"]))
    guardar("mockup-publicaciones", svg_doc(W, H, "".join(b), SOMBRA))


def mockup_sellos():
    W, H = 3000, 2000
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    S = os.path.join(OUT, "02 SELLOS Y VERIFICACION", "SVG")
    for i, nm in enumerate(["sello-verificable-rojo", "sello-verificable-rojo-sobre-blanco", "sello-logro-curso-completado-oro"]):
        b.append(svg_img(os.path.join(S, nm + ".svg"), 220 + i * 900, 260, 760, 760, 0, False))
    b.append(svg_img(os.path.join(S, "insignia-verifica-este-certificado.svg"), 600, 1250, 1800, 472, 0, False))
    guardar("mockup-sellos-y-verificacion", svg_doc(W, H, "".join(b), SOMBRA))


def copiar_fuentes():
    E = os.path.join(OUT, "10 EDITABLES Y DOCUMENTOS")
    os.makedirs(E, exist_ok=True)
    shutil.copy(os.path.join(SRC, "logotipo", "logotipo-maestro-original.webp"), os.path.join(E, "logotipo-maestro-original-10322x8933.webp"))
    for sub in ("identidad", "sistema", "ui"):
        shutil.copytree(os.path.join(SRC, sub), os.path.join(E, "DOCUMENTOS DE MARCA", sub), dirs_exist_ok=True)
    for f in ("BRAND.md", "README.md", "moodboard.html"):
        shutil.copy(os.path.join(SRC, f), os.path.join(E, "DOCUMENTOS DE MARCA", f))
    shutil.copytree(os.path.join(SRC, "laminas"), os.path.join(E, "DOCUMENTOS DE MARCA", "laminas-anteriores"), dirs_exist_ok=True)
    shutil.copytree(os.path.join(SRC, "logotipo"), os.path.join(E, "KIT DE LOGO ANTERIOR (raster)"), dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("logotipo-maestro-original.webp"))
    fot = os.path.join(OUT, "04 ASSETS", "FOTOGRAFIA")
    shutil.copytree(os.path.join(SRC, "portada", "fotos"), fot, dirs_exist_ok=True)
    shutil.copytree(os.path.join(SRC, "portada"), os.path.join(E, "PORTADA WEB (scripts)"), dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("fotos", "*.png"))
    # el código que genera todo
    G = os.path.join(E, "GENERADOR (python)")
    os.makedirs(G, exist_ok=True)
    for f in os.listdir(HERE):
        if f.endswith(".py"):
            shutil.copy(os.path.join(HERE, f), os.path.join(G, f))
    shutil.copy(os.path.join(HERE, "logo.pkl"), os.path.join(G, "logo.pkl"))


if __name__ == "__main__":
    mockup_certificado(); mockup_papeleria(); mockup_redes(); mockup_sellos(); print("mockups")
    copiar_fuentes(); print("copias")
