# Logotipo IPADECP

Los archivos se llaman por lo que son. `logotipo-blanco-sobre-navy` es el
logotipo en blanco sobre fondo navy. No hay que abrirlos para saber cuál es.

---

## ¿Está vectorizado? Sí a medias, y la mitad que importa

Esta es la respuesta honesta, porque cambia lo que se puede hacer con cada
archivo.

### La versión de UNA TINTA sí es vector de verdad

`vectorial/logotipo-una-tinta.svg` y sus variantes de color son **trazados
vectoriales reales**, no una imagen metida dentro de un SVG.

Se reconstruyeron del canal alfa del archivo original: el contorno se trazó con
*marching squares* interpolado (que da precisión de subpíxel, no escalera de
píxeles) y después se simplificó con Douglas-Peucker. Salieron **161 contornos
cerrados y unos 2 800 puntos**, con `fill-rule="evenodd"` para que los huecos
(las contraformas de las letras, la rejilla del globo) se resuelvan solos.

- **Fidelidad medida contra el original: 3.9 % de diferencia**, y casi toda es
  el antialiasing de un borde de 1 px sobre una silueta con muchísimo
  perímetro. Se verificó rasterizando el SVG y comparando píxel a píxel.
- **Pesa 29 KB** y escala a cualquier tamaño sin pixelar. Sirve para
  gigantografía, serigrafía, vinilo, bordado y corte láser.
- Usa `fill="currentColor"` en `logotipo-una-tinta.svg`, así que se puede pintar
  de cualquier color desde CSS o desde el programa de diseño.

### La versión A COLOR no se puede vectorizar, y no se debe

`vectorial/logotipo-color.svg` e `isotipo-color.svg` siguen siendo
**contenedores**: un mapa de bits dentro de un SVG. Sirven para colocar el logo
a cualquier tamaño sin fondo blanco ni recortes, pero al ampliarlos mucho
pixelan igual que un PNG.

El motivo es real y no es pereza: el globo y el libro tienen **degradados
continuos** (azul a cian). Un trazado vectorial automático los convertiría en
bandas planas de color, y el logo dejaría de verse como se ve. Para eso hace
falta el archivo original de quien lo diseñó.

> **Lo único que sigue faltando:** el vectorial a color original (.ai, .eps o
> .cdr). Con la versión de una tinta ya se cubre casi todo el uso impreso
> grande, porque en impresión grande el logo suele ir a una tinta de todos
> modos.

---

## Qué carpeta usar

| Necesitas | Carpeta |
|---|---|
| Foto de perfil de WhatsApp, Instagram, Facebook o LinkedIn | **`perfil-redes/`** |
| Poner el logo sobre tu propio fondo o diseño | `sin-fondo/` |
| Una imagen cuadrada ya lista para un post | `con-fondo/` |
| Imprimir grande, cortar vinilo, bordar | `vectorial/logotipo-una-tinta.svg` |
| Ponerlo en la web | `web/` |

---

## `perfil-redes/` — por qué el logo está más chico

WhatsApp, Instagram y LinkedIn **recortan la foto de perfil en círculo**. Si el
logo llena el cuadrado, las esquinas se pierden y el arco rojo queda cortado.

Estos archivos tienen el logo reducido a propósito, con el tamaño calculado:
se toma un círculo seguro del **82 % del lado** (886 px sobre un lienzo de
1080) y se ajusta el logo para que su **diagonal** entre completa ahí. Da
**669 px de ancho para el logotipo** y **722 px para el isotipo**, contra los
780 y 830 de las versiones normales.

Traducido: se ve más fondo alrededor y el logo no toca el filo del círculo en
ninguna red.

**El recomendado para foto de perfil es
`perfil-logotipo-blanco-sobre-navy.png`.**

También está `perfil-logotipo-color-sin-fondo.png` y su versión en blanco, con
el mismo encuadre seguro pero transparentes, por si quieres poner tu propio
fondo.

---

## La regla que más se rompe

**El logotipo a color va solo sobre fondo claro.** La palabra IPADECP y el
birrete son negros: sobre navy desaparecen. Sobre cualquier fondo oscuro va la
versión blanca, que además se ve mejor.

| Fondo | Archivo |
|---|---|
| Blanco, hueso `#f4f7fa`, navy lavado `#e8eef6` | `logotipo-color-*` |
| Navy `#10284d`, celeste `#6cb3d3`, degradado de marca, foto | `logotipo-blanco-*` |

Otras reglas: aire alrededor igual a la altura de la "I" de IPADECP; mínimo
120 px de ancho en pantalla para el logotipo completo y 40 px para el isotipo;
no estirar, no rotar, no recolorear el de color, no ponerle sombra ni contorno.

El detalle completo está en `../sistema/logo-uso.md`.

---

## Todos los archivos

```
vectorial/
  logotipo-una-tinta.svg        ★ VECTOR REAL, se pinta con currentColor
  logotipo-blanco.svg             vector real, blanco
  logotipo-navy.svg               vector real, navy #10284d
  logotipo-negro.svg              vector real, negro
  logotipo-color.svg              contenedor de mapa de bits (a color)
  isotipo-color.svg               contenedor de mapa de bits

sin-fondo/                      PNG transparentes
  logotipo-color-sin-fondo-400 / -800 / -1080 / -2048
  logotipo-blanco-sin-fondo-800 / -2048
  logotipo-navy-sin-fondo-800 / -2048
  isotipo-color-sin-fondo-512 / -1080
  isotipo-blanco-sin-fondo-512 / -1080

con-fondo/                      1080 x 1080, logo a tamaño normal
  logotipo-color-sobre-blanco
  logotipo-color-sobre-hueso
  logotipo-blanco-sobre-navy
  logotipo-blanco-sobre-celeste
  logotipo-blanco-sobre-degradado
  isotipo-color-sobre-blanco
  isotipo-blanco-sobre-navy

perfil-redes/                   1080 x 1080, logo más chico, a prueba de recorte circular
  perfil-logotipo-blanco-sobre-navy        ★ el recomendado
  perfil-logotipo-blanco-sobre-degradado
  perfil-logotipo-blanco-sobre-celeste
  perfil-logotipo-color-sobre-blanco
  perfil-logotipo-color-sobre-hueso
  perfil-logotipo-color-sin-fondo
  perfil-logotipo-blanco-sin-fondo
  perfil-isotipo-blanco-sobre-navy
  perfil-isotipo-color-sobre-blanco

web/                            optimizados para el sitio, de 9 a 61 KB
logotipo-maestro-original.webp  el archivo de origen, 10322 x 8933 px
```
