"""Propuestas de certificado digital IPADECP, A4 horizontal."""
import os
from brandlib import *
from icons import icon_g
from build_assets import globo

OUTC = r"F:\TRABAJOS CLAUDE\IPADECP\BRANDING\12 CERTIFICADOS - PROPUESTAS"
W, H = 2970, 2100
URL = "https://ipadecp.com.pe"
NOMBRE = "[Nombres y Apellidos del Alumno]"
CURSO = "[Nombre del curso]"
MODS = ["[Módulo 1]", "[Módulo 2]", "[Módulo 3]", "[Módulo 4]", "[Módulo 5]", "[Módulo 6]"]


def fit(text, size, maxw, fam="hanken", wt=800):
    w = text_width(text, fam, wt, size)
    return size if w <= maxw else size * maxw / w


def verif(x, y, fg, sub, qrbg="#fff", qrcol=None, size=260):
    qrcol = qrcol or C["navy"]
    b = [f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="12" fill="{qrbg}"/>',
         qr_path(URL, x + 18, y + 18, size - 36, qrcol, "Q")]
    tx = x + size + 36
    b.append(text_path("Verifica este certificado", tx, y + 56, 38, "hanken", 800, fg))
    b.append(text_path("Escanea el QR con tu celular.", tx, y + 108, 30, "inter", 400, sub))
    b.append(code_path("Código  IPD-0000", tx, y + 180, 30, sub))
    b.append(code_path("Registro 000000 · Libro 00000", tx, y + 228, 30, sub))
    return "".join(b)


def firma(cx, y, col, sub, w=480):
    return (f'<line x1="{cx-w/2}" y1="{y}" x2="{cx+w/2}" y2="{y}" stroke="{col}" stroke-width="3"/>'
            + text_path("[Nombre y apellidos]", cx, y + 56, 32, "inter", 600, col, "middle")
            + text_path("[Cargo]", cx, y + 100, 28, "inter", 400, sub, "middle"))


def logo(v, x, y, w, kind="logotipo"):
    _, el, h = logo_svg_el(v, kind, x, y, w, pfx=f"L{x:.0f}{y:.0f}")
    return el, h


# 1 ── Panel lateral navy
def p1():
    pw = 900
    d, bg = fondo(pw, H, "marca", "p1")
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<defs>{d}<clipPath id="cp1"><rect width="{pw}" height="{H}"/></clipPath></defs><g id="panel" clip-path="url(#cp1)">{bg}{globo(pw*0.2, H*0.78, 620, C["celeste"], 3, .22)}</g>',
         f'<rect x="{pw}" width="14" height="{H}" fill="{C["rojo"]}"/>']
    el, h = logo("una-tinta-blanco", 150, 170, 600); b.append(el)
    b.append(text_path("Certificado digital", 150, 170 + h + 120, 40, "hanken", 700, C["celeste"]))
    b.append(text_path("Verificable con código QR", 150, 170 + h + 175, 30, "inter", 400, "#cfe0ee"))
    b.append(f'<rect x="150" y="{H-560}" width="300" height="300" rx="14" fill="#fff"/>' + qr_path(URL, 170, H - 540, 260, C["navy"], "Q"))
    b.append(text_path("Escanea para verificar", 150, H - 200, 30, "inter", 600, "#fff"))
    b.append(code_path("IPD-0000 · Reg. 000000", 150, H - 150, 28, C["celeste"]))
    x0 = pw + 180
    b.append(text_path("CERTIFICADO", x0, 430, 64, "hanken", 800, C["cel800"], ls=0.3))
    b.append(text_path("Se otorga a", x0, 640, 40, "inter", 400, C["gris"]))
    b.append(text_path(NOMBRE, x0, 800, fit(NOMBRE, 104, W - x0 - 160), "hanken", 800, C["navy500"], ls=-0.015))
    b.append(f'<rect x="{x0}" y="860" width="160" height="8" rx="4" fill="{C["rojo"]}"/>')
    b.append(text_path("por haber completado satisfactoriamente el curso", x0, 1010, 40, "inter", 400, C["gris"]))
    b.append(text_path(CURSO, x0, 1130, 76, "hanken", 700, C["tinta"]))
    for i, (ic, t) in enumerate([("modulos", "6 módulos"), ("a-tu-ritmo", "[N] horas académicas"), ("evaluacion", "Del [00/00/0000] al [00/00/0000]")]):
        x = x0 + i * 560
        b.append(f'<rect x="{x}" y="1260" width="520" height="110" rx="16" fill="{C["navy100"]}"/>')
        b.append(f'<g transform="translate({x+30} 1285) scale(2.5)">{icon_g(ic, C["navy"], 2)}</g>')
        b.append(text_path(t, x + 110, 1328, 30, "inter", 600, C["navy"]))
    b.append(firma(x0 + 300, 1700, C["tinta"], C["gris"]))
    b.append(firma(x0 + 1000, 1700, C["tinta"], C["gris"]))
    b.append(text_path("Lima, [día] de [mes] de [año]", W - 160, 1960, 28, "inter", 400, C["gris"], "end"))
    return "".join(b)


