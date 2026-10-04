"""09 BRANDBOOK: un solo HTML con menú arriba, una página por tema y todo descargable."""
import os, json, hashlib, re
from urllib.parse import quote
from PIL import Image
from brandlib import OUT, C

BB = os.path.join(OUT, "09 BRANDBOOK")
WEB = os.path.join(BB, "web")
os.makedirs(WEB, exist_ok=True)
Image.MAX_IMAGE_PIXELS = None


def rel(p):
    """Ruta relativa desde 09 BRANDBOOK, codificada para href."""
    r = os.path.relpath(p, BB).replace("\\", "/")
    return "/".join(quote(s) for s in r.split("/"))


def thumb(png, maxw=900):
    h = hashlib.md5(os.path.relpath(png, OUT).encode()).hexdigest()[:12]
    base = re.sub(r"[^a-z0-9-]+", "-", os.path.splitext(os.path.basename(png))[0].lower())[:60]
    name = f"{base}-{h}.webp"
    dst = os.path.join(WEB, name)
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(png):
        im = Image.open(png)
        im.thumbnail((maxw, maxw))
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGBA")
        im.save(dst, "WEBP", quality=84, method=5)
    return "web/" + name


def item(png, title=None, svg=None, dark=False, **tags):
    if svg is None:
        cand = png.replace(os.sep + "PNG" + os.sep, os.sep + "SVG" + os.sep)[:-4] + ".svg"
        if os.path.exists(cand):
            svg = cand
        elif os.path.exists(png[:-4] + ".svg"):
            svg = png[:-4] + ".svg"
    t = title or os.path.splitext(os.path.basename(png))[0].replace("-", " ")
    d = dict(t=t, img=thumb(png), png=rel(png), w=Image.open(png).size[0], h=Image.open(png).size[1])
    if svg:
        d["svg"] = rel(svg)
    if dark:
        d["dark"] = 1
    d.update(tags)
    return d


def pngs(folder):
    out = []
    for root, _, files in os.walk(folder):
        for f in sorted(files):
            if f.lower().endswith(".png"):
                out.append(os.path.join(root, f))
    return sorted(out)


def J(p, *a):
    return os.path.join(OUT, p, *a)


# ------------------------------------------------------------ colecciones
G = {}
VERS = ["color", "color-plano", "escala-grises", "bn-positivo", "bn-negativo", "una-tinta-navy", "una-tinta-negro", "una-tinta-blanco", "una-tinta-rojo"]
VNOM = {"color": "Color", "color-plano": "Color en tintas planas", "escala-grises": "Escala de grises", "bn-positivo": "Blanco y negro positivo",
        "bn-negativo": "Blanco y negro negativo", "una-tinta-navy": "Una tinta navy", "una-tinta-negro": "Una tinta negro",
        "una-tinta-blanco": "Una tinta blanco", "una-tinta-rojo": "Una tinta rojo"}
DARKV = {"bn-negativo", "una-tinta-blanco"}

G["versiones"] = []
for kind, folder in [("logotipo", "LOGO OFICIAL"), ("isotipo", "ISOTIPO")]:
    for v in VERS:
        p = J("01 LOGOS", folder, "PNG", f"{kind}-{v}.png")
        G["versiones"].append(item(p, VNOM[v], dark=v in DARKV, tipo=kind))

G["kit"] = []
for kind, folder in [("logotipo", "LOGO OFICIAL"), ("isotipo", "ISOTIPO")]:
    for sub, fmt in [("CON FONDO 1x1", "1:1"), ("16x9", "16:9")]:
        d = J("01 LOGOS", folder, sub, "PNG")
        if not os.path.isdir(d):
            continue
        for p in pngs(d):
            n = os.path.basename(p)[:-4]
            v = next((x for x in sorted(VERS, key=len, reverse=True) if f"{kind}-{x}-" in n), "")
            fondo = n.split("fondo-")[-1] if "fondo-" in n else "sin fondo"
            G["kit"].append(item(p, f"{VNOM.get(v, v)} · {fondo.replace('-', ' ')}", tipo=kind, formato=fmt,
                                 dark=("sin fondo" == fondo and v in DARKV)))

