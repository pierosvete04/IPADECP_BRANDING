# IPADECP — Uso del logotipo

El logotipo **no se rediseña**. Este documento define cómo se usa el que hay y
qué archivo va en cada situación.

---

## 1. Qué está vectorizado y qué no

Hay que decirlo claro porque cambia lo que se puede hacer con cada archivo.

### La versión de una tinta SÍ es vector real

`logotipo/vectorial/logotipo-una-tinta.svg` es un **trazado vectorial de
verdad**, no una imagen metida dentro de un SVG.

Se reconstruyó del canal alfa del archivo original con *marching squares*
interpolado (precisión de subpíxel, no escalera de píxeles) y simplificación
Douglas-Peucker: **161 contornos cerrados, unos 2 800 puntos, 29 KB**, con
`fill-rule="evenodd"` para que los huecos (las contraformas de las letras, la
rejilla del globo) se resuelvan solos.

**Fidelidad medida: 3.9 % de diferencia** contra el original, y casi toda es el
antialiasing de un borde de 1 px sobre una silueta con muchísimo perímetro. Se
verificó rasterizando el SVG y comparando píxel a píxel contra la máscara
original.

Escala sin pixelar a cualquier tamaño: gigantografía, serigrafía, vinilo,
bordado, corte láser. Usa `fill="currentColor"`, así que se pinta de cualquier
color desde CSS o desde el programa de diseño. También hay variantes ya
pintadas: `logotipo-blanco.svg`, `logotipo-navy.svg`, `logotipo-negro.svg`.

### La versión a color NO se puede vectorizar

`vectorial/logotipo-color.svg` e `isotipo-color.svg` son **contenedores**: un
mapa de bits dentro de un SVG. Colocan el logo a cualquier tamaño sin fondo
blanco ni recortes, pero al ampliarlos mucho pixelan igual que un PNG.

El motivo es real y no es pereza: el globo y el libro tienen **degradados
continuos** de azul a cian. Un trazado vectorial automático los convertiría en
bandas planas de color, y el logo dejaría de verse como se ve.

### El origen

El único archivo maestro es `logotipo/logotipo-maestro-original.webp`: un mapa
de bits de **10 322 × 8 933 px** con fondo transparente. No hay `.ai`, `.eps` ni
`.cdr` en el proyecto. El fondo transparente **ya venía** en el archivo: lo que
se ve negro es tinta de verdad (la palabra IPADECP, el birrete y las líneas del
globo), no falta de recorte.

> **Lo que sigue faltando:** el vectorial a color original, que hay que pedirle
> a quien diseñó el logo. Con la versión de una tinta ya se cubre casi todo el
> uso impreso grande, porque ahí el logo suele ir a una tinta de todos modos.

---

## 2. Los colores reales del logotipo

Muestreados del archivo, no aproximados:

| | Hex | Dónde está |
|---|---|---|
| Rojo | `#c6111a` | arco exterior, filo del libro, ornamentos |
| Azul | `#0130db` | continentes del globo |
| Cian | `#00e4ff` | libro abierto |
| Negro | `#000000` | palabra IPADECP, birrete, texto circular, meridianos |

El negro es el que manda las reglas de fondo del punto 4. El degradado del
libro (cian a azul) es el origen del sistema de degradados de la marca, ver
`./color.md` §7.

---

## 3. Las tres versiones

| Versión | Qué incluye | Cuándo |
|---|---|---|
| **Completa** | Emblema + palabra IPADECP | Por defecto. Web, documentos, certificados, papelería |
| **Isotipo** | Solo el emblema, sin la palabra | Cuando "IPADECP" ya está escrito al lado, o en espacios cuadrados chicos (avatar, favicon, sello) |
| **Una tinta** | Silueta completa en un solo color | Obligatoria sobre navy, foto o cualquier fondo oscuro. También es la que sirve para impresión grande |

---

## 4. Fondos: la regla que más se rompe

**El logotipo a color solo va sobre fondo claro.**

Sobre navy `#10284d`, el birrete y la palabra IPADECP son negros sobre azul
oscuro y prácticamente desaparecen. Se comprobó al generar las piezas. Sobre
fondo oscuro va **siempre** la versión blanca, que además se ve mejor: el
emblema completo en una sola tinta gana fuerza.

