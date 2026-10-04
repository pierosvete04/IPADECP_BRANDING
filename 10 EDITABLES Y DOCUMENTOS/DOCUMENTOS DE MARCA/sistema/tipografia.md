# IPADECP — Tipografía

## 1. La decisión

**Dos familias. Ninguna tercera.**

| Rol | Familia | Pesos | Dónde |
|---|---|---|---|
| Títulos y botones | **Hanken Grotesk** | 400, 600, 700, 800 | h1–h4, botones, nombre de la marca, cifras destacadas |
| Cuerpo e interfaz | **Inter** | 400, 500, 600 | párrafos, formularios, tablas, navegación, etiquetas |
| Códigos | pila del sistema (`ui-monospace`) | — | código corto, número de registro, DNI, código de 6 dígitos |

Las dos ya están en el proyecto y funcionan. **La recomendación es quedarse con
ellas**, no cambiarlas: Hanken Grotesk es una grotesca humanista con la "a" y la
"g" abiertas, se lee cálida sin perder formalidad, y a peso 800 aguanta un
titular grande sin verse agresiva. Inter es la fuente de interfaz mejor resuelta
que existe para formularios y tablas densas, que es justo lo que el aula y el
panel son.

### Qué hay que quitar

**Geist se retira.** Se carga con `next/font` en `src/app/layout.tsx` y define
`--font-sans`, pero `tema-stitch.css` pisa `body { font-family: Inter }`, así que
**Geist no se ve en ninguna parte del sitio**. Es una descarga de fuente entera
por cada visita, a cambio de nada. Solo hay 2 usos de `font-sans` en JSX que hay
que revisar al quitarla.

### La serif del logotipo no entra a la interfaz

La palabra "IPADECP" del logotipo está en una serif de alto contraste tipo
Times. **Esa serif vive únicamente dentro del logotipo.** No se reproduce en
titulares, ni en el certificado, ni en piezas gráficas. Escribir "IPADECP" en
serif fuera del logo compite con el logo y hace ver dos marcas.

---

## 2. Escala tipográfica

Fluida con `clamp()`, de móvil a escritorio, sin saltos por breakpoint.

| Nivel | Tamaño | Peso | Interletrado | Interlínea |
|---|---|---|---|---|
| Display (héroe) | `clamp(2.25rem, 5vw, 3.75rem)` | 800 | `-0.02em` | 1.08 |
| H1 | `clamp(1.875rem, 3.5vw, 2.75rem)` | 700 | `-0.015em` | 1.15 |
| H2 | `clamp(1.5rem, 2.5vw, 2rem)` | 700 | `-0.01em` | 1.2 |
| H3 | `1.25rem` | 600 | `0` | 1.3 |
| Cuerpo grande | `1.0625rem` | 400 | `0` | 1.6 |
| Cuerpo | `1rem` | 400 | `0` | 1.6 |
| Cuerpo chico | `0.875rem` | 400 | `0` | 1.55 |
| Etiqueta | `0.8125rem` | 600 | `0.01em` | 1.4 |
| Botón | `0.95rem` | 700 | `0` | 1 |
| Código | `0.9375rem` | 500 | `0.06em` | 1.4 |

**Reglas:**
- Párrafos a `max-width: 65ch`. Una línea de texto más larga que eso se pierde
  al saltar de renglón.
- El interletrado negativo es solo para 2 rem en adelante. En cuerpo chico
  apretar las letras solo lo hace más difícil de leer.
- Cuerpo nunca por debajo de 15 px. Buena parte de nuestros alumnos lee desde el
  celular después de un turno.
- Códigos (`ABC-123`, número de registro, DNI) van siempre en la pila mono y con
  interletrado abierto: son cifras que la gente **copia y dicta por teléfono**, y
  la mono es la que distingue 0 de O y 1 de l.

---

## 3. Carga de fuentes

Hoy Hanken Grotesk, Inter y Material Symbols se traen con un `<link>` a Google
Fonts en `layout.tsx`. Funciona, pero significa un DNS + conexión + descarga a
un dominio de terceros antes de que se pinte el primer texto.

**Mejora recomendada** (una sola tarea, sin cambio visual): pasar las dos
familias a `next/font/google`, que las auto-aloja en el propio dominio, genera
el `@font-face` con `font-display: swap` y calcula el ajuste de métricas para
que no haya salto de layout al cargar. Es el mismo mecanismo con el que hoy se
carga Geist, así que el patrón ya está en el archivo.

```tsx
import { Hanken_Grotesk, Inter } from 'next/font/google';

const titulo = Hanken_Grotesk({ subsets: ['latin'], weight: ['400','600','700','800'], variable: '--ipd-font-titulo' });
const texto  = Inter({ subsets: ['latin'], weight: ['400','500','600'], variable: '--ipd-font-texto' });
```

> Antes de tocar esto: leer la guía de fuentes en
> `node_modules/next/dist/docs/` — este proyecto usa Next 16 y la API puede no
> ser la que uno recuerda.

**Material Symbols se queda con `<link>`.** Es una fuente de íconos variable y
`next/font` no la maneja bien. El comentario que ya está en `tema-stitch.css`
explica por qué no debe volver a un `@import`: causaba el parpadeo donde se veía
la palabra "home" antes de cargar la tipografía.

---

## 4. Íconos

Hoy conviven **dos sistemas**: Material Symbols Outlined (44 archivos) y
`lucide-react` (27 archivos). No fue una decisión, se fue dando.

**Regla mientras convivan:**

| Zona | Sistema |
|---|---|
| Web pública | **Material Symbols Outlined** — es el lenguaje visual del tema Stitch y es mayoría ahí |
| Panel admin y aula | **lucide-react** — ya está integrado con los componentes shadcn |

Nunca los dos en la misma pantalla: los pesos de trazo no coinciden y se nota.

**Estado final deseable:** consolidar en Material Symbols y sacar `lucide-react`
del bundle. Son 27 archivos, así que es una tarea propia, no un efecto
secundario de este trabajo de marca.

`lucide-react` no se usa para íconos nuevos en la web pública. Si falta un
glifo, se busca en Material Symbols antes de dibujar un SVG a mano — dibujar
íconos a mano es lo que hace que un set se vea desparejo.
