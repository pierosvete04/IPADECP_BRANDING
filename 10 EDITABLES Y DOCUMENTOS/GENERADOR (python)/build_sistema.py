"""06 PALETA DE COLORES + 07 TIPOGRAFIAS (muestras) + hoja de marca."""
import os, json, shutil, struct
from brandlib import *
from build_assets import globo

PAL = os.path.join(OUT, "06 PALETA DE COLORES")
TIP = os.path.join(OUT, "07 TIPOGRAFIAS")
SRC = os.path.join(HERE, "..", "branding")


def lum(h):
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contraste(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def cmyk(h):
    r, g, b = [c / 255 for c in rgb(h)]
    k = 1 - max(r, g, b)
    if k >= 1:
        return (0, 0, 0, 100)
    return tuple(round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))


# (grupo, nombre, hex, rol)
GRUPOS = [
    ("Navy · color primario", [
        ("Navy 900", C["navy900"], "Fondo oscuro profundo"), ("Navy 800", C["navy800"], "Hover del primario"),
        ("Navy IPADECP", C["navy"], "Primario de la marca"), ("Navy 600", C["navy600"], "Superficie elevada"),
        ("Navy de texto", C["navy500"], "Titulares"), ("Navy lavado", C["navy100"], "Chips y secciones"),
        ("Fondo suave", C["hueso"], "Fondo del sitio")]),
    ("Celeste · color secundario", [
        ("Celeste profundo", C["cel800"], "Texto y enlaces"), ("Celeste accesible", C["cel700"], "Botón sólido"),
        ("Celeste IPADECP", C["celeste"], "Decorativo; texto solo sobre navy"), ("Celeste 100", C["cel100"], "Superficie de chip"),
        ("Celeste 050", C["cel050"], "Superficie teñida")]),
    ("Rojo · solo certificación   ·   Oro · solo logros", [
        ("Rojo 700", C["rojo700"], "Hover y texto"), ("Rojo IPADECP", C["rojo"], "Sello, certificado, verificación"),
        ("Rojo 050", C["rojo050"], "Superficie del sello"), ("Oro de glifo", C["oro700"], "Estrellas e íconos"),
        ("Oro de logro", C["oro"], "Relleno y bordes"), ("Oro 050", C["oro050"], "Superficie de logro")]),
    ("Neutros", [
        ("Tinta", C["tinta"], "Texto principal"), ("Gris", C["gris"], "Texto secundario"),
        ("Gris tenue", C["tenue"], "Solo decorativo"), ("Borde de campo", C["campo"], "Borde de input"),
        ("Borde fuerte", C["bordef"], "Tablas y separadores"), ("Borde", C["borde"], "Tarjetas")]),
    ("Colores del logotipo", [
        ("Rojo logotipo", C["rojo"], "Arco y filetes"), ("Azul logotipo", C["azul_logo"], "Continentes"),
        ("Cian logotipo", C["cian_logo"], "Libro abierto"), ("Negro logotipo", C["negro"], "Palabra y birrete")]),
]
PRINCIPALES = [("Navy IPADECP", C["navy"], "Primario"), ("Celeste IPADECP", C["celeste"], "Secundario"),
               ("Rojo IPADECP", C["rojo"], "Certificación"), ("Fondo suave", C["hueso"], "Fondo"),
               ("Tinta", C["tinta"], "Texto"), ("Oro de logro", C["oro"], "Logros")]


def badge(h):
    cb, cs = contraste(h, "#ffffff"), contraste(h, C["hueso"])
    best = max(cb, contraste(h, "#000000"))
    if cb >= 7:
        return f"{cb:.2f}:1 AAA", C["ok-texto"] if "ok-texto" in C else "#15703a"
    if cb >= 4.5:
        return f"{cb:.2f}:1 AA", "#15703a"
    if cb >= 3:
        return f"{cb:.2f}:1 grande", "#845c08"
    return f"{cb:.2f}:1 decorativo", C["gris"]