G["perfil"] = [item(p, os.path.basename(p)[:-4].replace("perfil-", "").replace("-", " ")) for p in pngs(J("08 REDES SOCIALES", "PERFIL", "PNG"))]
G["perfil_prev"] = [item(p) for p in pngs(J("08 REDES SOCIALES", "PERFIL", "VISTA PREVIA CIRCULO"))]
G["sellos"] = [item(p, os.path.basename(p)[:-4].replace("-", " ")) for p in pngs(J("02 SELLOS Y VERIFICACION", "PNG"))]
G["papeleria"] = [item(p, os.path.basename(p)[:-4].replace("-", " ")) for p in pngs(J("03 PAPELERIA"))]
G["mockups"] = [item(p, os.path.basename(p)[:-4].replace("mockup-", "").replace("-", " ")) for p in pngs(J("05 MOCKUPS", "PNG"))]
G["iconos"] = []
for p in pngs(J("04 ASSETS", "ICONOS", "PNG")):
    parts = os.path.relpath(p, J("04 ASSETS", "ICONOS", "PNG")).split(os.sep)
    G["iconos"].append(item(p, os.path.basename(p)[:-4].replace("icono-", "").replace("-", " "), estilo=parts[0], color=parts[1],
                            dark=parts[1] == "blanco"))
G["graficos"] = [item(p, os.path.basename(p)[:-4].replace("-", " "), dark="blanco" in p) for p in pngs(J("04 ASSETS", "ELEMENTOS GRAFICOS", "PNG"))]
G["patrones"] = [item(p, os.path.basename(p)[:-4].replace("patron-", "").replace("-", " ")) for p in pngs(J("04 ASSETS", "PATRONES", "PNG"))]
G["fondos"] = [item(p, os.path.basename(p)[:-4].replace("fondo-", "").replace("-", " "), formato=os.path.relpath(p, J("04 ASSETS", "FONDOS")).split(os.sep)[0])
               for p in pngs(J("04 ASSETS", "FONDOS"))]
G["qr"] = [item(p, os.path.basename(p)[:-4].replace("-", " "), dark=p.endswith("blanco.png")) for p in pngs(J("04 ASSETS", "QR", "PNG"))]
G["fotos"] = []
for f in sorted(os.listdir(J("04 ASSETS", "FOTOGRAFIA"))):
    p = J("04 ASSETS", "FOTOGRAFIA", f)
    G["fotos"].append(dict(t=f[:-4].replace("-", " "), img=thumb(p), png=rel(p), w=Image.open(p).size[0], h=Image.open(p).size[1]))
G["portadas"] = [item(p, os.path.basename(p)[:-4].replace("-", " ")) for p in pngs(J("08 REDES SOCIALES", "PORTADAS", "PNG"))] + \
                [item(p, os.path.basename(p)[:-4].replace("-", " ")) for p in pngs(J("08 REDES SOCIALES", "PORTADA WEB"))]
G["highlights"] = []
for p in pngs(J("08 REDES SOCIALES", "HIGHLIGHTS", "PNG")):
    var = os.path.relpath(p, J("08 REDES SOCIALES", "HIGHLIGHTS", "PNG")).split(os.sep)
    G["highlights"].append(item(p, os.path.basename(p)[:-4].replace("highlight-", "").replace("-", " "), variante=var[0] if len(var) > 1 else "vista"))
G["posts"] = [item(p, os.path.basename(p)[:-4].replace("-", " ")) for p in pngs(J("08 REDES SOCIALES", "POSTS 4x5", "PNG"))]
G["stories"] = [item(p, os.path.basename(p)[:-4].replace("-", " ")) for p in pngs(J("08 REDES SOCIALES", "STORIES", "PNG"))]
G["tipos"] = [item(p, os.path.basename(p)[:-4].replace("-", " ")) for p in pngs(J("07 TIPOGRAFIAS", "MUESTRAS", "PNG"))]
G["laminas"] = [item(J("06 PALETA DE COLORES", "paleta-ipadecp.png"), "Lámina de paleta"),
                item(J("06 PALETA DE COLORES", "HOJA-DE-MARCA-IPADECP.png"), "Hoja de marca")]

