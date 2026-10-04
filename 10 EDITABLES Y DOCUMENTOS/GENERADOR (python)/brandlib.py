"""Utilidades compartidas para generar el branding de IPADECP."""

import os, io, pickle, math, functools

import numpy as np

import resvg_py

from PIL import Image

from fontTools.ttLib import TTFont

from fontTools.varLib.instancer import instantiateVariableFont

from fontTools.pens.svgPathPen import SVGPathPen

from fontTools.pens.transformPen import TransformPen

import uharfbuzz as hb



HERE = os.path.dirname(os.path.abspath(__file__))

OUT = r"F:\TRABAJOS CLAUDE\IPADECP\BRANDING"

FONTSRC = os.path.join(OUT, "07 TIPOGRAFIAS", "INSTALAR")

FONTDIR = os.path.join(HERE, "fonts")

os.makedirs(FONTDIR, exist_ok=True)



# ---------------------------------------------------------------- color

C = dict(

    navy900="#06142b", navy800="#0a1c38", navy="#10284d", navy600="#1c3d6b", navy500="#001331",

    navy100="#e8eef6", hueso="#f4f7fa",

    cel800="#0b6683", cel700="#2f7593", celeste="#6cb3d3", cel100="#dcf0f8", cel050="#f0f9fd",

    rojo700="#9d0d14", rojo="#c6111a", rojo050="#fdf0f1",

    oro700="#ad8420", oro="#d4af37", oro050="#fdf8e8",

    tinta="#1f2d3d", gris="#5a6878", tenue="#8492a3", borde="#e1e8ed", bordef="#c9d5df", campo="#768495",

    blanco="#ffffff", negro="#000000",

    azul_logo="#0130db", cian_logo="#00e4ff",

)



# degradados de marca (siempre 135 grados)

GRAD = dict(

    marca=[(0, C["navy900"]), (0.45, C["navy"]), (1, C["cel700"])],

    primario=[(0, C["navy"]), (1, "#24608f")],

    secundario=[(0, C["cel800"]), (1, "#307a99")],

    sello=[(0, C["rojo"]), (1, "#8f0c12")],

    libro=[(0, C["cian_logo"]), (1, C["azul_logo"])],

)





def grad135(gid, w, h, stops):

    """linearGradient equivalente a CSS linear-gradient(135deg) sobre un rect w x h."""

    a = math.radians(135)

    dx, dy = math.sin(a), -math.cos(a)

    L = abs(w * dx) + abs(h * dy)

    cx, cy = w / 2, h / 2

    x1, y1 = cx - dx * L / 2, cy - dy * L / 2

    x2, y2 = cx + dx * L / 2, cy + dy * L / 2

    st = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)

    return (f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{y1:.1f}" '

            f'x2="{x2:.1f}" y2="{y2:.1f}">{st}</linearGradient>')





def fondo(w, h, key, gid="bg"):

    """Devuelve (defs, rect) para un fondo de color plano o degradado de marca."""

    if key in GRAD:

        return grad135(gid, w, h, GRAD[key]), f'<rect width="{w}" height="{h}" fill="url(#{gid})"/>'

    return "", f'<rect width="{w}" height="{h}" fill="{C.get(key, key)}"/>'





# ---------------------------------------------------------------- fuentes

FAM = {"hanken": "HankenGrotesk[wght].ttf", "inter": "Inter[opsz,wght].ttf"}





@functools.lru_cache(None)

def font(fam, wt):

    path = os.path.join(FONTDIR, f"{fam}-{wt}.ttf")

    if not os.path.exists(path):

        f = TTFont(os.path.join(FONTSRC, FAM[fam]))

        axes = {"wght": wt}

        if fam == "inter":

            axes["opsz"] = 14

        inst = instantiateVariableFont(f, axes)

        inst.save(path)

    data = open(path, "rb").read()

    tt = TTFont(path)

    face = hb.Face(data)

    hbf = hb.Font(face)

    return tt, hbf, tt["head"].unitsPerEm





def shape(text, fam, wt, feats=None):

    tt, hbf, upm = font(fam, wt)

    buf = hb.Buffer()

    buf.add_str(text)

    buf.guess_segment_properties()

    f = {"kern": True, "liga": True}

    f.update(feats or {})

    hb.shape(hbf, buf, f)

    return tt, upm, buf.glyph_infos, buf.glyph_positions