| Fondo | Archivo |
|---|---|
| Blanco `#ffffff` | color |
| Fondo suave `#f4f7fa` | color |
| Navy lavado `#e8eef6` | color |
| **Navy `#10284d` / `#0a1c38` / `#06142b`** | **blanco** |
| **Degradado de marca** | **blanco** |
| Foto | blanco, y solo sobre una zona oscura y sin detalle |
| Celeste `#6cb3d3` | blanco, o color si el celeste es solo un filo |

---

## 5. Aire y tamaño mínimo

**Aire:** un margen libre alrededor igual a la **altura de la letra "I" de
IPADECP**. Nada entra ahí: ni texto, ni borde, ni el filo de una foto.

**Tamaños mínimos** (por debajo el texto circular se convierte en una mancha
gris):

| Uso | Mínimo |
|---|---|
| Logotipo completo, pantalla | 120 px de ancho |
| Logotipo completo, impreso | 30 mm de ancho |
| Isotipo, pantalla | 40 px |
| Isotipo, favicon | 32 px (a 16 px se usa el `icon.png` existente) |

En el header del sitio el logo va a 34 px de alto: ahí funciona porque va
**acompañado de la palabra IPADECP escrita al lado**, no solo.

---

## 6. Lo que no se hace

- No estirar ni deformar. Escalar siempre proporcional.
- No rotar ni inclinar.
- No recolorear el logo a color. Recolorear solo se puede sobre la versión de
  una tinta, que para eso usa `currentColor`.
- No ponerle sombra, brillo, contorno ni borde.
- No encerrarlo en una caja de color para "salvarlo" de un fondo difícil: si el
  fondo es difícil, va la versión de una tinta.
- No reescribir "IPADECP" con otra tipografía al lado del emblema.
- No usar solo el globo, solo el libro o solo el birrete como marca suelta.
- No llenar el cuadrado con el logo en una foto de perfil: las redes recortan en
  círculo. Para eso está `perfil-redes/` (ver §7).

---

## 7. Los archivos

Todos en `branding/logotipo/`, con nombres que se entienden solos:
`logotipo-blanco-sobre-navy` es exactamente eso. La lista completa y la
explicación de cada carpeta están en `branding/logotipo/LEEME.md`.

| Carpeta | Para qué |
|---|---|
| `vectorial/` | Vector real de una tinta, más los contenedores a color |
| `sin-fondo/` | PNG transparentes, de 400 a 2048 px |
| `con-fondo/` | Cuadrados 1080 × 1080 con el logo a tamaño normal |
| `perfil-redes/` | Cuadrados 1080 × 1080 con el logo **más chico**, calculado para el recorte circular de las redes |
| `web/` | Optimizados para el sitio, de 9 a 61 KB |

### Por qué existe `perfil-redes/`

WhatsApp, Instagram y LinkedIn recortan la foto de perfil **en círculo**. Si el
logo llena el cuadrado, las esquinas se pierden y el arco rojo queda cortado.

En esa carpeta el logo va reducido a propósito, con el tamaño calculado: se toma
un círculo seguro del **82 % del lado** (886 px sobre un lienzo de 1080) y se
ajusta el logo para que su **diagonal** entre completa ahí. Da **669 px de ancho
para el logotipo** y **722 px para el isotipo**, contra los 780 y 830 de las
versiones normales.

El recomendado para foto de perfil es
`perfil-redes/perfil-logotipo-blanco-sobre-navy.png`.

---

## 8. Cómo se sirve en el sitio (ya resuelto)

`src/Componentes/brand/Logo.tsx` servía `public/logo-ipadecp.webp`: **1,4 MB**
para dibujarlo a 34 px de alto, en cada visita a cada página. Era de lejos el
archivo más pesado del sitio.

Ya está corregido: ahora sirve `logo-ipadecp-96.webp` con un `srcSet` que sube
al de 192 px en pantalla retina. Son **9 KB en vez de 1,4 MB**, alrededor de
99 % menos, y pega directo en el LCP de la portada. El rótulo de pedido del
panel pasó al de 384 px (61 KB), que a 7 mm impreso sobra.

El maestro se queda en `branding/logotipo/` como archivo de origen.
