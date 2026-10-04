"""08 REDES SOCIALES: portadas, highlights, posts y stories (plantillas)."""
import os, shutil
from brandlib import *
from icons import icon_g
from build_assets import globo

R = os.path.join(OUT, "08 REDES SOCIALES")
SRC = os.path.join(HERE, "..", "branding")


def save_r(sub, name, svg, w):
    pair(os.path.join(R, sub, "SVG"), os.path.join(R, sub, "PNG"), name, svg, w)


def boton(x, y, txt, size=40, estilo="primario", gid="bt"):
    w = text_width(txt, "hanken", 700, size) + size * 2.2
    h = size * 2.1
    if estilo == "blanco":
        return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h:.0f}" rx="10" fill="#fff"/>'
                + text_path(txt, x + w / 2, y + h / 2 + size * 0.36, size, "hanken", 700, C["navy"], "middle")), w
    d = grad135(gid, w, h, GRAD[estilo]).replace('gradientUnits="userSpaceOnUse"', f'gradientUnits="userSpaceOnUse" gradientTransform="translate({x} {y})"')
    return (f'<defs>{d}</defs><rect x="{x}" y="{y}" width="{w:.0f}" height="{h:.0f}" rx="10" fill="url(#{gid})"/>'
            + text_path(txt, x + w / 2, y + h / 2 + size * 0.36, size, "hanken", 700, "#fff", "middle")), w


def portadas():
    for nm, W, H in [("portada-facebook-1640x624", 1640, 624), ("portada-linkedin-1584x396", 1584, 396),
                     ("portada-youtube-2560x1440", 2560, 1440), ("portada-whatsapp-16x9-1920x1080", 1920, 1080)]:
        d, rect = fondo(W, H, "marca")
        m = min(W, H)
        b = [rect, globo(W * 0.86, H * 0.55, m * 0.75, C["celeste"], max(2, m * 0.003), .3)]
        # zona segura: el contenido va centrado a la izquierda, lejos de la foto de perfil en Facebook
        if "youtube" in nm:
            sx, sy, sw, sh = (W - 1546) / 2, (H - 423) / 2, 1546, 423
        else:
            sx, sy, sw, sh = W * 0.07, H * 0.12, W * 0.62, H * 0.76
        lw = sh * 0.95 * LW / LH
        _, el, lh = logo_svg_el("una-tinta-blanco", "logotipo", sx, sy + (sh - sh * 0.95) / 2, lw)
        b.append(el)
        tx = sx + lw + sh * 0.18
        ts = sh * 0.17
        maxw = W - tx - W * 0.05
        ts = min(ts, ts * maxw / text_width("con un certificado verificable.", "hanken", 800, ts))
        b.append(text_path("Lleva tu curso y termina", tx, sy + sh * 0.42, ts, "hanken", 800, "#fff"))
        b.append(text_path("con un certificado verificable.", tx, sy + sh * 0.42 + ts * 1.15, ts, "hanken", 800, "#fff"))
        b.append(text_path("Cursos para personal de salud · 100 % virtual · ipadecp.com.pe", tx, sy + sh * 0.42 + ts * 2.35, ts * 0.42, "inter", 500, C["celeste"]))
        save_r("PORTADAS", nm, svg_doc(W, H, "".join(b), d), W)
    # el banner de la web que venía en el kit
    dst = os.path.join(R, "PORTADA WEB")
    os.makedirs(dst, exist_ok=True)
    for f in ("banner-escritorio-1920x1080.png", "banner-movil-1080x1920.png"):
        shutil.copy(os.path.join(SRC, "portada", f), os.path.join(dst, f))


HL = [("cursos", "Cursos", "curso"), ("certificado", "Certificado", "certificado"), ("verificar", "Verificar", "verificar"),
      ("envios", "Envíos", "envio"), ("pagos", "Pagos", "pago"), ("preguntas", "Preguntas", "mensaje"),
      ("material", "Material", "documento"), ("alumnos", "Alumnos", "alumno")]


def highlights():
    for slug, lbl, ic in HL:
        for var, bg, fg in [("navy", "navy", "#fff"), ("degradado", "marca", "#fff"), ("hueso", "hueso", C["navy"])]:
            d, rect = fondo(1080, 1080, bg)
            b = rect + f'<g transform="translate(300 300) scale(20)">{icon_g(ic, fg, 1.6)}</g>'
            save_r(os.path.join("HIGHLIGHTS", var), f"highlight-{slug}-{var}-1080", svg_doc(1080, 1080, b, d), 1080)
            d2, rect2 = fondo(1080, 1920, bg)
            b2 = (rect2 + f'<g transform="translate(330 610) scale(17.5)">{icon_g(ic, fg, 1.6)}</g>'
                  + text_path(lbl, 540, 1240, 84, "hanken", 800, fg, "middle"))
            save_r(os.path.join("HIGHLIGHTS", var), f"highlight-{slug}-{var}-story", svg_doc(1080, 1920, b2, d2), 1080)
    # vista previa en círculos
    W, H = 2200, 420
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    for i, (slug, lbl, ic) in enumerate(HL):
        cx = 150 + i * 270
        b.append(f'<circle cx="{cx}" cy="160" r="118" fill="none" stroke="{C["bordef"]}" stroke-width="4"/>')
        b.append(f'<circle cx="{cx}" cy="160" r="104" fill="{C["navy"]}"/>')
        b.append(f'<g transform="translate({cx-50} 110) scale(4.17)">{icon_g(ic, "#fff", 1.6)}</g>')
        b.append(text_path(lbl, cx, 340, 34, "inter", 500, C["tinta"], "middle"))
    save_r("HIGHLIGHTS", "vista-previa-circulos", svg_doc(W, H, "".join(b)), W)