def text_width(text, fam="hanken", wt=700, size=40, ls=0.0, feats=None):

    tt, upm, infos, pos = shape(text, fam, wt, feats)

    s = size / upm

    return sum(p.x_advance for p in pos) * s + ls * size * max(len(infos) - 1, 0)





def text_path(text, x, y, size, fam="hanken", wt=700, fill="#000", anchor="start", ls=0.0, extra="", feats=None):

    """Texto convertido a curvas. ls = interletrado en em."""

    if not text:

        return ""

    tt, upm, infos, pos = shape(text, fam, wt, feats)

    s = size / upm

    gs = tt.getGlyphSet()

    order = tt.getGlyphOrder()

    w = text_width(text, fam, wt, size, ls, feats)

    if anchor == "middle":

        x -= w / 2

    elif anchor == "end":

        x -= w

    pen = SVGPathPen(gs, lambda v: f"{v:.1f}".rstrip("0").rstrip("."))

    cx = x

    for inf, p in zip(infos, pos):

        name = order[inf.codepoint]

        tp = TransformPen(pen, (s, 0, 0, -s, cx + p.x_offset * s, y - p.y_offset * s))

        gs[name].draw(tp)

        cx += p.x_advance * s + ls * size

    d = pen.getCommands()

    return f'<path fill="{fill}" d="{d}"{extra}/>'





def wrap(text, width, size, fam="inter", wt=400):

    words, lines, cur = text.split(), [], ""

    for wd in words:

        t = (cur + " " + wd).strip()

        if text_width(t, fam, wt, size) <= width or not cur:

            cur = t

        else:

            lines.append(cur)

            cur = wd

    if cur:

        lines.append(cur)

    return lines





def para(text, x, y, width, size, lh=1.5, fam="inter", wt=400, fill="#1f2d3d", anchor="start"):

    out = []

    for i, ln in enumerate(wrap(text, width, size, fam, wt)):

        out.append(text_path(ln, x, y + i * size * lh, size, fam, wt, fill, anchor))

    return "".join(out), len(wrap(text, width, size, fam, wt))





# ---------------------------------------------------------------- logo

LOGO = pickle.load(open(os.path.join(HERE, "logo.pkl"), "rb"))

LW, LH = LOGO["W"], LOGO["H"]

ISO_CUT = 2900  # todo lo que está debajo es la palabra IPADECP y el remate del arco





def _hex(c):

    c = np.clip(np.array(c), 0, 255).astype(int)

    return f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}"





def _gray(c):

    c = np.array(c, float)

    v = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

    return _hex([v, v, v])





def logo_inner(version, pfx="L"):

    """Contenido del logo (coordenadas LW x LH) para cada versión."""

    comps = LOGO["comps"]

    if version.startswith("una-tinta-"):

        col = {"navy": C["navy"], "negro": C["negro"], "blanco": C["blanco"], "rojo": C["rojo"],

               "celeste": C["cel700"]}[version.split("-")[-1]]

        return "", f'<path id="logo-una-tinta" fill="{col}" fill-rule="evenodd" d="{LOGO["sil"]}"/>'

    defs, body = [], []

    for i, c in enumerate(comps):

        if version == "color":

            if "flat" in c:

                op = "" if c["op"] > .97 else f' fill-opacity="{c["op"]:.2f}"'

                body.append(f'<path fill="{_hex(c["flat"])}"{op} d="{c["d"]}"/>')

            else:

                st = "".join(f'<stop offset="{o:.3f}" stop-color="{_hex(col)}"' + ("" if a > .97 else f' stop-opacity="{a:.2f}"') + "/>"

                             for o, col, a in c["stops"])

                (x1, y1), (x2, y2) = c["p1"], c["p2"]

                defs.append(f'<linearGradient id="{pfx}g{i}" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}">{st}</linearGradient>')

                body.append(f'<path fill="url(#{pfx}g{i})" d="{c["d"]}"/>')

        elif version == "escala-grises":

            if "flat" in c:

                body.append(f'<path fill="{_gray(c["flat"])}" d="{c["d"]}"/>')

            else:

                st = "".join(f'<stop offset="{o:.3f}" stop-color="{_gray(col)}"' + ("" if a > .97 else f' stop-opacity="{a:.2f}"') + "/>"

                             for o, col, a in c["stops"])

                (x1, y1), (x2, y2) = c["p1"], c["p2"]

                defs.append(f'<linearGradient id="{pfx}g{i}" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}">{st}</linearGradient>')

                body.append(f'<path fill="url(#{pfx}g{i})" d="{c["d"]}"/>')

        else:

            body.append(c["d"])

    if version == "color-plano":

        cian = " ".join(c["d"] for c in comps if c["cls"] == "cian")

        azul = " ".join(c["d"] for c in comps if c["cls"] == "azul")

        blues = f'<g id="libro" fill="{C["cian_logo"]}"><path d="{cian}"/></g><g id="globo" fill="{C["azul_logo"]}"><path d="{azul}"/></g>'

        red, black = C["rojo"], C["negro"]

    elif version in ("bn-positivo", "bn-negativo"):

        g = "#7d7d7d" if version == "bn-positivo" else "#b5b5b5"

        blues = f'<g id="libro-y-globo" fill="{g}"><path d="{" ".join(body)}"/></g>'

        red = black = C["negro"] if version == "bn-positivo" else C["blanco"]

    else:

        blues = f'<g id="libro-y-globo">{"".join(body)}</g>'

        red, black = (C["rojo"], C["negro"]) if version == "color" else (_gray([198, 17, 26]), C["negro"])

    inner = (f'<g fill-rule="evenodd">{blues}'

             f'<g id="arco-y-filetes" fill="{red}"><path d="{LOGO["red"]}"/></g>'

             f'<g id="palabra-birrete-y-texto" fill="{black}"><path d="{LOGO["black"]}"/></g></g>')

    return "".join(defs), inner





