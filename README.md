# Branding IPADECP

Instituto Peruano Americano de Desarrollo y Capacitación Profesional.
Abre **`index.html`** (o `09 BRANDBOOK/brandbook-ipadecp.html`): es el manual de marca con menú arriba, una página por tema, y cada pieza se ve y se descarga ahí.

```
BRANDING/
├── 01 LOGOS/
│   ├── LOGO OFICIAL/             logotipo completo (emblema + palabra IPADECP)
│   │   ├── SVG/                  9 versiones 100 % vectoriales (el globo y el libro conservan sus degradados)
│   │   ├── PNG/                  las mismas en 4000 px, fondo transparente
│   │   ├── CON FONDO 1x1/SVG|PNG/  cada versión sobre los fondos que le corresponden (3000 px)
│   │   └── 16x9/SVG|PNG/         cada versión en 16:9 (3840 × 2160), sin fondo y con fondos
│   └── ISOTIPO/                  el emblema solo, mismas versiones y fondos 1:1
├── 02 SELLOS Y VERIFICACION/     sello verificable (rojo), sello de logro (oro) e insignia «Verifica este certificado»
├── 03 PAPELERIA/                 certificado A4 (plantilla), hoja membretada A4, tarjeta 85×55 (frente y dorso),
│                                 sobre DL del certificado físico, firma de correo. SVG en milímetros, PNG a 300 ppp
├── 04 ASSETS/
│   ├── ICONOS/                   40 íconos (curso, certificado y salud) · lineal (navy, celeste, blanco, negro, gris) y círculo (navy, celeste, lavado, degradado)
│   ├── ELEMENTOS GRAFICOS/       globo lineal, filete del logo, barra de avance
│   ├── PATRONES/                 malla de globo, diagonal 135°, puntos, QR · sobre navy, hueso, blanco y transparente
│   ├── FONDOS/                   16x9, story 9x16, post 4x5, cuadrado 1x1
│   ├── QR/                       web y WhatsApp, en navy, negro y blanco, más tarjetas
│   └── FOTOGRAFIA/               las fotos de la portada web
├── 05 MOCKUPS/                   certificado y sobre, papelería, publicaciones, sellos (vectoriales)
├── 06 PALETA DE COLORES/         lámina, hoja de marca, .ase (Illustrator), .gpl (Inkscape/GIMP), .css y .json
├── 07 TIPOGRAFIAS/
│   ├── INSTALAR/                 Hanken Grotesk e Inter (variables) + ESTATICAS (una por peso) · licencia OFL
│   └── MUESTRAS/                 una lámina por familia y la escala
├── 08 REDES SOCIALES/            perfil a prueba de recorte circular, portadas (Facebook, LinkedIn, YouTube, WhatsApp),
│                                 historias destacadas, posts 4:5, stories, portada web
├── 09 BRANDBOOK/                 brandbook-ipadecp.html · web/ = miniaturas
├── 10 EDITABLES Y DOCUMENTOS/    logotipo maestro original (10322 px), documentos de marca (BRAND.md, identidad, sistema, ui),
                                  kit de logo anterior y el generador en Python que produce todo esto
├── 11 GOOGLE FLOW/              solo PNG (máx. 2048 px) con nombres para llamar con @ en Flow · lista en NOMBRES-PARA-GOOGLE-FLOW.md
└── 12 CERTIFICADOS - PROPUESTAS/  6 modelos A4 horizontal · SVG EDITABLE (texto vivo, instala antes las fuentes de 07/INSTALAR/ESTATICAS), SVG EN CURVAS, PNG 300 ppp
```

## El logo: qué cambió

El kit anterior decía que la versión a color «no se puede vectorizar». Ahora sí está vectorizada:
el maestro se separó en sus capas (rojo, negro y azules) y cada pieza del globo y del libro lleva
su propio degradado medido del original. Diferencia media contra el maestro: 1.6 sobre 255.

| Versión | Uso |
|---|---|
| color | por defecto, solo sobre fondo claro |
| color-plano | tintas planas (rojo, azul #0130db, cian #00e4ff, negro): serigrafía, bordado, vinilo |
| escala-grises | impresión en grises |
| bn-positivo / bn-negativo | una pieza en blanco y negro sobre claro u oscuro |
| una-tinta-navy / negro | silueta en un color, sobre claro |
| una-tinta-blanco | **obligatoria** sobre navy, degradados y foto |
| una-tinta-rojo | solo en piezas de certificación (sello, certificado) |

Los SVG agrupan el logo en `libro-y-globo`, `arco-y-filetes` y `palabra-birrete-y-texto`.

## Reglas

1. **El logo no se rediseña ni se genera con IA.** Se usan los archivos de `01 LOGOS/`.
2. **El color a color solo va sobre fondo claro.** Sobre oscuro, la versión blanca.
3. **El rojo es solo de certificación y verificación.** Nunca botones generales, enlaces ni titulares.
4. **La certificación directa no se menciona** en web, anuncios ni piezas. El instituto no certifica experiencia previa.
5. **Nada de afirmar acreditación** (avalado, acreditado, reconocido, MINSA, SUNEDU…). Lo que sí se dice: el certificado se comprueba en segundos.
6. Textos entre `[corchetes]` son marcadores: se reemplazan antes de usar. Ninguna cifra sin confirmar.
7. Esquinas 8 / 10 / 16 px; la píldora no es de la marca. Degradados siempre a 135°.

## Volver a generar

Todo sale de `10 EDITABLES Y DOCUMENTOS/GENERADOR (python)/`. Requiere Python con
`pillow numpy opencv-python-headless resvg-py fonttools uharfbuzz qrcode`.
Orden: `build_logos.py`, `build_assets.py`, `build_papeleria.py`, `build_sistema.py`,
`build_redes.py`, `build_mockups.py`, `build_brandbook.py`.