# 2 ── Banda superior con degradado
def p2():
    bh = 620
    d, bg = fondo(W, bh, "marca", "p2")
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<defs>{d}<clipPath id="cp2"><rect width="{W}" height="{bh}"/></clipPath></defs><g id="banda" clip-path="url(#cp2)">{bg}{globo(W*0.88, bh*0.6, 900, C["celeste"], 3, .25)}</g>',
         f'<path d="M0 {bh} L{W} {bh} L{W} {bh+10} L0 {bh+10}z" fill="{C["rojo"]}"/>']
    el, h = logo("una-tinta-blanco", 160, 110, 470); b.append(el)
    b.append(text_path("CERTIFICADO", 720, 300, 150, "hanken", 800, "#fff", ls=0.12))
    b.append(text_path("de aprobación de curso · 100 % virtual", 726, 390, 44, "inter", 400, C["celeste"]))
    b.append(text_path("Se otorga a", W / 2, 800, 42, "inter", 400, C["gris"], "middle"))
    b.append(text_path(NOMBRE, W / 2, 950, fit(NOMBRE, 110, W - 400), "hanken", 800, C["navy500"], "middle", -0.015))
    b.append(text_path("por haber completado el curso", W / 2, 1060, 42, "inter", 400, C["gris"], "middle"))
    b.append(text_path(CURSO, W / 2, 1170, 78, "hanken", 700, C["cel800"], "middle"))
    b.append(text_path("6 módulos · [N] horas académicas · del [00/00/0000] al [00/00/0000]", W / 2, 1250, 36, "inter", 500, C["gris"], "middle"))
    b.append(f'<rect x="0" y="{H-420}" width="{W}" height="420" fill="{C["hueso"]}"/>')
    b.append(firma(520, H - 250, C["tinta"], C["gris"]))
    b.append(firma(1200, H - 250, C["tinta"], C["gris"]))
    b.append(verif(1700, H - 360, C["rojo"], C["rojo700"], "#fff"))
    return "".join(b)