def logo_box(kind):

    """viewBox (x, y, w, h) del logotipo completo o del isotipo."""

    if kind == "isotipo":

        return (0, 0, LW, ISO_CUT)

    return (0, 0, LW, LH)





def logo_svg_el(version, kind, x, y, w, pfx="L"):

    """Logo como <svg> anidado, colocado en (x,y) con ancho w. Devuelve (defs, el, alto)."""

    bx, by, bw, bh = logo_box(kind)

    h = w * bh / bw

    defs, inner = logo_inner(version, pfx)

    clip = ""

    if kind == "isotipo":

        clip = f'<clipPath id="{pfx}iso"><rect x="0" y="0" width="{LW}" height="{ISO_CUT}"/></clipPath>'

        inner = f'<g clip-path="url(#{pfx}iso)">{inner}</g>'

    el = (f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="{bx} {by} {bw} {bh}">'

          f'<defs>{defs}{clip}</defs>{inner}</svg>')

    return "", el, h





def svg_doc(w, h, body, defs="", title="IPADECP"):

    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'

            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'

            f'<title>{title}</title><defs>{defs}</defs>{body}</svg>\n')





# ---------------------------------------------------------------- salida

def save(path, svg=None, png_w=None, png=True):

    """Guarda el SVG y, si png, su PNG al ancho pedido."""

    os.makedirs(os.path.dirname(path), exist_ok=True)

    if svg is not None and path.endswith(".svg"):

        open(path, "w", encoding="utf-8").write(svg)

    return path





def render(svg, png_path, width=None, height=None):

    os.makedirs(os.path.dirname(os.path.abspath(png_path)), exist_ok=True)

    kw = {}

    if width:

        kw["width"] = int(width)

    if height:

        kw["height"] = int(height)

    import re
    svg = re.sub(r'width="([\d.]+)mm" height="([\d.]+)mm"',
                 lambda m: f'width="{float(m.group(1))*10:g}" height="{float(m.group(2))*10:g}"', svg, count=1)
    data = bytes(resvg_py.svg_to_bytes(svg_string=svg, **kw))

    im = Image.open(io.BytesIO(data))

    if png_path.lower().endswith(".jpg"):

        im.convert("RGB").save(png_path, quality=92)

    else:

        im.save(png_path, optimize=False, compress_level=6)

    return im





def pair(folder_svg, folder_png, name, svg, width=None, height=None):

    """Escribe name.svg en folder_svg y name.png en folder_png."""

    os.makedirs(folder_svg, exist_ok=True)

    open(os.path.join(folder_svg, name + ".svg"), "w", encoding="utf-8").write(svg)

    return render(svg, os.path.join(folder_png, name + ".png"), width, height)