def lamina_paleta():
    W = 3000
    pad, gap = 120, 36
    b, y = [], 0
    y = 230
    b.append(text_path("Paleta IPADECP", pad, 190, 110, "hanken", 800, C["navy500"]))
    b.append(text_path("Contraste WCAG 2.1 medido sobre blanco · HEX, RGB y CMYK de referencia", pad, 255, 36, "inter", 400, C["gris"]))
    b.append(text_path("INSTITUTO PERUANO AMERICANO", W - pad, 160, 28, "hanken", 700, C["gris"], "end", 0.2))
    b.append(text_path("DE DESARROLLO Y CAPACITACIÓN PROFESIONAL", W - pad, 205, 28, "hanken", 700, C["gris"], "end", 0.2))
    y = 310
    b.append(f'<rect x="{pad}" y="{y}" width="{W-2*pad}" height="5" fill="{C["navy"]}"/>')
    y += 110
    for gname, cols in GRUPOS:
        b.append(text_path(gname.upper(), pad, y, 32, "hanken", 700, C["cel800"], ls=0.14))
        y += 40
        n = len(cols)
        cw = (W - 2 * pad - gap * (n - 1)) / n
        ch = 470
        for i, (nm, h, rol) in enumerate(cols):
            x = pad + i * (cw + gap)
            fg = "#ffffff" if contraste(h, "#ffffff") > contraste(h, C["tinta"]) else C["tinta"]
            b.append(f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="{ch}" rx="24" fill="#fff" stroke="{C["borde"]}" stroke-width="3"/>')
            b.append(f'<path d="M{x:.1f} {y+24}a24 24 0 0 1 24-24h{cw-48:.1f}a24 24 0 0 1 24 24v196h{-cw:.1f}z" fill="{h}"/>')
            b.append(text_path(nm, x + 30, y + 270, 34, "hanken", 700, C["tinta"]))
            b.append(code_path(h.upper(), x + 30, y + 318, 28, C["gris"], wt=500))
            r_, g_, b_ = rgb(h)
            c_, m_, yy, k_ = cmyk(h)
            b.append(code_path(f"RGB {r_} {g_} {b_}", x + 30, y + 358, 22, C["gris"], wt=400))
            b.append(code_path(f"CMYK {c_} {m_} {yy} {k_}", x + 30, y + 392, 22, C["gris"], wt=400))
            t, tc = badge(h)
            tw = text_width(t, "inter", 600, 22) + 32
            b.append(f'<rect x="{x+30}" y="{y+410}" width="{tw:.1f}" height="40" rx="8" fill="{tc}"/>')
            b.append(text_path(t, x + 46, y + 438, 22, "inter", 600, "#fff"))
        y += ch + 90
    # degradados
    b.append(text_path("DEGRADADOS · SIEMPRE A 135 GRADOS", pad, y, 32, "hanken", 700, C["cel800"], ls=0.14))
    y += 40
    defs = []
    gl = [("Primario", "primario", "#10284d a #24608f · parada clara 6.68:1"),
          ("Secundario", "secundario", "#0b6683 a #307a99 · parada clara 4.81:1"),
          ("Sello", "sello", "#c6111a a #8f0c12 · solo certificación"),
          ("Marca", "marca", "superficies grandes: héroe, portadas"),
          ("Libro", "libro", "el del logotipo · sin texto encima")]
    n = len(gl)
    cw = (W - 2 * pad - gap * (n - 1)) / n
    for i, (nm, k, sub) in enumerate(gl):
        x = pad + i * (cw + gap)
        defs.append(grad135(f"gr{i}", cw, 300, GRAD[k]).replace('gradientUnits="userSpaceOnUse"', f'gradientUnits="userSpaceOnUse" gradientTransform="translate({x:.1f} {y})"'))
        b.append(f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="300" rx="24" fill="url(#gr{i})"/>')
        b.append(text_path(nm, x + 30, y + 210, 40, "hanken", 800, "#fff"))
        b.append(text_path(sub, x + 30, y + 258, 21, "inter", 500, "#fff"))
    y += 300 + 90
    # reglas
    b.append(f'<rect x="{pad}" y="{y}" width="{W-2*pad}" height="260" rx="24" fill="{C["rojo050"]}"/>')
    b.append(f'<rect x="{pad}" y="{y}" width="12" height="260" fill="{C["rojo"]}"/>')
    b.append(text_path("Las reglas que sostienen la paleta", pad + 50, y + 70, 36, "hanken", 800, C["rojo700"]))
    for i, t in enumerate(["El rojo va solo donde se dice «esto es un certificado real y se puede comprobar». Si ocupa más del 10 % de la pantalla, está mal usado.",
                           "El celeste #6cb3d3 es decorativo sobre fondo claro (2.33:1). Para texto o botón sólido va el celeste 700. Sobre navy sí es texto (6.30:1).",
                           "Un acento por página, y es el rojo. El oro no es color de marca: es el color de un logro."]):
        b.append(text_path(t, pad + 50, y + 130 + i * 48, 26, "inter", 400, C["tinta"]))
    y += 260 + 100
    b.append(text_path("Valores completos en paleta-ipadecp.css y paleta-ipadecp.json", pad, y, 26, "inter", 400, C["gris"]))
    b.append(text_path("ipadecp.com.pe", W - pad, y, 26, "inter", 600, C["gris"], "end"))
    H = y + 90
    svg = svg_doc(W, H, f'<rect width="{W}" height="{H}" fill="{C["hueso"]}"/>' + "".join(b), "".join(defs), "Paleta IPADECP")
    pair(PAL, PAL, "paleta-ipadecp", svg, W)


def archivos_paleta():
    allc = []
    seen = set()
    for _, cols in GRUPOS:
        for nm, h, rol in cols:
            if h not in seen:
                seen.add(h); allc.append((nm, h, rol))
    # ASE (Adobe Swatch Exchange)
    def ase_block(name, h):
        nm = (name + "\0").encode("utf-16-be")
        r, g, b = [c / 255 for c in rgb(h)]
        body = struct.pack(">H", len(name) + 1) + nm + b"RGB " + struct.pack(">fff", r, g, b) + struct.pack(">H", 2)
        return struct.pack(">HI", 0x0001, len(body)) + body
    data = b"ASEF" + struct.pack(">HHI", 1, 0, len(allc)) + b"".join(ase_block(n, h) for n, h, _ in allc)
    open(os.path.join(PAL, "paleta-ipadecp.ase"), "wb").write(data)
    # GIMP / Inkscape
    gpl = "GIMP Palette\nName: IPADECP\nColumns: 6\n#\n" + "".join(f"{rgb(h)[0]:3d} {rgb(h)[1]:3d} {rgb(h)[2]:3d}\t{n}\n" for n, h, _ in allc)
    open(os.path.join(PAL, "paleta-ipadecp.gpl"), "w", encoding="utf-8").write(gpl)
    shutil.copy(os.path.join(SRC, "sistema", "tokens.css"), os.path.join(PAL, "paleta-ipadecp.css"))
    shutil.copy(os.path.join(SRC, "sistema", "tokens.json"), os.path.join(PAL, "paleta-ipadecp.json"))
    json.dump([dict(nombre=n, hex=h, rgb=rgb(h), cmyk=cmyk(h), rol=r, contraste_blanco=round(contraste(h, "#ffffff"), 2)) for n, h, r in allc],
              open(os.path.join(PAL, "paleta-ipadecp-muestras.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def hoja_de_marca():
    W, H = 3000, 2000
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    d, r = fondo(1100, H, "marca", "hm")
    b.append(f'<svg width="1100" height="{H}"><defs>{d}</defs>{r}{globo(900, 1500, 700, C["celeste"], 3, .28)}</svg>')
    _, el, lh = logo_svg_el("una-tinta-blanco", "logotipo", 150, 380, 800)
    b.append(el)
    b.append(text_path("Hoja de marca", 150, 1380, 80, "hanken", 800, "#fff"))
    for i, t in enumerate(["Lleva tu curso y termina con", "un certificado verificable."]):
        b.append(text_path(t, 150, 1470 + i * 60, 44, "inter", 400, C["celeste"]))
    b.append(text_path("ipadecp.com.pe", 150, H - 120, 34, "inter", 600, "#fff"))
    x0 = 1250
    b.append(text_path("COLOR", x0, 220, 32, "hanken", 700, C["cel800"], ls=0.16))
    for i, (nm, h, rol) in enumerate(PRINCIPALES):
        x = x0 + (i % 3) * 530
        y = 260 + (i // 3) * 330
        b.append(f'<rect x="{x}" y="{y}" width="490" height="290" rx="20" fill="{h}" stroke="{C["borde"]}" stroke-width="3"/>')
        fg = "#fff" if contraste(h, "#ffffff") > 4 else C["tinta"]
        b.append(text_path(nm, x + 30, y + 200, 34, "hanken", 700, fg))
        b.append(code_path(h.upper() + "  ·  " + rol, x + 30, y + 248, 24, fg, wt=500))
    y = 1010
    b.append(text_path("TIPOGRAFÍA", x0, y, 32, "hanken", 700, C["cel800"], ls=0.16))
    b.append(text_path("Hanken Grotesk", x0, y + 120, 96, "hanken", 800, C["navy500"]))
    b.append(text_path("Títulos, botones y cifras · 400 600 700 800", x0, y + 175, 30, "inter", 400, C["gris"]))
    b.append(text_path("Inter", x0 + 900, y + 120, 96, "inter", 600, C["navy500"]))
    b.append(text_path("Cuerpo, formularios y tablas · 400 500 600", x0 + 900, y + 175, 30, "inter", 400, C["gris"]))
    y = 1330
    b.append(text_path("TRES REGLAS", x0, y, 32, "hanken", 700, C["cel800"], ls=0.16))
    reglas = ["El logo a color va solo sobre fondo claro. Sobre navy, la versión blanca.",
              "El rojo es de certificación y verificación. Nunca botones ni titulares.",
              "Esquinas 8 / 10 / 16 px. La píldora no es de la marca."]
    for i, t in enumerate(reglas):
        b.append(f'<circle cx="{x0+22}" cy="{y+80+i*90-12}" r="22" fill="{C["navy"]}"/>')
        b.append(text_path(str(i + 1), x0 + 22, y + 80 + i * 90, 28, "hanken", 800, "#fff", "middle"))
        b.append(text_path(t, x0 + 70, y + 80 + i * 90, 34, "inter", 400, C["tinta"]))
    svg = svg_doc(W, H, "".join(b), title="Hoja de marca IPADECP")
    pair(PAL, PAL, "HOJA-DE-MARCA-IPADECP", svg, W)


def muestra_fuente(fam, nombre, pesos, rol, archivo):
    W, H = 2400, 1500
    b = [f'<rect width="{W}" height="{H}" fill="{C["hueso"]}"/>',
         f'<rect x="80" y="80" width="{W-160}" height="{H-160}" rx="32" fill="#fff" stroke="{C["borde"]}" stroke-width="3"/>',
         text_path(rol.upper(), 160, 210, 30, "hanken", 700, C["cel800"], ls=0.16),
         text_path(nombre, 160, 400, 190, fam, 800 if fam == "hanken" else 600, C["navy500"]),
         text_path("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", 160, 560, 64, fam, 400, C["tinta"]),
         text_path("abcdefghijklmnñopqrstuvwxyz", 160, 650, 64, fam, 400, C["tinta"]),
         text_path("0123456789 ¿? ¡! áéíóú · % S/ @", 160, 740, 64, fam, 400, C["tinta"]),
         f'<rect x="160" y="810" width="{W-320}" height="3" fill="{C["borde"]}"/>']
    for i, (w, lbl) in enumerate(pesos):
        x = 160 + i * 520
        b.append(text_path("Aa", x, 1000, 150, fam, w, C["navy500"]))
        b.append(text_path(f"{w} {lbl}", x, 1070, 30, "inter", 500, C["gris"]))
    frase = "Lleva tu curso y termina con un certificado verificable."
    b.append(text_path(frase, 160, 1250, 62, fam, pesos[-1][0] if fam == "hanken" else 500, C["navy"]))
    b.append(text_path("Descarga incluida en 07 TIPOGRAFIAS/INSTALAR · licencia SIL Open Font License", 160, 1340, 28, "inter", 400, C["gris"]))
    pair(os.path.join(TIP, "MUESTRAS", "SVG"), os.path.join(TIP, "MUESTRAS", "PNG"), archivo, svg_doc(W, H, "".join(b)), W)


def escala():
    W = 2400
    filas = [("Display", "800 · -0.02em · 1.08", "Lleva tu curso", 120, "hanken", 800, -0.02),
             ("H1", "700 · -0.015em · 1.15", "Verifica tu certificado en segundos", 88, "hanken", 700, -0.015),
             ("H2", "700 · -0.01em · 1.2", "Estudia a tu ritmo, desde el celular", 64, "hanken", 700, -0.01),
             ("H3", "600 · 1.3", "Aula virtual sin horarios", 40, "hanken", 600, 0),
             ("Cuerpo grande", "Inter 400 · 1.6", "Cada módulo incluye material en Word editable, presentación y una evaluación.", 34, "inter", 400, 0),
             ("Cuerpo", "Inter 400 · 1.6", "El certificado físico llega por courier a cualquier parte del Perú.", 32, "inter", 400, 0),
             ("Etiqueta", "Inter 600 · 0.01em", "Número de documento", 26, "inter", 600, 0.01),
             ("Botón", "Hanken 700", "Llevar este curso", 30, "hanken", 700, 0)]
    b = [text_path("Escala tipográfica", 120, 190, 100, "hanken", 800, C["navy500"]),
         text_path("Dos familias, ninguna tercera. Los tamaños son los de pantalla de escritorio.", 120, 255, 34, "inter", 400, C["gris"])]
    y = 340
    for lbl, spec, txt, sz, fam, wt, ls in filas:
        hgt = max(sz * 1.6, 120)
        b.append(f'<rect x="120" y="{y}" width="{W-240}" height="{hgt:.0f}" fill="#fff" stroke="{C["borde"]}" stroke-width="2"/>')
        b.append(text_path(lbl, 160, y + hgt / 2 - 6, 26, "inter", 600, C["tinta"]))
        b.append(code_path(spec, 160, y + hgt / 2 + 32, 20, C["gris"], wt=400))
        col = C["navy500"] if fam == "hanken" else C["tinta"]
        if lbl == "Botón":
            tw = text_width(txt, fam, wt, sz) + 80
            dd = grad135("btn", tw, 76, GRAD["primario"])
            b.append(f'<svg x="660" y="{y + hgt/2 - 38:.0f}" width="{tw:.0f}" height="76"><defs>{dd}</defs><rect width="{tw:.0f}" height="76" rx="10" fill="url(#btn)"/>{text_path(txt, 40, 49, sz, fam, wt, "#fff")}</svg>')
        else:
            b.append(text_path(txt, 660, y + hgt / 2 + sz * 0.35, sz, fam, wt, col, ls=ls))
        y += hgt
    b.append(text_path("Código", 160, y + 64, 26, "inter", 600, C["tinta"]))
    b.append(f'<rect x="120" y="{y}" width="{W-240}" height="120" fill="#fff" stroke="{C["borde"]}" stroke-width="2"/>')
    b.append(text_path("Código", 160, y + 64, 26, "inter", 600, C["tinta"]))
    b.append(code_path("Registro 000075 · Libro 09000 · IPD-4K7Q", 660, y + 74, 40, C["navy500"]))
    y += 120 + 80
    b.append(text_path("En la web los códigos van en la monoespaciada del sistema; en impresos, Inter con cifras tabulares y cero con barra.", 120, y, 28, "inter", 400, C["gris"]))
    H = y + 80
    svg = svg_doc(W, H, f'<rect width="{W}" height="{H}" fill="{C["hueso"]}"/>' + "".join(b))
    pair(os.path.join(TIP, "MUESTRAS", "SVG"), os.path.join(TIP, "MUESTRAS", "PNG"), "tipografia-escala-ipadecp", svg, W)


def estaticas():
    dst = os.path.join(TIP, "INSTALAR", "ESTATICAS (una por peso)")
    os.makedirs(dst, exist_ok=True)
    nombres = {("hanken", 400): "HankenGrotesk-Regular", ("hanken", 600): "HankenGrotesk-SemiBold",
               ("hanken", 700): "HankenGrotesk-Bold", ("hanken", 800): "HankenGrotesk-ExtraBold",
               ("inter", 400): "Inter-Regular", ("inter", 500): "Inter-Medium", ("inter", 600): "Inter-SemiBold"}
    for (fam, wt), nm in nombres.items():
        font(fam, wt)
        shutil.copy(os.path.join(FONTDIR, f"{fam}-{wt}.ttf"), os.path.join(dst, nm + ".ttf"))


if __name__ == "__main__":
    os.makedirs(PAL, exist_ok=True)
    lamina_paleta(); archivos_paleta(); hoja_de_marca(); print("paleta ok")
    estaticas()
    muestra_fuente("hanken", "Hanken Grotesk", [(400, "regular"), (600, "semibold"), (700, "bold"), (800, "extrabold")],
                   "Títulos, botones y cifras", "tipografia-hanken-grotesk")
    muestra_fuente("inter", "Inter", [(400, "regular"), (500, "medium"), (600, "semibold")],
                   "Cuerpo, formularios y tablas", "tipografia-inter")
    escala(); print("tipografia ok")
