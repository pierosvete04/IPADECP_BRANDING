"""11 GOOGLE FLOW: cada PNG con un nombre corto para llamarlo con @ en Flow."""
import os, re, sys, unicodedata, shutil
from collections import defaultdict
from PIL import Image, PngImagePlugin

Image.MAX_IMAGE_PIXELS = None
BR = r"F:\TRABAJOS CLAUDE\IPADECP\BRANDING"
CERT = r"F:\TRABAJOS CLAUDE\IPADECP\BRANDING\12 CERTIFICADOS - PROPUESTAS"
FLOW = os.path.join(BR, "11 GOOGLE FLOW")
MAXL = 2048


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def limpia(t):
    rep = [("una_tinta_", ""), ("color_plano", "planos"), ("escala_grises", "grises"), ("degradado_marca", "degradado"),
           ("navy_lavado", "lavado"), ("navy_profundo", "navy_oscuro"), ("16x9_sin_fondo", "16x9"), ("sin_fondo", ""),
           ("_1080x1350", ""), ("_1080x1920", ""), ("_1080", ""), ("sobre_", "fondo_")]
    for a, b in rep:
        t = t.replace(a, b)
    return re.sub(r"_+", "_", t).strip("_")


def nombre(path):
    rel = os.path.relpath(path, BR) if path.startswith(BR) else os.path.relpath(path, CERT)
    parts = rel.split(os.sep)
    base = slug(os.path.splitext(parts[-1])[0])
    top = parts[0]
    if path.startswith(CERT):
        if base.startswith("comparativa"):
            return "certificados", "certificados_ipadecp_comparativa"
        t = re.sub(r"^certificado_\d+_", "", base)
        return "certificados", f"certificado_ipadecp_{t}"
    if top == "01 LOGOS":
        kind = "logo" if base.startswith("logotipo") else "isotipo"
        rest = limpia(re.sub(r"^(logotipo|isotipo)_", "", base))
        return "logos", f"{kind}_ipadecp_{rest}"
    if top == "02 SELLOS Y VERIFICACION":
        t = limpia(base).replace("sello_verificable", "verificable").replace("sello_logro_curso_completado", "logro")
        t = t.replace("insignia_verifica_este_certificado", "insignia_verifica")
        cat = "insignia" if t.startswith("insignia") else "sello"
        t = t.replace("insignia_", "")
        return "sellos", f"{cat}_ipadecp_{t}"
    if top == "03 PAPELERIA":
        m = {"certificado_a4_horizontal_plantilla": "certificado_ipadecp_plantilla", "hoja_membretada_a4": "membrete_ipadecp",
             "tarjeta_personal_frente": "tarjeta_ipadecp_frente", "tarjeta_personal_dorso": "tarjeta_ipadecp_dorso",
             "sobre_dl_certificado_fisico": "sobre_ipadecp", "firma_correo_1200x360": "firma_correo_ipadecp",
             "firma_correo_600x180": "firma_correo_ipadecp_chica"}
        return "papeleria", m.get(base, f"papeleria_ipadecp_{base}")
    if top == "04 ASSETS":
        sub = parts[1]
        if sub == "ICONOS":
            if base == "muestra_iconos":
                return "iconos", "iconos_ipadecp_muestra"
            t = re.sub(r"^icono_", "", base).replace("_circulo_", "_circulo_")
            return "iconos", f"icono_ipadecp_{t}"
        if sub == "ELEMENTOS GRAFICOS":
            t = base.replace("barra_de_avance_degradado_libro", "barra_avance").replace("globo_lineal", "globo")
            first, _, rest = t.partition("_")
            return "elementos", f"{first}_ipadecp_{rest}".strip("_")
        if sub == "PATRONES":
            return "patrones", "patron_ipadecp_" + limpia(re.sub(r"^patron_", "", base))
        if sub == "FONDOS":
            t = limpia(re.sub(r"^fondo_", "", base)).replace("story_9x16", "story").replace("post_4x5", "post").replace("cuadrado_1x1", "cuadrado")
            return "fondos", f"fondo_ipadecp_{t}"
        if sub == "QR":
            t = re.sub(r"^qr_", "", base).replace("_ipadecp", "")
            return "qr", f"qr_ipadecp_{t}"
        if sub == "FOTOGRAFIA":
            return "fotos", f"foto_ipadecp_{base}"
    if top == "05 MOCKUPS":
        return "mockups", "mockup_ipadecp_" + re.sub(r"^mockup_", "", base).replace("_y_", "_")
    if top == "06 PALETA DE COLORES":
        return "paleta", {"paleta_ipadecp": "paleta_ipadecp", "hoja_de_marca_ipadecp": "hoja_de_marca_ipadecp"}.get(base, base)
    if top == "07 TIPOGRAFIAS":
        t = re.sub(r"^tipografia_", "", base).replace("_ipadecp", "")
        return "tipografias", f"tipografia_ipadecp_{t}"
    if top == "08 REDES SOCIALES":
        sub = parts[1]
        if sub == "PERFIL":
            if "VISTA PREVIA" in rel:
                t = limpia(re.sub(r"^perfil_", "", base)).replace("_circulo", "")
                return "redes", f"perfil_ipadecp_{t}_circulo"
            return "redes", "perfil_ipadecp_" + limpia(re.sub(r"^perfil_", "", base))
        if sub == "PORTADAS":
            t = re.sub(r"^portada_", "", base)
            t = re.sub(r"_\d+x\d+$", "", t).replace("_16x9", "")
            return "redes", f"portada_ipadecp_{t}"
        if sub == "PORTADA WEB":
            return "redes", "banner_web_ipadecp_" + ("escritorio" if "escritorio" in base else "movil")
        if sub == "HIGHLIGHTS":
            if base == "vista_previa_circulos":
                return "redes", "highlights_ipadecp_vista_previa"
            t = limpia(re.sub(r"^highlight_", "", base))
            return "redes", f"highlight_ipadecp_{t}"
        if sub == "POSTS 4x5":
            return "redes", "post_ipadecp_" + limpia(re.sub(r"^post_", "", base))
        if sub == "STORIES":
            return "redes", "story_ipadecp_" + limpia(re.sub(r"^story_", "", base))
    return "otros", f"ipadecp_{base}"