# imágenes sueltas para la maqueta
I = {
    "logo_color": thumb(J("01 LOGOS", "LOGO OFICIAL", "PNG", "logotipo-color.png"), 1200),
    "logo_blanco": thumb(J("01 LOGOS", "LOGO OFICIAL", "PNG", "logotipo-una-tinta-blanco.png"), 1200),
    "iso_color": thumb(J("01 LOGOS", "ISOTIPO", "PNG", "isotipo-color.png"), 600),
    "iso_blanco": thumb(J("01 LOGOS", "ISOTIPO", "PNG", "isotipo-una-tinta-blanco.png"), 600),
    "mock_cert": thumb(J("05 MOCKUPS", "PNG", "mockup-certificado-y-sobre.png"), 1400),
    "mock_pap": thumb(J("05 MOCKUPS", "PNG", "mockup-papeleria.png"), 1400),
    "sello": thumb(J("02 SELLOS Y VERIFICACION", "PNG", "sello-verificable-rojo.png"), 700),
    "foto_hero": thumb(J("04 ASSETS", "FOTOGRAFIA", "hero.jpg"), 1000),
    "foto_cert": thumb(J("04 ASSETS", "FOTOGRAFIA", "certificado.jpg"), 1000),
    "foto_est": thumb(J("04 ASSETS", "FOTOGRAFIA", "camino-estudiar.jpg"), 1000),
    "post_ver": thumb(J("08 REDES SOCIALES", "POSTS 4x5", "PNG", "post-verificacion-1080x1350.png"), 900),
    "iconos": thumb(J("04 ASSETS", "ICONOS", "MUESTRA-ICONOS.png"), 1400),
}
L = {  # enlaces de descarga
    "logo_color_svg": rel(J("01 LOGOS", "LOGO OFICIAL", "SVG", "logotipo-color.svg")),
    "logo_color_png": rel(J("01 LOGOS", "LOGO OFICIAL", "PNG", "logotipo-color.png")),
    "logo_blanco_svg": rel(J("01 LOGOS", "LOGO OFICIAL", "SVG", "logotipo-una-tinta-blanco.svg")),
    "logo_blanco_png": rel(J("01 LOGOS", "LOGO OFICIAL", "PNG", "logotipo-una-tinta-blanco.png")),
    "iso_color_svg": rel(J("01 LOGOS", "ISOTIPO", "SVG", "isotipo-color.svg")),
    "iso_color_png": rel(J("01 LOGOS", "ISOTIPO", "PNG", "isotipo-color.png")),
    "maestro": rel(J("10 EDITABLES Y DOCUMENTOS", "logotipo-maestro-original-10322x8933.webp")),
    "ase": rel(J("06 PALETA DE COLORES", "paleta-ipadecp.ase")), "gpl": rel(J("06 PALETA DE COLORES", "paleta-ipadecp.gpl")),
    "css": rel(J("06 PALETA DE COLORES", "paleta-ipadecp.css")), "json": rel(J("06 PALETA DE COLORES", "paleta-ipadecp.json")),
    "hanken": rel(J("07 TIPOGRAFIAS", "INSTALAR", "HankenGrotesk[wght].ttf")), "inter": rel(J("07 TIPOGRAFIAS", "INSTALAR", "Inter[opsz,wght].ttf")),
    "brand": rel(J("10 EDITABLES Y DOCUMENTOS", "DOCUMENTOS DE MARCA", "BRAND.md")),
    "vocab": rel(J("10 EDITABLES Y DOCUMENTOS", "DOCUMENTOS DE MARCA", "identidad", "vocabulario.md")),
    "readme": rel(J("README.md")),
}


def count(folder, ext):
    n = 0
    for root, _, files in os.walk(J(folder)):
        n += sum(1 for f in files if f.lower().endswith(ext))
    return n


CARPETAS = []
for f in sorted(os.listdir(OUT)):
    if os.path.isdir(J(f)) and f[:2].isdigit():
        CARPETAS.append(dict(n=f, href=rel(J(f)), svg=count(f, ".svg"), png=count(f, ".png"), otros=sum(len(fs) for _, _, fs in os.walk(J(f))) - count(f, ".svg") - count(f, ".png")))

HTML = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "brandbook_template.html"), encoding="utf-8").read()
HTML = HTML.replace("/*DATA*/", "const G=" + json.dumps(G, ensure_ascii=False) + ";\nconst CARPETAS=" + json.dumps(CARPETAS, ensure_ascii=False) + ";")
for k, v in I.items():
    HTML = HTML.replace("{{img:" + k + "}}", v)
for k, v in L.items():
    HTML = HTML.replace("{{dl:" + k + "}}", v)
HTML = HTML.replace("{{font:hanken}}", rel(J("07 TIPOGRAFIAS", "INSTALAR", "HankenGrotesk[wght].ttf")))
HTML = HTML.replace("{{font:inter}}", rel(J("07 TIPOGRAFIAS", "INSTALAR", "Inter[opsz,wght].ttf")))
left = re.findall(r"\{\{[^}]+\}\}", HTML)
assert not left, left
open(os.path.join(BB, "brandbook-ipadecp.html"), "w", encoding="utf-8").write(HTML)
total = sum(len(v) for v in G.values())
print("brandbook ok · piezas en galerías:", total)
