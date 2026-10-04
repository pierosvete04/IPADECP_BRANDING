"""02 SELLOS Y VERIFICACION + 04 ASSETS (íconos, QR, globo lineal, patrones, fondos)."""
import os, math
from brandlib import *
from icons import ICONS, NOMBRES, icon_g

A = os.path.join(OUT, "04 ASSETS")
S2 = os.path.join(OUT, "02 SELLOS Y VERIFICACION")
WEB = "https://ipadecp.com.pe"
WA = "https://wa.me/51992951855"


# ------------------------------------------------------------ globo lineal
def globo(cx, cy, r, color, sw, op=1.0, meridianos=7, paralelos=6, tilt=-18):
    """Malla de globo como la del logotipo: meridianos y paralelos."""
    g = [f'<circle cx="0" cy="0" r="{r}"/>']
    for k in range(1, meridianos):
        t = math.cos(math.pi * k / meridianos)
        rx = abs(r * t)
        if rx > 1:
            g.append(f'<ellipse cx="0" cy="0" rx="{rx:.1f}" ry="{r}"/>')
    g.append(f'<line x1="0" y1="{-r}" x2="0" y2="{r}"/>')
    for k in range(1, paralelos):
        y = -r + 2 * r * k / paralelos
        w = math.sqrt(max(r * r - y * y, 0))
        g.append(f'<path d="M{-w:.1f} {y:.1f} Q0 {y + r * 0.12:.1f} {w:.1f} {y:.1f}"/>')
    return (f'<g transform="translate({cx},{cy}) rotate({tilt})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-opacity="{op}" stroke-linecap="round">{"".join(g)}</g>')