# 3 ── Minimal con globo
def p3():
    b = [f'<rect width="{W}" height="{H}" fill="{C["hueso"]}"/>',
         globo(W * 0.86, H * 0.42, 1050, C["cel700"], 4, .14, 9, 8),
         f'<rect x="140" y="140" width="{W-280}" height="{H-280}" fill="none" stroke="{C["bordef"]}" stroke-width="3"/>']
    el, h = logo("color", 260, 240, 320); b.append(el)
    b.append(text_path("CERTIFICADO", 260, 240 + h + 130, 44, "hanken", 800, C["cel800"], ls=0.35))
    y = 240 + h + 330
    for i, ln in enumerate(["[Nombres y Apellidos", "del Alumno]"]):
        b.append(text_path(ln, 250, y + i * 160, 150, "hanken", 800, C["navy500"], ls=-0.025))
    y += 160 + 120
    b.append(text_path("completó el curso", 260, y, 44, "inter", 400, C["gris"]))
    b.append(text_path(CURSO, 260, y + 90, 72, "hanken", 700, C["tinta"]))
    b.append(code_path("6 MÓDULOS · [N] HORAS · [00/00/0000]", 260, y + 170, 32, C["gris"], wt=500))
    b.append(firma(560, H - 330, C["tinta"], C["gris"], 560))
    sello_src = open(os.path.join(OUT, "02 SELLOS Y VERIFICACION", "SVG", "sello-verificable-rojo.svg"), encoding="utf-8").read()
    inner = "<defs>" + sello_src.split("<defs>", 1)[1].rsplit("</svg>", 1)[0]
    b.append(f'<g id="sello" transform="translate({W-760} {H-860}) scale(0.44)">{inner}</g>')
    b.append(f'<rect x="{W-1260}" y="{H-380}" width="220" height="220" rx="10" fill="#fff"/>' + qr_path(URL, W - 1245, H - 365, 190, C["navy"], "Q"))
    b.append(text_path("Verifica en segundos", W - 1000, H - 300, 34, "hanken", 800, C["rojo"]))
    b.append(code_path("IPD-0000", W - 1000, H - 245, 30, C["rojo700"]))
    b.append(code_path("Reg. 000000", W - 1000, H - 200, 30, C["rojo700"]))
    return "".join(b)


# 4 ── Clásico moderno con oro
def p4():
    b = [f'<rect width="{W}" height="{H}" fill="#fffdf8"/>',
         f'<rect x="80" y="80" width="{W-160}" height="{H-160}" fill="none" stroke="{C["navy"]}" stroke-width="14"/>',
         f'<rect x="120" y="120" width="{W-240}" height="{H-240}" fill="none" stroke="{C["oro"]}" stroke-width="4"/>']
    for cx, cy, sx, sy in [(120, 120, 1, 1), (W - 120, 120, -1, 1), (120, H - 120, 1, -1), (W - 120, H - 120, -1, -1)]:
        b.append(f'<path d="M{cx} {cy+sy*170} L{cx} {cy} L{cx+sx*170} {cy}" fill="none" stroke="{C["oro"]}" stroke-width="16"/>')
        b.append(f'<circle cx="{cx+sx*60}" cy="{cy+sy*60}" r="14" fill="{C["oro"]}"/>')
    b.append(globo(W / 2, H / 2 + 60, 760, C["oro"], 3, .10, 9, 8))
    el, h = logo("color", W / 2 - 210, 210, 420); b.append(el)
    b.append(text_path("CERTIFICADO", W / 2, 210 + h + 150, 132, "hanken", 800, C["navy500"], "middle", 0.2))
    b.append(text_path("DE APROBACIÓN", W / 2, 210 + h + 220, 36, "hanken", 700, C["oro700"], "middle", 0.4))
    y = 210 + h + 340
    b.append(text_path("Otorgado a", W / 2, y, 40, "inter", 400, C["gris"], "middle"))
    b.append(text_path(NOMBRE, W / 2, y + 130, fit(NOMBRE, 100, W - 700), "hanken", 700, C["navy"], "middle"))
    b.append(f'<path d="M{W/2-560} {y+175} Q{W/2} {y+168} {W/2+560} {y+175} Q{W/2} {y+182} {W/2-560} {y+175}z" fill="{C["oro"]}"/>')
    b.append(text_path("por haber completado el curso " + CURSO, W / 2, y + 270, 42, "inter", 500, C["tinta"], "middle"))
    b.append(text_path("6 módulos · [N] horas académicas · del [00/00/0000] al [00/00/0000]", W / 2, y + 335, 34, "inter", 400, C["gris"], "middle"))
    b.append(firma(640, H - 330, C["tinta"], C["gris"]))
    b.append(firma(W - 640, H - 330, C["tinta"], C["gris"]))
    sello_src = open(os.path.join(OUT, "02 SELLOS Y VERIFICACION", "SVG", "sello-logro-curso-completado-oro.svg"), encoding="utf-8").read()
    inner = "<defs>" + sello_src.split("<defs>", 1)[1].rsplit("</svg>", 1)[0]
    b.append(f'<g id="sello" transform="translate({W/2-210} {H-560}) scale(0.42)">{inner}</g>')
    b.append(f'<rect x="{W-420}" y="{H-430}" width="190" height="190" fill="#fff"/>' + qr_path(URL, W - 410, H - 420, 170, C["navy"], "Q"))
    b.append(code_path("IPD-0000", W - 325, H - 200, 24, C["gris"], "middle"))
    return "".join(b)


