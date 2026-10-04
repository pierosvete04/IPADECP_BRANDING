# Portada: las dos piezas del banner

## Las medidas, y por qué son esas

El banner ocupa **lo que mide la pantalla**, no una franja. Por eso son dos
piezas distintas y no una sola reencuadrada: una foto apaisada recortada a
vertical pierde la mitad del sujeto.

| Pieza | Medida | Proporción |
|---|---|---|
| Computadora | **1920 × 1080 px** | 16:9 |
| Celular | **1080 × 1920 px** | 9:16 |

El componente sirve la que toca con `<picture>` y un `media="(max-width: 767px)"`,
así que el celular nunca descarga la de escritorio. En el marco hay un tope de
`max-height: calc(100dvh - alto del header)` para que en un monitor muy ancho el
banner no tape lo que viene debajo.

## Cómo se hicieron

Dos pasos, y el orden importa.

### 1. La fotografía, con Gemini

`generar-fotos.js` pide las fotos a `gemini-3-pro-image` de Google AI Studio.
Necesita la clave en la variable de entorno `GEMINI_API_KEY`.

```bash
GEMINI_API_KEY=... node branding/portada/generar-fotos.js
```

Las fotos se piden **sin nada de texto**, a propósito. Ver el punto 2.

> **Lo que costó descubrir:** al pedir una foto 9:16 de "un pasillo de hospital",
> el modelo devolvió dos veces la escena **girada 90 grados** dentro del lienzo
> vertical. La persona salía acostada. No es un problema de metadatos EXIF: la
> imagen se genera así.
>
> **La solución:** para vertical hay que pedir un encuadre que sea naturalmente
> vertical, un **retrato cerrado de medio cuerpo con el fondo desenfocado**. En
> cuanto se le quitó el pasillo y las líneas de fuga, salió derecha a la primera.
> Para horizontal, el pasillo funciona perfecto.

También conviene pedir explícitamente dónde va el espacio libre: en escritorio
"la persona a la derecha y toda la mitad izquierda despejada", en celular "la
persona arriba y la mitad inferior despejada". Ahí es donde entra el texto.

### 2. El texto, con Chrome

`componer.js` monta la pieza final: la fotografía, un velo en degradado y el
texto de la campaña escrito en **HTML con Hanken Grotesk e Inter reales**, y lo
rasteriza con Chrome headless.

```bash
node branding/portada/componer.js
```

**El texto no lo escribe la IA a propósito.** Un generador de imágenes comete
faltas de ortografía, parte mal las palabras y no respeta la tipografía de la
marca. Compuesto en HTML sale exacto, con el degradado del botón correcto y su
filo superior, y se cambia editando una constante.

Para una campaña nueva se edita el objeto `CAMPANA` al inicio de `componer.js`:

```js
const CAMPANA = {
  etiqueta: 'NUEVA CONVOCATORIA',
  titular: 'Certifícate en cuidados intensivos',
  apoyo: '6 módulos, 100 % virtual, con certificado verificable por QR.',
  boton: 'Ver el curso',
};
```

## Dónde queda cada cosa

```
branding/portada/
  fotos/                              las fotografías originales de Gemini
  banner-escritorio-1920x1080.png     la pieza compuesta, full
  banner-movil-1080x1920.png          la pieza compuesta, full
  generar-fotos.js                    paso 1
  componer.js                         paso 2

public/img/portada/                   las versiones que sirve la web, en webp
  banner-escritorio.webp   94 KB
  banner-movil.webp        98 KB
  hero.webp                96 KB
  certificado.webp         74 KB
  camino-estudiar.webp     35 KB
  camino-certificar.webp   40 KB
```

Las seis suman **430 KB**. El velo del banner es un degradado CSS rasterizado,
no una capa de imagen, así que comprime muy bien.

## Para publicar la campaña

Las piezas **no se publican solas**: el banner de la home sale de la tabla de
banners y se sube desde el panel. Entra a la sección de banners, sube
`banner-escritorio-1920x1080.png` como pieza de computadora y
`banner-movil-1080x1920.png` como pieza de celular, escribe el `alt` y publícalo.

Mientras no haya ningún banner publicado, la home simplemente no muestra esa
sección y arranca en el héroe de texto. Es el comportamiento correcto y no hay
que tocar nada.

## Antes de subir cualquier banner

- [ ] Las dos piezas, computadora y celular.
- [ ] El texto dentro de la imagen no baja de 32 px en escritorio ni de 40 px en
      celular.
- [ ] El `alt` dice de qué es la campaña, no "banner".
- [ ] Cero rayas largas.
- [ ] Ninguna cifra sin confirmar por el instituto.
- [ ] Nada que insinúe que el certificado está avalado o acreditado.

---

## Ya está publicado

El banner de esta campaña se subió a Supabase el 2026-09-02 y está activo.

| | |
|---|---|
| Bucket | `cursos-imagenes` |
| Rutas | `banners/desktop-1788476673442.webp` y `banners/mobile-1788476673442.webp` |
| Fila | `banners` id **3**, activo, orden 1, enlace `/cursos` |

Verificado en el navegador: en escritorio sirve la pieza de 1920×1080 a 1425×802
(ratio 1.778) y en celular la de 1080×1920 a 375×667 (ratio 0.563). Las dos a
sangre y sin errores de consola.

### Un ajuste que hubo que hacer en el componente

El banner venía envuelto en `.ipd-contenedor`, que limita el ancho a 1240 px.
Eso es lo correcto para el resto de la home, pero dejaba **dos franjas grises a
los lados** de una pieza pensada para ocupar la pantalla entera. Se reemplazó
por `.ipd-banner-interior`, que no limita el ancho. El resto de secciones sigue
usando `.ipd-contenedor` sin cambios.

### Para cambiar la campaña

Desde el panel de banners, o volviendo a correr el compositor y subiendo las dos
piezas nuevas. La fila 3 se puede editar en vez de crear otra: así el orden y el
enlace se mantienen.