def fuentes():
    out = []
    for root, dirs, files in os.walk(BR):
        r = os.path.relpath(root, BR)
        if r.startswith(("09 BRANDBOOK", "10 EDITABLES", "11 GOOGLE FLOW", "12 CERTIFICADOS")) or "DEL KIT ORIGINAL" in r:
            continue
        for f in files:
            if f.lower().endswith((".png", ".jpg")):
                out.append(os.path.join(root, f))
    for root, _, files in os.walk(CERT):
        for f in files:
            if f.lower().endswith(".png"):
                out.append(os.path.join(root, f))
    return sorted(out)


def plan():
    vistos, filas = defaultdict(int), []
    for p in fuentes():
        cat, n = nombre(p)
        n = re.sub(r"_+", "_", n).strip("_")
        vistos[n] += 1
        if vistos[n] > 1:
            n = f"{n}_{vistos[n]}"
        filas.append((cat, n, p))
    return filas


if __name__ == "__main__":
    filas = plan()
    if "--ver" in sys.argv:
        for cat, n, p in filas:
            print(f"{cat:12s} {n:60s} <- {os.path.relpath(p, BR) if p.startswith(BR) else os.path.basename(p)}")
        print(len(filas), "imágenes ·", sum(1 for c, n, p in filas if re.search(r"_\d$", n)), "con sufijo por choque")
        sys.exit()
    if os.path.isdir(FLOW):
        shutil.rmtree(FLOW)
    for cat, n, p in filas:
        d = os.path.join(FLOW, cat)
        os.makedirs(d, exist_ok=True)
        im = Image.open(p)
        im.load()
        if max(im.size) > MAXL:
            im.thumbnail((MAXL, MAXL), Image.LANCZOS)
        meta = PngImagePlugin.PngInfo()
        meta.add_text("Title", n)
        meta.add_text("Description", f"IPADECP · {n.replace('_', ' ')}")
        meta.add_text("Author", "IPADECP")
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGBA")
        im.save(os.path.join(d, n + ".png"), pnginfo=meta, optimize=True)
    # índice
    por = defaultdict(list)
    for cat, n, p in filas:
        por[cat].append(n)
    L = ["# Nombres para Google Flow", "",
         "Cada imagen se llama igual que su archivo. Súbela a Flow y llámala con @ seguido del nombre.",
         "Todos siguen la regla `tipo_ipadecp_variante`: escribe `@logo_ipadecp` y Flow te sugiere las variantes.", "",
         "Atajos más usados:", "",
         "| Quiero | Escribe |", "|---|---|",
         "| El logo a color | `@logo_ipadecp_color` |", "| El logo blanco | `@logo_ipadecp_blanco` |",
         "| El logo blanco sobre navy | `@logo_ipadecp_blanco_fondo_navy` |", "| El isotipo a color | `@isotipo_ipadecp_color` |",
         "| La paleta | `@paleta_ipadecp` |", "| La hoja de marca | `@hoja_de_marca_ipadecp` |",
         "| Tipografía de títulos | `@tipografia_ipadecp_hanken_grotesk` |", "| Tipografía de texto | `@tipografia_ipadecp_inter` |",
         "| El sello rojo | `@sello_ipadecp_verificable_rojo` |", "| Un certificado | `@certificado_ipadecp_panel_lateral_navy` |", ""]
    for cat in sorted(por):
        L += [f"## {cat} ({len(por[cat])})", ""] + [f"- `@{n}`" for n in sorted(por[cat])] + [""]
    open(os.path.join(BR, "NOMBRES-PARA-GOOGLE-FLOW.md"), "w", encoding="utf-8").write("\n".join(L))
    print("listo:", len(filas))