# 5 ── Credencial oscura
def p5():
    d, bg = fondo(W, H, "navy900", "p5")
    b = [bg, globo(W * 0.9, H * 0.15, 1100, C["celeste"], 3, .18, 9, 8),
         f'<rect x="0" y="0" width="{W}" height="16" fill="url(#lb5)"/>']
    defs = grad135("lb5", W, 16, GRAD["libro"]) + d
    el, h = logo("una-tinta-blanco", 180, 170, 360); b.append(el)
    b.append(f'<rect x="{W-760}" y="200" width="580" height="90" rx="10" fill="none" stroke="{C["celeste"]}" stroke-width="3"/>')
    b.append(text_path("CERTIFICADO DIGITAL", W - 470, 260, 34, "hanken", 800, C["celeste"], "middle", 0.16))
    y = 170 + h + 210
    b.append(text_path("Se certifica que", 180, y, 42, "inter", 400, "#b8c7d6"))
    b.append(text_path(NOMBRE, 180, y + 150, fit(NOMBRE, 124, W - 360), "hanken", 800, "#fff", ls=-0.02))
    b.append(text_path("completó el curso", 180, y + 260, 42, "inter", 400, "#b8c7d6"))
    b.append(text_path(CURSO, 180, y + 370, 84, "hanken", 700, C["celeste"]))
    yy = y + 470
    for i, (lbl, val) in enumerate([("Módulos", "6 de 6"), ("Horas", "[N]"), ("Avance", "100 %"), ("Emitido", "[00/00/0000]")]):
        x = 180 + i * 470
        b.append(f'<rect x="{x}" y="{yy}" width="430" height="170" rx="16" fill="{C["navy600"]}"/>')
        b.append(text_path(lbl.upper(), x + 36, yy + 60, 26, "hanken", 700, C["celeste"], ls=0.14))
        b.append(text_path(val, x + 36, yy + 135, 56, "hanken", 800, "#fff"))
    b.append(firma(W - 640, H - 420, "#fff", "#b8c7d6"))
    b.append(f'<rect x="180" y="{H-330}" width="{W-360}" height="2" fill="{C["navy600"]}"/>')
    b.append(f'<rect x="{W-480}" y="{H-280}" width="0" height="0"/>')
    b.append(qr_path(URL, 180, H - 280, 180, "#fff", "Q"))
    b.append(text_path("Verifica este certificado escaneando el QR. Sin cuenta ni contraseña.", 410, H - 205, 34, "inter", 500, "#fff"))
    b.append(code_path("Código IPD-0000 · Registro 000000 · Libro 00000", 410, H - 145, 30, C["celeste"]))
    return "".join(b), defs