def circ_text(text, cx, cy, r, size, fam="hanken", wt=700, fill="#000", start=-90, ls=0.12, outward=True):

    """Texto sobre círculo, centrado en el ángulo 'start' (grados, -90 = arriba)."""

    widths = [text_width(ch, fam, wt, size) + ls * size for ch in text]

    total = sum(widths) - ls * size

    ang_total = math.degrees(total / r)

    a = start - ang_total / 2 if outward else start + ang_total / 2

    out = []

    for ch, w in zip(text, widths):

        da = math.degrees(w / r)

        mid = a + (da / 2 if outward else -da / 2)

        if ch != " ":

            rad = math.radians(mid)

            x, y = cx + r * math.cos(rad), cy + r * math.sin(rad)

            rot = mid + 90 if outward else mid - 90

            g = text_path(ch, 0, 0, size, fam, wt, fill, "middle")

            out.append(f'<g transform="translate({x:.2f},{y:.2f}) rotate({rot:.2f})">{g}</g>')

        a += da if outward else -da

    return "".join(out)





def qr_path(data, x, y, size, color="#10284d", ec="M"):

    """Código QR como un solo trazado vectorial."""

    import qrcode

    q = qrcode.QRCode(error_correction=getattr(qrcode.constants, "ERROR_CORRECT_" + ec), border=0)

    q.add_data(data)

    q.make(fit=True)

    m = q.get_matrix()

    n = len(m)

    s = size / n

    d = []

    for j, row in enumerate(m):

        i = 0

        while i < n:

            if row[i]:

                k = i

                while k < n and row[k]:

                    k += 1

                d.append(f"M{x + i * s:.2f} {y + j * s:.2f}h{(k - i) * s:.2f}v{s:.2f}h{-(k - i) * s:.2f}z")

                i = k

            else:

                i += 1

    return f'<path fill="{color}" shape-rendering="crispEdges" d="{"".join(d)}"/>'





CODE = {"tnum": True, "zero": True, "ss02": True}





def code_path(text, x, y, size, fill="#1f2d3d", anchor="start", wt=600):

    """Códigos (registro, código corto, DNI): Inter con cifras tabulares y cero con barra."""

    return text_path(text, x, y, size, "inter", wt, fill, anchor, 0.06, feats=CODE)





def print_doc(wmm, hmm, body, defs="", title="IPADECP"):
    """Documento de impresión: 10 unidades por milímetro."""
    W, H = wmm * 10, hmm * 10
    return ('<?xml version="1.0" encoding="UTF-8"?>' + chr(10) + '<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {W} {H}" width="{wmm}mm" height="{hmm}mm"><title>{title}</title>'
            f'<defs>{defs}</defs>{body}</svg>' + chr(10))


def px300(mm):

    return round(mm / 25.4 * 300)



# ---------------------------------------------------------------- modo editable (texto vivo para Illustrator)
EDITABLE = False
PSN = {"hanken": ("HankenGrotesk", "Hanken Grotesk"), "inter": ("Inter", "Inter")}
STY = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold"}
_text_path_curvas = text_path


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text_path(text, x, y, size, fam="hanken", wt=700, fill="#000", anchor="start", ls=0.0, extra="", feats=None):
    if not EDITABLE:
        return _text_path_curvas(text, x, y, size, fam, wt, fill, anchor, ls, extra, feats)
    if not text:
        return ""
    ps, famname = PSN[fam]
    a = "" if anchor == "start" else f' text-anchor="{anchor}"'
    l = f' letter-spacing="{ls*size:.2f}"' if ls else ""
    fv = ' style="font-variant-numeric:tabular-nums slashed-zero"' if feats else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="\'{ps}-{STY[wt]}\', \'{famname}\'" font-weight="{wt}" '
            f'font-size="{size:.1f}" fill="{fill}"{a}{l}{fv}{extra}>{_esc(text)}</text>')


def code_path(text, x, y, size, fill="#1f2d3d", anchor="start", wt=600):
    return text_path(text, x, y, size, "inter", wt, fill, anchor, 0.06, feats=CODE)


def logo_svg_el(version, kind, x, y, w, pfx="L"):
    """Logo como grupo transformado (compatible con Illustrator). Devuelve (defs, el, alto)."""
    bx, by, bw, bh = logo_box(kind)
    h = w * bh / bw
    s = w / bw
    defs, inner = logo_inner(version, pfx)
    clip = ""
    if kind == "isotipo":
        clip = f'<clipPath id="{pfx}iso"><rect x="0" y="0" width="{LW}" height="{ISO_CUT}"/></clipPath>'
        inner = f'<g clip-path="url(#{pfx}iso)">{inner}</g>'
    el = (f'<g id="logo-ipadecp-{kind}-{version}" transform="translate({x:.2f} {y:.2f}) scale({s:.6f})">'
          f'<defs>{defs}{clip}</defs>{inner}</g>')
    return "", el, h