def iconos():
    base = os.path.join(A, "ICONOS")
    lineal = {"navy": C["navy"], "celeste": C["cel700"], "blanco": C["blanco"], "negro": C["negro"], "gris": C["gris"]}
    circulo = {"navy": (C["navy"], C["blanco"]), "celeste": (C["cel700"], C["blanco"]),
               "lavado": (C["navy100"], C["navy"]), "degradado": ("primario", C["blanco"])}
    for n in ICONS:
        for k, col in lineal.items():
            svg = svg_doc(24, 24, icon_g(n, col), title=NOMBRES[n])
            pair(os.path.join(base, "SVG", "lineal", k), os.path.join(base, "PNG", "lineal", k), f"icono-{n}-{k}", svg, 1024)
        for k, (bg, fg) in circulo.items():
            defs = ""
            if bg in GRAD:
                defs = grad135("g", 48, 48, GRAD[bg])
                bgf = "url(#g)"
            else:
                bgf = bg
            body = f'<circle cx="24" cy="24" r="24" fill="{bgf}"/><g transform="translate(12 12)">{icon_g(n, fg)}</g>'
            pair(os.path.join(base, "SVG", "circulo", k), os.path.join(base, "PNG", "circulo", k),
                 f"icono-{n}-circulo-{k}", svg_doc(48, 48, body, defs, NOMBRES[n]), 1024)
    # lámina de muestra
    names = list(ICONS)
    cols, cell = 5, 300
    rows = math.ceil(len(names) / cols)
    W, H = cols * cell + 160, rows * cell + 300
    body = [f'<rect width="{W}" height="{H}" fill="{C["hueso"]}"/>',
            text_path(f"Íconos IPADECP · {len(ICONS)}", 80, 120, 64, "hanken", 800, C["navy500"]),
            text_path("Retícula de 24 · trazo de 2 · puntas y uniones redondas", 80, 175, 26, "inter", 400, C["gris"])]
    for i, n in enumerate(names):
        x, y = 80 + (i % cols) * cell, 230 + (i // cols) * cell
        body.append(f'<rect x="{x+10}" y="{y}" width="{cell-20}" height="{cell-30}" rx="16" fill="#fff" stroke="{C["borde"]}" stroke-width="2"/>')
        body.append(f'<g transform="translate({x + cell/2 - 60} {y + 40}) scale(5)">{icon_g(n, C["navy"])}</g>')
        body.append(text_path(NOMBRES[n], x + cell / 2, y + 230, 24, "inter", 600, C["tinta"], "middle"))
    svg = svg_doc(W, H, "".join(body))
    pair(base, base, "MUESTRA-ICONOS", svg, W)


def qrs():
    base = os.path.join(A, "QR")
    for nm, url in [("qr-web-ipadecp", WEB), ("qr-whatsapp-ipadecp", WA)]:
        for k, col in [("navy", C["navy"]), ("negro", C["negro"]), ("blanco", C["blanco"])]:
            svg = svg_doc(1000, 1000, qr_path(url, 0, 0, 1000, col, "Q"), title=url)
            pair(os.path.join(base, "SVG"), os.path.join(base, "PNG"), f"{nm}-{k}", svg, 2000)
        # tarjeta con QR y rótulo
        lab = "Visita ipadecp.com.pe" if "web" in nm else "Escríbenos por WhatsApp"
        body = (f'<rect width="1200" height="1450" rx="64" fill="#fff"/>'
                f'<rect x="4" y="4" width="1192" height="1442" rx="60" fill="none" stroke="{C["navy"]}" stroke-width="8"/>'
                + qr_path(url, 150, 150, 900, C["navy"], "Q")
                + text_path(lab, 600, 1200, 64, "hanken", 800, C["navy500"], "middle")
                + text_path("Escanea con la cámara del celular", 600, 1290, 40, "inter", 400, C["gris"], "middle"))
        pair(os.path.join(base, "SVG"), os.path.join(base, "PNG"), f"{nm}-tarjeta", svg_doc(1200, 1450, body), 1200)


def sellos():
    R = 500
    def sello(fondo_c, tinta, borde, nm, top, bottom, icono, centro1, centro2, ink2=None):
        ink2 = ink2 or tinta
        defs = ""
        if fondo_c in GRAD:
            defs = grad135("sg", 1000, 1000, GRAD[fondo_c]); fill = "url(#sg)"
        else:
            fill = fondo_c
        b = [f'<circle cx="500" cy="500" r="490" fill="{fill}"/>',
             f'<circle cx="500" cy="500" r="462" fill="none" stroke="{borde}" stroke-width="10"/>',
             f'<circle cx="500" cy="500" r="330" fill="none" stroke="{borde}" stroke-width="5"/>',
             circ_text(top, 500, 500, 378, 48, "hanken", 800, tinta, -90, 0.10),
             circ_text(bottom, 500, 500, 414, 42, "hanken", 700, tinta, 90, 0.12, outward=False)]
        for a in (180, 0):
            x = 500 + 395 * math.cos(math.radians(a))
            b.append(f'<circle cx="{x:.1f}" cy="500" r="11" fill="{tinta}"/>')
        b.append(f'<g transform="translate(395 300) scale(8.75)">{icon_g(icono, ink2, 2)}</g>')
        b.append(text_path(centro1, 500, 600, 66, "hanken", 800, ink2, "middle"))
        b.append(text_path(centro2, 500, 670, 40, "inter", 600, ink2, "middle", ls=0.06))
        svg = svg_doc(1000, 1000, "".join(b), defs, nm)
        pair(os.path.join(S2, "SVG"), os.path.join(S2, "PNG"), nm, svg, 3000)

    V = ("CERTIFICADO VERIFICABLE", "IPADECP · DESDE 2015", "verificar", "VERIFICA", "CON CÓDIGO QR")
    sello("sello", C["blanco"], C["blanco"], "sello-verificable-rojo", *V)
    sello(C["blanco"], C["rojo"], C["rojo"], "sello-verificable-rojo-sobre-blanco", *V)
    sello(C["rojo050"], C["rojo"], C["rojo"], "sello-verificable-rojo-sobre-rojo050", *V)
    sello(C["navy"], C["blanco"], C["blanco"], "sello-verificable-blanco-sobre-navy", *V)
    L = ("CURSO COMPLETADO", "IPADECP · 6 DE 6 MÓDULOS", "logro", "100 %", "DE AVANCE")
    sello(C["oro050"], C["oro700"], C["oro"], "sello-logro-curso-completado-oro", *L)
    sello(C["blanco"], C["oro700"], C["oro"], "sello-logro-curso-completado-oro-sobre-blanco", *L)

    # insignia horizontal de verificación (para el certificado y la web)
    for nm, bg, fg, sub in [("insignia-verifica-este-certificado", C["rojo050"], C["rojo"], C["rojo700"]),
                            ("insignia-verifica-este-certificado-blanco", C["rojo"], C["blanco"], C["blanco"])]:
        body = (f'<rect width="1600" height="420" rx="32" fill="{bg}"/>'
                f'<rect x="40" y="40" width="340" height="340" rx="16" fill="#fff"/>'
                + qr_path(WEB, 60, 60, 300, C["navy"], "Q")
                + f'<g transform="translate(440 70) scale(4)">{icon_g("verificar", fg, 2)}</g>'
                + text_path("Verifica este certificado", 560, 125, 66, "hanken", 800, fg)
                + text_path("Escanea el código QR con la cámara del celular.", 440, 235, 40, "inter", 400, sub)
                + text_path("No necesitas cuenta ni contraseña.", 440, 295, 40, "inter", 400, sub)
                + text_path("Código corto  IPD-0000", 440, 365, 36, "inter", 600, sub, ls=0.06))
        pair(os.path.join(S2, "SVG"), os.path.join(S2, "PNG"), nm, svg_doc(1600, 420, body), 3200)


def graficos():
    base = os.path.join(A, "ELEMENTOS GRAFICOS")
    for k, col in [("navy", C["navy"]), ("celeste", C["celeste"]), ("blanco", C["blanco"]), ("celeste-700", C["cel700"])]:
        svg = svg_doc(1000, 1000, globo(500, 500, 470, col, 6), title="Globo lineal")
        pair(os.path.join(base, "SVG"), os.path.join(base, "PNG"), f"globo-lineal-{k}", svg, 3000)
    # filete rojo del logotipo (línea afinada en las puntas)
    for k, col in [("rojo", C["rojo"]), ("navy", C["navy"]), ("blanco", C["blanco"])]:
        svg = svg_doc(2000, 40, f'<path d="M0 20 Q1000 6 2000 20 Q1000 34 0 20z" fill="{col}"/>', title="Filete")
        pair(os.path.join(base, "SVG"), os.path.join(base, "PNG"), f"filete-{k}", svg, 4000)
    # barra de progreso con el degradado del libro
    d = grad135("lb", 1200, 40, GRAD["libro"])
    svg = svg_doc(1200, 40, f'<rect width="1200" height="40" rx="8" fill="{C["navy100"]}"/><rect width="840" height="40" rx="8" fill="url(#lb)"/>', d, "Barra de avance")
    pair(os.path.join(base, "SVG"), os.path.join(base, "PNG"), "barra-de-avance-degradado-libro", svg, 2400)


def patrones():
    base = os.path.join(A, "PATRONES")
    T = 240
    tiles = {
        "malla-globo": lambda c, op: globo(T / 2, T / 2, 100, c, 2, op, 5, 4, -18),
        "diagonal-135": lambda c, op: f'<path d="M-60 {T} L{T} -60 M{T/2-60} {T+60} L{T+60} {T/2-60} M-60 {T/2} L{T/2} -60" stroke="{c}" stroke-opacity="{op}" stroke-width="3"/>',
        "puntos": lambda c, op: "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" fill-opacity="{op}"/>' for x in (30, 90, 150, 210) for y in (30, 90, 150, 210)),
        "qr": lambda c, op: qr_path("IPADECP", 20, 20, 200, c, "L").replace("<path", f'<path fill-opacity="{op}"', 1),
    }
    fondos_p = [("sobre-navy", C["navy"], C["celeste"], .35), ("sobre-hueso", C["hueso"], C["cel700"], .22),
                ("sobre-blanco", C["blanco"], C["navy"], .12), ("transparente", None, C["navy"], .25)]
    for nm, fn in tiles.items():
        for fk, bg, fg, op in fondos_p:
            pat = f'<pattern id="p" width="{T}" height="{T}" patternUnits="userSpaceOnUse">{fn(fg, op)}</pattern>'
            W = H = 2400
            body = (f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else "") + f'<rect width="{W}" height="{H}" fill="url(#p)"/>'
            pair(os.path.join(base, "SVG"), os.path.join(base, "PNG"), f"patron-{nm}-{fk}", svg_doc(W, H, body, pat), 2400)


def fondos_marca():
    base = os.path.join(A, "FONDOS")
    formatos = {"16x9": (3840, 2160), "story-9x16": (1080, 1920), "post-4x5": (1080, 1350), "cuadrado-1x1": (1080, 1080)}
    for fk, (W, H) in formatos.items():
        m = min(W, H)
        variantes = {
            "degradado-marca-globo": ("marca", globo(W * 0.82, H * 0.62, m * 0.62, C["celeste"], m * 0.003, .35)),
            "navy-globo": ("navy", globo(W * 0.85, H * 0.5, m * 0.7, C["celeste"], m * 0.003, .28)),
            "hueso-globo": ("hueso", globo(W * 0.85, H * 0.55, m * 0.65, C["cel700"], m * 0.003, .18)),
            "degradado-primario": ("primario", ""),
            "degradado-libro": ("libro", globo(W * 0.5, H * 0.5, m * 0.55, C["blanco"], m * 0.003, .22)),
            "navy-profundo-filete": ("navy900", f'<path d="M{W*0.06} {H*0.86} Q{W/2} {H*0.86-6} {W*0.94} {H*0.86} Q{W/2} {H*0.86+6} {W*0.06} {H*0.86}z" fill="{C["celeste"]}"/>'),
        }
        for vk, (bg, extra) in variantes.items():
            d, rect = fondo(W, H, bg)
            pair(os.path.join(base, fk, "SVG"), os.path.join(base, fk, "PNG"), f"fondo-{vk}-{fk}", svg_doc(W, H, rect + extra, d), W)


if __name__ == "__main__":
    iconos(); print("iconos")
    qrs(); print("qr")
    sellos(); print("sellos")
    graficos(); print("graficos")
    patrones(); print("patrones")
    fondos_marca(); print("fondos")