# 6 ── Con detalle de módulos
def p6():
    cw = 860
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<rect x="{W-cw}" width="{cw}" height="{H}" fill="{C["hueso"]}"/>',
         f'<rect x="{W-cw}" width="10" height="{H}" fill="{C["rojo"]}"/>']
    el, h = logo("color", 180, 150, 300); b.append(el)
    b.append(text_path("CERTIFICADO", 540, 300, 96, "hanken", 800, C["navy500"], ls=0.1))
    b.append(text_path("Curso virtual completado", 546, 370, 36, "inter", 500, C["cel800"]))
    y = 760
    b.append(text_path("Se otorga a", 180, y, 40, "inter", 400, C["gris"]))
    b.append(text_path(NOMBRE, 180, y + 130, fit(NOMBRE, 100, W - cw - 340), "hanken", 800, C["navy500"], ls=-0.015))
    b.append(text_path("por haber completado el curso", 180, y + 240, 40, "inter", 400, C["gris"]))
    b.append(text_path(CURSO, 180, y + 345, 76, "hanken", 700, C["tinta"]))
    b.append(text_path("[N] horas académicas · del [00/00/0000] al [00/00/0000]", 180, y + 420, 34, "inter", 400, C["gris"]))
    b.append(firma(470, H - 300, C["tinta"], C["gris"]))
    b.append(firma(1260, H - 300, C["tinta"], C["gris"]))
    x = W - cw + 110
    b.append(text_path("CONTENIDO DEL CURSO", x, 230, 30, "hanken", 800, C["cel800"], ls=0.14))
    for i, m in enumerate(MODS):
        yy = 320 + i * 150
        b.append(f'<circle cx="{x+36}" cy="{yy+30}" r="36" fill="{C["navy"]}"/>')
        b.append(text_path(str(i + 1), x + 36, yy + 44, 36, "hanken", 800, "#fff", "middle"))
        b.append(text_path(m, x + 100, yy + 26, 34, "hanken", 700, C["tinta"]))
        b.append(text_path("Aprobado", x + 100, yy + 70, 26, "inter", 500, C["ok"] if "ok" in C else "#15703a"))
    b.append(f'<rect x="{x}" y="{H-470}" width="{cw-220}" height="330" rx="16" fill="#fff"/>')
    b.append(qr_path(URL, x + 30, H - 440, 270, C["navy"], "Q"))
    b.append(text_path("Verifica", x + 340, H - 360, 38, "hanken", 800, C["rojo"]))
    b.append(text_path("este certificado", x + 340, H - 312, 30, "inter", 500, C["rojo700"]))
    b.append(code_path("IPD-0000", x + 340, H - 230, 28, C["rojo700"]))
    b.append(code_path("Reg. 000000", x + 340, H - 185, 28, C["rojo700"]))
    return "".join(b)


PROP = [("01-panel-lateral-navy", "Panel lateral navy", p1),
        ("02-banda-degradado", "Banda con degradado", p2),
        ("03-minimal-globo", "Minimal con globo", p3),
        ("04-clasico-oro", "Clásico moderno con oro", p4),
        ("05-credencial-oscura", "Credencial digital oscura", p5),
        ("06-detalle-de-modulos", "Con detalle de módulos", p6)]

if __name__ == "__main__":
    C.setdefault("ok", "#15703a")
    from PIL import Image
    thumbs = []
    import brandlib
    for slug, nombre, fn in PROP:
        brandlib.EDITABLE = True
        r = fn()
        body, defs = (r if isinstance(r, tuple) else (r, ""))
        ed = print_doc(297, 210, body, defs, f"Certificado IPADECP · {nombre}")
        os.makedirs(os.path.join(OUTC, "SVG EDITABLE (texto vivo)"), exist_ok=True)
        open(os.path.join(OUTC, "SVG EDITABLE (texto vivo)", f"certificado-{slug}-editable.svg"), "w", encoding="utf-8").write(ed)
        brandlib.EDITABLE = False
        r = fn()
        body, defs = (r if isinstance(r, tuple) else (r, ""))
        svg = print_doc(297, 210, body, defs, f"Certificado IPADECP · {nombre}")
        im = pair(os.path.join(OUTC, "SVG EN CURVAS"), os.path.join(OUTC, "PNG"), f"certificado-{slug}", svg, px300(297))
        thumbs.append((nombre, im))
        print(slug)
    # hoja comparativa
    tw, th, g = 1100, 778, 60
    sheet = Image.new("RGB", (tw * 2 + g * 3, (th + 110) * 3 + g * 2), C["navy100"])
    from PIL import ImageDraw, ImageFont
    dr = ImageDraw.Draw(sheet)
    f = ImageFont.truetype(os.path.join(FONTDIR, "hanken-700.ttf"), 44)
    for i, (n, im) in enumerate(thumbs):
        x = g + (i % 2) * (tw + g); y = g + (i // 2) * (th + 110)
        t = im.convert("RGB").resize((tw, th), Image.LANCZOS)
        sheet.paste(t, (x, y))
        dr.text((x, y + th + 22), f"{i+1}. {n}", font=f, fill=C["navy500"])
    sheet.save(os.path.join(OUTC, "COMPARATIVA-PROPUESTAS.png"))
    print("ok")
