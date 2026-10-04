"""01 LOGOS: versiones, con fondo 1:1, 16:9 y perfil de redes."""
import os
from brandlib import *

L = os.path.join(OUT, "01 LOGOS")
VERS = ["color", "color-plano", "escala-grises", "bn-positivo", "bn-negativo",
        "una-tinta-navy", "una-tinta-negro", "una-tinta-blanco", "una-tinta-rojo"]
OSCURAS = {"bn-negativo", "una-tinta-blanco"}
CLAROS = ["blanco", "hueso", "navy100"]
OSCUROS = ["navy", "navy900", "cel700", "marca", "primario"]
NOMBRE_FONDO = {"blanco": "blanco", "hueso": "hueso", "navy100": "navy-lavado", "navy": "navy",
                "navy900": "navy-profundo", "cel700": "celeste", "marca": "degradado-marca",
                "primario": "degradado-primario"}


def fondos_para(v):
    if v in OSCURAS:
        return OSCUROS
    if v == "una-tinta-rojo":
        return ["blanco", "hueso"]
    return CLAROS


def pieza(v, kind, W, H, bg, escala):
    """Logo centrado en un lienzo W x H. escala = ancho del logo / lado menor."""
    bx, by, bw, bh = logo_box(kind)
    lw = min(W, H) * escala
    lh = lw * bh / bw
    if lh > H * escala:
        lh = H * escala
        lw = lh * bw / bh
    d0, el, _ = logo_svg_el(v, kind, (W - lw) / 2, (H - lh) / 2, lw)
    defs, rect = ("", "") if bg is None else fondo(W, H, bg)
    return svg_doc(W, H, rect + el, defs, f"IPADECP {kind} {v}")


def main():
    n = 0
    for kind, folder in [("logotipo", "LOGO OFICIAL"), ("isotipo", "ISOTIPO")]:
        base = os.path.join(L, folder)
        bx, by, bw, bh = logo_box(kind)
        for v in VERS:
            name = f"{kind}-{v}"
            # 1. sin fondo, ajustado al dibujo
            _, el, _ = logo_svg_el(v, kind, 0, 0, bw)
            svg = svg_doc(bw, bh, el, "", f"IPADECP {kind} {v}")
            pair(os.path.join(base, "SVG"), os.path.join(base, "PNG"), name, svg, width=4000)
            n += 1
            # 2. con fondo 1:1
            for bg in fondos_para(v):
                nm = f"{name}-fondo-{NOMBRE_FONDO[bg]}"
                svg = pieza(v, kind, 3000, 3000, bg, 0.74 if kind == "logotipo" else 0.78)
                pair(os.path.join(base, "CON FONDO 1x1", "SVG"), os.path.join(base, "CON FONDO 1x1", "PNG"), nm, svg, 3000)
                n += 1
            # 3. 16:9 (solo el logotipo completo)
            if kind == "logotipo":
                pair(os.path.join(base, "16x9", "SVG"), os.path.join(base, "16x9", "PNG"), f"{name}-16x9-sin-fondo",
                     pieza(v, kind, 3840, 2160, None, 0.72), 3840)
                for bg in fondos_para(v):
                    pair(os.path.join(base, "16x9", "SVG"), os.path.join(base, "16x9", "PNG"),
                         f"{name}-16x9-fondo-{NOMBRE_FONDO[bg]}", pieza(v, kind, 3840, 2160, bg, 0.72), 3840)
                    n += 1
        print(kind, "ok", n)

    # 4. perfil de redes: círculo seguro del 82 %, la diagonal del logo entra completa
    P = os.path.join(OUT, "08 REDES SOCIALES", "PERFIL")
    import math
    combos = [("logotipo", "una-tinta-blanco", "navy"), ("logotipo", "una-tinta-blanco", "marca"),
              ("logotipo", "color", "blanco"), ("logotipo", "color", "hueso"),
              ("isotipo", "una-tinta-blanco", "navy"), ("isotipo", "color", "blanco"),
              ("logotipo", "una-tinta-blanco", "cel700")]
    for kind, v, bg in combos:
        bx, by, bw, bh = logo_box(kind)
        S = 1080
        diag = math.hypot(bw, bh)
        lw = S * 0.82 * bw / diag
        lh = lw * bh / bw
        _, el, _ = logo_svg_el(v, kind, (S - lw) / 2, (S - lh) / 2, lw)
        defs, rect = fondo(S, S, bg)
        svg = svg_doc(S, S, rect + el, defs)
        nm = f"perfil-{kind}-{v.replace('una-tinta-', '')}-sobre-{NOMBRE_FONDO[bg]}"
        pair(os.path.join(P, "SVG"), os.path.join(P, "PNG"), nm, svg, 1080)
        # vista previa recortada en círculo
        circ = (f'<clipPath id="c"><circle cx="{S/2}" cy="{S/2}" r="{S/2}"/></clipPath>')
        prev = svg_doc(S, S, f'<g clip-path="url(#c)">{rect}{el}</g>', defs + circ)
        render(prev, os.path.join(P, "VISTA PREVIA CIRCULO", nm + "-circulo.png"), 540)
    print("perfil ok")


if __name__ == "__main__":
    main()