def piezas(W, H, tipo):
    """Tres plantillas de pieza: marca, verificación, curso."""
    out = {}
    m = W
    s = W / 1080
    top = 120 * s if H < 1500 else 260 * s
    # 1. marca
    d, rect = fondo(W, H, "marca")
    b = [rect, globo(W * 0.92, H * 0.8, W * 0.7, C["celeste"], 3, .28)]
    _, el, lh = logo_svg_el("una-tinta-blanco", "logotipo", 90 * s, top, 300 * s)
    b.append(el)
    y = top + lh + 150 * s
    for i, t in enumerate(["Lleva tu curso", "y termina con un", "certificado", "verificable."]):
        b.append(text_path(t, 90 * s, y + i * 112 * s, 104 * s, "hanken", 800, "#fff", ls=-0.02))
    y += 4 * 112 * s + 30 * s
    b.append(text_path("Estudia a tu ritmo, desde el celular.", 90 * s, y, 40 * s, "inter", 400, C["celeste"]))
    bt, _ = boton(90 * s, H - 230 * s, "Ver cursos", 40 * s, "blanco")
    b.append(bt)
    b.append(text_path("ipadecp.com.pe", W - 90 * s, H - 145 * s, 34 * s, "inter", 600, "#fff", "end"))
    out["marca"] = svg_doc(W, H, "".join(b), d)
    # 2. verificación (el rojo entra porque es certificación)
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>', f'<rect width="{W}" height="{24*s}" fill="{C["rojo"]}"/>',
         globo(W * 0.85, H * 0.25, W * 0.5, C["cel700"], 3, .10)]
    _, el, lh = logo_svg_el("color", "logotipo", 90 * s, top, 200 * s)
    b.append(el)
    y = top + lh + 120 * s
    for i, t in enumerate(["Tu certificado", "se comprueba", "en segundos."]):
        b.append(text_path(t, 90 * s, y + i * 92 * s, 86 * s, "hanken", 800, C["navy500"], ls=-0.02))
    y += 2 * 92 * s + 70 * s
    pasos = [("qr", "Escanea el código QR con la cámara del celular."),
             ("verificar", "Mira el registro del certificado al instante."),
             ("alumno", "Sin cuenta ni contraseña.")]
    for i, (ic, t) in enumerate(pasos):
        yy = y + i * 108 * s
        b.append(f'<rect x="{90*s}" y="{yy}" width="{88*s}" height="{88*s}" rx="{16*s}" fill="{C["rojo050"]}"/>')
        b.append(f'<g transform="translate({110*s} {yy+20*s}) scale({2*s})">{icon_g(ic, C["rojo"], 2)}</g>')
        b.append(text_path(t, 210 * s, yy + 56 * s, 36 * s, "inter", 400, C["tinta"]))
    bt, _ = boton(90 * s, H - 230 * s, "Verificar certificado", 40 * s, "sello", "bs")
    b.append(bt)
    out["verificacion"] = svg_doc(W, H, "".join(b))
    # 3. curso (plantilla)
    d, rect = fondo(W, H, "hueso")
    b = [rect, globo(W * 0.9, H * 0.2, W * 0.45, C["cel700"], 3, .14)]
    _, el, lh = logo_svg_el("color", "logotipo", 90 * s, top, 220 * s)
    b.append(el)
    y = top + lh + 120 * s
    b.append(f'<rect x="{90*s}" y="{y-56*s}" width="{250*s}" height="{70*s}" rx="{8*s}" fill="{C["navy100"]}"/>')
    b.append(text_path("CURSO VIRTUAL", 215 * s, y - 10 * s, 28 * s, "hanken", 800, C["navy"], "middle", 0.08))
    y += 120 * s
    b.append(text_path("[Nombre", 90 * s, y, 104 * s, "hanken", 800, C["navy500"], ls=-0.02))
    b.append(text_path("del curso]", 90 * s, y + 112 * s, 104 * s, "hanken", 800, C["navy500"], ls=-0.02))
    y += 112 * s + 120 * s
    for i, (ic, t) in enumerate([("modulos", "6 módulos"), ("a-tu-ritmo", "A tu ritmo, sin horarios"),
                                 ("documento", "Material en Word y PowerPoint editables"), ("certificado", "Certificado con código QR")]):
        yy = y + i * 96 * s
        b.append(f'<g transform="translate({90*s} {yy-34*s}) scale({2*s})">{icon_g(ic, C["cel700"], 2)}</g>')
        b.append(text_path(t, 160 * s, yy, 38 * s, "inter", 500, C["tinta"]))
    bt, _ = boton(90 * s, H - 230 * s, "Llevar este curso", 40 * s, "primario", "bp")
    b.append(bt)
    b.append(text_path("ipadecp.com.pe", W - 90 * s, H - 145 * s, 34 * s, "inter", 600, C["navy"], "end"))
    out["curso"] = svg_doc(W, H, "".join(b), d)
    return out


def posts_y_stories():
    for nm, svg in piezas(1080, 1350, "post").items():
        save_r("POSTS 4x5", f"post-{nm}-1080x1350", svg, 1080)
    for nm, svg in piezas(1080, 1920, "story").items():
        save_r("STORIES", f"story-{nm}-1080x1920", svg, 1080)


def perfil_original():
    dst = os.path.join(R, "PERFIL", "DEL KIT ORIGINAL (raster)")
    shutil.copytree(os.path.join(SRC, "logotipo", "perfil-redes"), dst, dirs_exist_ok=True)


if __name__ == "__main__":
    portadas(); print("portadas")
    highlights(); print("highlights")
    posts_y_stories(); print("posts")
    perfil_original()
