# branding/

Sistema de marca de IPADECP. Es la fuente única de verdad: si un color, una
tipografía o una palabra no está aquí, no es de la marca.

---

## Empieza por aquí

| Si vas a... | Abre |
|---|---|
| Ver la marca de un vistazo | **`moodboard.html`** (ábrelo en el navegador) |
| Darle contexto de marca a un agente o skill | **`BRAND.md`** |
| Programar en el proyecto | `sistema/tokens.css` |
| Diseñar en Figma, Canva o Illustrator | `sistema/tokens.json` + `logotipo/` |
| Poner una foto de perfil en redes | `logotipo/perfil-redes/` |
| Ver la paleta o las tipografías de un vistazo | `laminas/` |
| Escribir un texto | `identidad/vocabulario.md` |
| Colocar el logo | `sistema/logo-uso.md` |

---

## Qué hay

```
branding/
├── README.md                          este archivo
├── moodboard.html                     la marca en una página, autocontenida
├── BRAND.md                           ★ contexto operativo para agentes
├── identidad/
│   ├── mision-vision-valores.md       quiénes somos y qué defendemos
│   ├── posicionamiento.md             a quién le hablamos y contra qué competimos
│   └── vocabulario.md                 voz, tono, léxico oficial, palabras prohibidas
├── sistema/
│   ├── tokens.css                     ★ colores, radios y sombras para el proyecto
│   ├── tokens.json                    los mismos valores para herramientas de diseño
│   ├── color.md                       por qué cada color, con auditoría de contraste
│   ├── tipografia.md                  las dos familias, la escala, qué se retira
│   └── logo-uso.md                    fondos, aire, tamaños, archivos
├── laminas/
│   ├── paleta-ipadecp.png             la paleta completa en una imagen
│   └── tipografia-ipadecp.png         las dos familias y la escala en una imagen
└── logotipo/
    ├── LEEME.md                       qué archivo usar en cada caso
    ├── vectorial/                     vector REAL de una tinta + contenedores a color
    ├── sin-fondo/                     PNG transparentes, de 400 a 2048 px
    ├── con-fondo/                     cuadrados 1080x1080, logo a tamaño normal
    ├── perfil-redes/                  cuadrados 1080x1080, logo más chico, a prueba de recorte circular
    └── web/                           optimizados para el sitio (9 a 61 KB)
```

---

## Las siete decisiones

1. **El navy `#10284d` sigue siendo el primario.** Es correcto para el sector y
   ya está en todas partes.
2. **El rojo del logotipo `#c6111a` entra al sistema**, reservado a certificación
   y verificación. Era la pieza que faltaba para que el logo y la web se
   parecieran.
3. **Hanken Grotesk + Inter se quedan. Geist se retira** porque se descarga y no
   se ve en ninguna parte.
4. **Formas menos circulares: la píldora salió del sistema.** La escala es
   8 / 10 / 16 por rol. El círculo queda solo para avatares y puntos de estado.
5. **Los degradados entran como propiedad de la marca**, no como efecto: el libro
   del logotipo ya es un degradado de cian a azul. Siempre a 135 grados, y cada
   uno con su parada más clara medida contra 4.5:1.
6. **El logotipo a color solo va sobre fondo claro.** Sobre navy va la versión
   de una tinta en blanco.
7. **`--gris` pasa de `#6b7a8d` a `#5a6878`** porque el anterior reprobaba WCAG
   AA en el color con el que está escrito todo el texto secundario del sitio.

---

## Cómo usarlo con agentes

Para que un agente escriba o diseñe con la marca puesta, cárgale `BRAND.md`.
Está escrito para eso: es el resumen operativo, y cada sección apunta al
documento largo si necesita el detalle.

Para trabajos específicos conviene sumar el documento que corresponda:

| Trabajo | Contexto que hay que darle |
|---|---|
| Copy de web, correo o anuncio | `BRAND.md` + `identidad/vocabulario.md` |
| Pieza gráfica o post | `BRAND.md` + `sistema/tokens.json` + `sistema/logo-uso.md` |
| Interfaz o componente | `BRAND.md` + `sistema/tokens.css` + `sistema/color.md` |
| Landing o sección nueva | `BRAND.md` completo + `identidad/posicionamiento.md` |

---

## Ya aplicado en el código

La marca ya está en el producto. Lo que se cambió en `src/`:

1. **`src/styles/tokens.css`** es una copia de `sistema/tokens.css` y se importa
   primero en `src/app/layout.tsx`. El resto de las hojas consume esas
   variables en vez de repetir hex.
2. **`--gris` corregido a `#5a6878`**, que arregla el contraste de todo el texto
   secundario del sitio.
3. **El logo del header pasó de 1,4 MB a 9 KB** (`logo-ipadecp-96.webp` con
   `srcSet` a 192 px en retina). El rótulo de pedido del panel usa el de 61 KB.
4. **Geist retirado.** Hanken Grotesk e Inter pasaron a `next/font/google` con
   eje variable: se auto-alojan, ya no hay `<link>` a Google Fonts para ellas y
   no hay salto de maquetación al cargar.
5. **Variantes `-texto` de los estados** agregadas, y el borde de input pasó a
   `--ipd-borde-campo #768495` (3.55:1): el anterior daba 1.24:1 y WCAG pide
   3:1 para controles. Las estrellas de valoración pasaron al oro de glifo.
6. **Formas y degradados llevados al sitio:** la píldora salió (chips a 8 px,
   botones y campos a 10 px) y los botones usan los degradados del sistema. El
   único cambio visible en todos los CTA es que el botón primario pasó del
   degradado celeste al navy de marca; se revierte con una línea, marcada en
   `src/styles/publico.css`.

Con esto la base de marca ya está en el producto, que era la condición para
entrar al rediseño de la web pública.

> Antes de tocar cualquier cosa de Next.js en este proyecto, leer la guía
> correspondiente en `node_modules/next/dist/docs/`. Es Next 16 y la API puede
> no ser la que uno recuerda. Lo pide `AGENTS.md` en la raíz.
