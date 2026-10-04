"""03 PAPELERIA: certificado, hoja membretada, tarjeta personal, sobre y firma de correo."""
import os
from brandlib import *
from icons import icon_g
from build_assets import globo, WEB, WA

P = os.path.join(OUT, "03 PAPELERIA")
WEBTXT, WATXT, MAIL = "ipadecp.com.pe", "992 951 855", "educacion@ipadecp.com.pe"


def out(sub, name, svg, wmm):
    pair(os.path.join(P, sub, "SVG"), os.path.join(P, sub, "PNG"), name, svg, px300(wmm))


def certificado():
    W, H = 2970, 2100
    b = [f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         # marca de agua: globo lineal
         globo(W / 2, H / 2 + 40, 760, C["cel700"], 3, .07, 9, 8, -18),
         # marco
         f'<rect x="70" y="70" width="{W-140}" height="{H-140}" fill="none" stroke="{C["navy"]}" stroke-width="10"/>',
         f'<rect x="100" y="100" width="{W-200}" height="{H-200}" fill="none" stroke="{C["celeste"]}" stroke-width="3"/>',
         # franja roja del certificado (permitida: es certificación)
         f'<rect x="70" y="70" width="44" height="{H-140}" fill="{C["rojo"]}"/>']
    _, el, lh = logo_svg_el("color", "logotipo", W / 2 - 230, 170, 460)
    b.append(el)
    y = 170 + lh + 160
    b.append(text_path("CERTIFICADO", W / 2, y, 120, "hanken", 800, C["navy500"], "middle", ls=0.18))
    b.append(f'<path d="M{W/2-500} {y+50} Q{W/2} {y+42} {W/2+500} {y+50} Q{W/2} {y+58} {W/2-500} {y+50}z" fill="{C["rojo"]}"/>')
    y += 150
    b.append(text_path("Se otorga a", W / 2, y, 46, "inter", 400, C["gris"], "middle"))
    y += 120
    b.append(text_path("[NOMBRES Y APELLIDOS DEL ALUMNO]", W / 2, y, 92, "hanken", 700, C["navy"], "middle"))
    y += 100
    b.append(text_path("por haber completado el curso", W / 2, y, 46, "inter", 400, C["gris"], "middle"))
    y += 100
    b.append(text_path("[NOMBRE DEL CURSO]", W / 2, y, 70, "hanken", 700, C["tinta"], "middle"))
    y += 80
    b.append(text_path("6 módulos · [N] horas académicas · del [00/00/0000] al [00/00/0000]", W / 2, y, 40, "inter", 500, C["gris"], "middle"))
    # firmas
    fy = H - 330
    for cx, nm, cargo in [(760, "[Nombre y apellidos]", "[Cargo]"), (1560, "[Nombre y apellidos]", "[Cargo]")]:
        b.append(f'<line x1="{cx-260}" y1="{fy}" x2="{cx+260}" y2="{fy}" stroke="{C["tinta"]}" stroke-width="3"/>')
        b.append(text_path(nm, cx, fy + 60, 36, "inter", 600, C["tinta"], "middle"))
        b.append(text_path(cargo, cx, fy + 108, 32, "inter", 400, C["gris"], "middle"))
    # bloque de verificación
    vx, vy = W - 770, H - 610
    b.append(f'<rect x="{vx}" y="{vy}" width="600" height="420" rx="16" fill="{C["rojo050"]}"/>')
    b.append(f'<rect x="{vx+30}" y="{vy+30}" width="230" height="230" fill="#fff"/>')
    b.append(qr_path(WEB, vx + 40, vy + 40, 210, C["navy"], "Q"))
    b.append(text_path("Verifica este", vx + 290, vy + 90, 40, "hanken", 800, C["rojo"]))
    b.append(text_path("certificado", vx + 290, vy + 140, 40, "hanken", 800, C["rojo"]))
    b.append(text_path("Escanea el código QR", vx + 290, vy + 200, 28, "inter", 400, C["rojo700"]))
    b.append(text_path("con tu celular.", vx + 290, vy + 238, 28, "inter", 400, C["rojo700"]))
    b.append(code_path("Código   IPD-0000", vx + 30, vy + 320, 30, C["rojo700"]))
    b.append(code_path("Registro 000000 · Libro 00000", vx + 30, vy + 372, 30, C["rojo700"]))
    svg = print_doc(297, 210, "".join(b), title="Certificado IPADECP (plantilla)")
    out("CERTIFICADO", "certificado-a4-horizontal-plantilla", svg, 297)


def membrete():
    W, H = 2100, 2970
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    _, el, lh = logo_svg_el("color", "logotipo", 150, 120, 300)
    b.append(el)
    for i, t in enumerate([WEBTXT, f"WhatsApp {WATXT}", MAIL]):
        b.append(text_path(t, W - 150, 200 + i * 56, 32, "inter", 500 if i == 0 else 400, C["navy"] if i == 0 else C["gris"], "end"))
    b.append(f'<rect x="150" y="{120+lh+50}" width="{W-300}" height="4" fill="{C["navy"]}"/>')
    # cuerpo de ejemplo
    y = 120 + lh + 200
    b.append(text_path("Lima, [día] de [mes] de [año]", 150, y, 34, "inter", 400, C["tinta"]))
    y += 140
    b.append(text_path("Asunto: [asunto del documento]", 150, y, 38, "hanken", 700, C["navy"]))
    y += 100
    for k in range(14):
        w = W - 300 if k % 5 != 4 else (W - 300) * 0.6
        b.append(f'<rect x="150" y="{y + k*62}" width="{w}" height="16" rx="8" fill="{C["navy100"]}"/>')
    # pie
    b.append(globo(W - 170, H - 160, 320, C["cel700"], 3, .10))
    b.append(f'<path d="M150 {H-210} Q{W/2} {H-216} {W-150} {H-210} Q{W/2} {H-204} 150 {H-210}z" fill="{C["celeste"]}"/>')
    b.append(text_path("Instituto Peruano Americano de Desarrollo y Capacitación Profesional", 150, H - 140, 30, "inter", 600, C["navy"]))
    b.append(text_path(f"{WEBTXT}  ·  WhatsApp {WATXT}  ·  {MAIL}", 150, H - 92, 28, "inter", 400, C["gris"]))
    out("HOJA MEMBRETADA", "hoja-membretada-a4", print_doc(210, 297, "".join(b), title="Hoja membretada"), 210)


def tarjeta():
    W, H = 850, 550
    d, rect = fondo(W, H, "marca")
    f = [rect, globo(W - 60, H - 40, 330, C["celeste"], 2, .25)]
    _, el, lh = logo_svg_el("una-tinta-blanco", "logotipo", (W - 360) / 2, (H - 360 * LH / LW) / 2 - 20, 360)
    f.append(el)
    f.append(text_path(WEBTXT, W / 2, H - 50, 24, "inter", 500, C["celeste"], "middle", ls=0.04))
    out("TARJETA PERSONAL", "tarjeta-personal-frente", print_doc(85, 55, "".join(f), d, "Tarjeta frente"), 85)
    r = [f'<rect width="{W}" height="{H}" fill="#fff"/>', f'<rect width="14" height="{H}" fill="{C["navy"]}"/>']
    r.append(text_path("[Nombres y apellidos]", 70, 120, 44, "hanken", 700, C["navy500"]))
    r.append(text_path("[Cargo]", 70, 168, 26, "inter", 500, C["cel800"]))
    for i, (ic, t) in enumerate([("mensaje", f"WhatsApp {WATXT}"), ("documento", MAIL), ("ubicacion", WEBTXT)]):
        y = 290 + i * 70
        r.append(f'<g transform="translate(70 {y-26}) scale(1.4)">{icon_g(ic, C["navy"], 1.8)}</g>')
        r.append(text_path(t, 120, y, 24, "inter", 400, C["tinta"]))
    r.append(qr_path(WA, W - 230, H - 230, 170, C["navy"], "Q"))
    r.append(text_path("Escríbenos", W - 145, H - 30, 18, "inter", 600, C["gris"], "middle"))
    out("TARJETA PERSONAL", "tarjeta-personal-dorso", print_doc(85, 55, "".join(r), title="Tarjeta dorso"), 85)


def sobre():
    W, H = 2200, 1100
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>', f'<rect y="{H-40}" width="{W}" height="40" fill="{C["rojo"]}"/>',
         globo(W - 150, 180, 380, C["cel700"], 3, .08)]
    _, el, lh = logo_svg_el("color", "logotipo", 110, 90, 260)
    b.append(el)
    b.append(text_path("Certificado IPADECP", 110, 90 + lh + 80, 40, "hanken", 800, C["navy"]))
    b.append(text_path("Documento original. Verifícalo con el código QR.", 110, 90 + lh + 130, 28, "inter", 400, C["gris"]))
    # ventana del destinatario
    b.append(f'<rect x="1150" y="560" width="900" height="360" rx="16" fill="none" stroke="{C["bordef"]}" stroke-width="3" stroke-dasharray="14 10"/>')
    b.append(text_path("Para:", 1190, 630, 30, "inter", 600, C["gris"]))
    b.append(text_path("[Nombres y apellidos]", 1190, 700, 40, "hanken", 700, C["tinta"]))
    b.append(text_path("[Dirección] · [Distrito]", 1190, 760, 32, "inter", 400, C["tinta"]))
    b.append(text_path("[Provincia] · [Departamento]", 1190, 810, 32, "inter", 400, C["tinta"]))
    b.append(text_path("[Celular]", 1190, 860, 32, "inter", 400, C["tinta"]))
    out("SOBRE", "sobre-dl-certificado-fisico", print_doc(220, 110, "".join(b), title="Sobre DL"), 220)


def firma_correo():
    W, H = 1200, 360
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    _, el, lh = logo_svg_el("color", "isotipo", 30, 40, 280)
    b.append(el)
    b.append(f'<rect x="350" y="40" width="4" height="280" fill="{C["navy100"]}"/>')
    b.append(text_path("[Nombres y apellidos]", 390, 105, 44, "hanken", 700, C["navy500"]))
    b.append(text_path("[Cargo] · IPADECP", 390, 155, 28, "inter", 500, C["cel800"]))
    b.append(text_path(f"WhatsApp {WATXT}", 390, 225, 28, "inter", 400, C["tinta"]))
    b.append(text_path(f"{MAIL}  ·  {WEBTXT}", 390, 270, 28, "inter", 400, C["tinta"]))
    svg = svg_doc(W, H, "".join(b), title="Firma de correo")
    pair(os.path.join(P, "FIRMA DE CORREO", "SVG"), os.path.join(P, "FIRMA DE CORREO", "PNG"), "firma-correo-1200x360", svg, 1200)
    render(svg, os.path.join(P, "FIRMA DE CORREO", "PNG", "firma-correo-600x180.png"), 600)


if __name__ == "__main__":
    certificado(); membrete(); tarjeta(); sobre(); firma_correo(); print("papeleria ok")
