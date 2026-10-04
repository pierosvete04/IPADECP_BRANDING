# IPADECP — Sistema de color

Valores en `./tokens.css` y `./tokens.json`. Este documento explica **por qué**
cada uno está ahí y cuándo se usa.

---

## 1. El problema que este sistema resuelve

Antes de esta estandarización había dos paletas que no se hablaban:

- **El logotipo** es rojo (#c6111a), azul (#0130db), cian (#00e4ff) y negro.
- **El sitio** era navy (#10284d) y celeste (#6cb3d3), sin una gota de rojo.

Por eso el logo se veía pegado encima de la web en vez de pertenecer a ella. Y
además había siete azules casi iguales (`#10284d`, `#0a1c38`, `#001331`,
`#0b6683`, `#6cb3d3`, `#98deff`, `#2f7593`) sin regla que dijera cuál va dónde.

La decisión fue **no repintar el sitio de rojo**. El navy es correcto para el
sector, ya está en todas partes y comunica lo que tiene que comunicar. Lo que
faltaba era darle al rojo del logotipo **un trabajo concreto y acotado**, en vez
de dejarlo fuera del sistema.

---

## 2. Los tres colores de la marca

| | Color | Hex | Trabajo |
|---|---|---|---|
| **Primario** | Navy IPADECP | `#10284d` | Todo lo institucional: encabezados, botón primario, footer, superficies oscuras |
| **Secundario** | Celeste IPADECP | `#6cb3d3` | Aire y apoyo: bordes, íconos, fondos de sección, ilustración |
| **Acento** | Rojo IPADECP | `#c6111a` | Solo certificación y verificación (§3) |
| **Logro** | Oro | `#d4af37` | No es color de marca: es el color de un logro. Estrellas, sello, racha, estados del aula |

Un acento por página, y es el rojo. No se agrega un quinto color.

---

## 3. La regla del rojo

El rojo es el color más distintivo de IPADECP y también el más fácil de arruinar.
Se usa **solo donde la marca dice "esto es un certificado real y se puede
comprobar"**:

**Sí:**
- El sello / marca de agua del certificado en PDF
- La página pública de verificación de certificados (estado "válido")
- El módulo "Verificar certificado" del sitio
- Un ícono de sello junto al número de registro
- La franja del certificado físico

**No:**
- Botones generales de compra ("Llevar este curso" es navy)
- Enlaces del cuerpo de texto
- Encabezados de sección
- Fondos amplios
- Estados de error (para eso está `--ipd-error #d64545`, que es otro rojo, a
  propósito más apagado, para que el sello no se confunda con una falla)

**Regla mecánica:** si en una pantalla el rojo ocupa más del 10 % del área
visible, está mal usado.

---

## 4. Escalas y para qué sirve cada paso

### Navy — primario
```
--ipd-navy-900  #06142b   fondo oscuro profundo (footer, modo oscuro)
--ipd-navy-800  #0a1c38   hover del botón primario
--ipd-navy-700  #10284d ★ PRIMARIO
--ipd-navy-600  #1c3d6b   superficie elevada sobre navy (tarjeta en footer)
--ipd-navy-500  #001331   navy de texto para titulares grandes
--ipd-navy-100  #e8eef6   chip, fondo de sección alterna
--ipd-navy-050  #f4f7fa ★ fondo del sitio
```

### Celeste — secundario
```
--ipd-celeste-800  #0b6683   texto y enlaces sobre claro (6.48:1)
--ipd-celeste-700  #2f7593 ★ botón sólido con texto blanco (5.14:1)
--ipd-celeste-500  #6cb3d3 ★ CELESTE DE MARCA — decorativo
--ipd-celeste-100  #dcf0f8   superficie de chip
--ipd-celeste-050  #f0f9fd   superficie apenas teñida
```

> **La trampa del celeste.** `#6cb3d3` da **2.33:1** sobre blanco. Como texto
> sobre fondo claro es ilegible y reprueba WCAG AA. Sobre navy, en cambio, da
> **6.30:1** y funciona muy bien. Entonces: **celeste-500 es decorativo sobre
> claro y tipográfico sobre oscuro.** Para texto o botón sólido sobre fondo
> claro se usa `celeste-700`.

### Rojo — acento
```
--ipd-rojo-700  #9d0d14   hover y texto (8.40:1)
--ipd-rojo-600  #c6111a ★ ROJO DEL LOGOTIPO (6.01:1 sobre blanco)
--ipd-rojo-050  #fdf0f1   superficie del sello
```

El `#c6111a` está muestreado del archivo del logo, no aproximado a ojo, y no
necesitó corrección: pasa AA sobre blanco y también como relleno sólido con
texto blanco encima.

---

## 5. Accesibilidad — lo que la auditoría encontró

Contrastes WCAG 2.1 medidos contra los dos fondos reales del sitio.

| Token | Hex | s/ blanco | s/ #f4f7fa | Veredicto |
|---|---|---|---|---|
| navy-700 | `#10284d` | 14.66 | 13.63 | AAA |
| tinta | `#1f2d3d` | 13.99 | 13.01 | AAA |
| rojo-600 | `#c6111a` | 6.01 | 5.59 | AA |
| celeste-800 | `#0b6683` | 6.48 | 6.02 | AA |
| celeste-700 | `#2f7593` | 5.14 | 4.78 | AA |
| **gris (nuevo)** | `#5a6878` | **5.70** | **5.30** | **AA** |
| ~~gris (anterior)~~ | ~~`#6b7a8d`~~ | ~~4.38~~ | ~~4.07~~ | ~~**REPRUEBA**~~ |
| celeste-500 | `#6cb3d3` | 2.33 | 2.16 | Solo decorativo |

### Dos correcciones que hay que llevar al código

1. **`--gris` pasa de `#6b7a8d` a `#5a6878`.** El anterior daba **4.07:1** sobre
   el fondo suave del sitio: reprueba AA (mínimo 4.5) en el color con el que
   está escrito todo el texto secundario del sitio. Es el hallazgo más serio de
   la auditoría y es un cambio de un solo token.

2. **Los colores de estado necesitan variante de texto.** `--ok #2e9e5b` (3.41),
   `--error #d64545` (4.38) y `--aviso #b8860b` (3.25) reprueban como texto
   sobre blanco. Sirven como **relleno** de badge o ícono, no como letra. Por eso
   cada estado ahora tiene su par `-texto`, más oscuro, que sí pasa:
   `--ipd-ok-texto #15703a` (6.16), `--ipd-error-texto #b53232` (6.06),
   `--ipd-aviso-texto #845c08` (5.97).

3. **El oro `#d4af37` se queda, con una regla nueva.** En una primera pasada se
   dio por retirado sobre un conteo mal hecho; el conteo correcto son **13 usos
   reales** en `src/`: estrellas de valoración, sello del certificado, racha de
   estudio y estados de logro del aula. No es un color de marca, es **el color
   de un logro**, y entra al sistema como `--ipd-oro-*`. Lo que sí era un
   problema: da 2.10:1 y se usaba para **glifos** de estrella, que necesitan
   3:1. Por eso ahora hay dos valores: `--ipd-oro-500 #d4af37` para relleno,
   degradados y bordes, y `--ipd-oro-700 #ad8420` (3.44:1) para estrellas e
   íconos.

### Cómo volver a correr la auditoría
Cualquier hex nuevo se mide antes de entrar. El cálculo es WCAG 2.1 estándar
(luminancia relativa sRGB); el script que se usó está en el commit de esta
estandarización. Regla: **texto normal ≥ 4.5:1, texto ≥ 18 px o negrita ≥ 3:1,
elementos de interfaz y bordes de foco ≥ 3:1.**

---

## 6. Forma

**La marca no es de esquinas redondas.** La píldora (`9999px`) se retiró del
sistema: hacía que todo pareciera una aplicación de consumo y no un instituto que
emite certificados. La escala es **8 / 10 / 16**, asignada por rol:

| Rol | Radio | Qué lo usa |
|---|---|---|
| Se etiqueta | `8px` | chips, badges, etiquetas |
| Se toca | `10px` | botones, tabs |
| Se escribe | `10px` | input, select, textarea |
| Contiene | `16px` | tarjetas, modales, paneles, imágenes |

El único círculo que queda (`--ipd-radio-redondo`) es para lo que es circular
por geometría: **avatares, puntos de estado, numeradores y botones de ícono de
igual ancho y alto**. Nunca un botón con texto.

Botones redondos dentro de tarjetas cuadradas es lo que hace que una interfaz se
vea armada por partes. Estos valores no se mezclan ni se inventan otros.

**Sombras: dos niveles y ninguno más** (`--ipd-sombra-1` en reposo,
`--ipd-sombra-2` en hover). Siempre tintadas de navy, nunca negro puro: el negro
sobre un fondo azulado se ve gris sucio. Los botones con degradado llevan además
su sombra propia (`--ipd-sombra-primario`, `--ipd-sombra-sello`), tintada del
color del propio botón para que el relieve se vea del mismo material.

### Corrección al borde de campo

`--ipd-borde-fuerte #c9d5df` se usaba como borde de input y da **1.39:1** contra
el fondo del sitio. WCAG 1.4.11 pide **3:1** para cualquier control de interfaz,
así que en la práctica había campos que no se veían. Entra
`--ipd-borde-campo #768495` (**3.55:1**) para inputs; el `#c9d5df` se queda para
separadores y bordes de tabla, que son decorativos.

---

## 7. Degradados

**De dónde salen.** No son un adorno arbitrario: el **libro abierto del logotipo
ya es un degradado de cian a azul**. El sistema lo extiende al resto de la
interfaz, así que el degradado es una propiedad de la marca y no un efecto de
moda pegado encima.

### La regla dura

> Un degradado con texto blanco encima es accesible **solo si su parada más clara
> pasa 4.5:1**. De nada sirve que el promedio pase: si la esquina clara deja el
> texto ilegible, el botón está roto en esa esquina.

Por eso cada degradado del sistema lleva medida su parada clara:

| Token | Degradado | Parada clara | Contraste |
|---|---|---|---|
| `--ipd-grad-primario` | `#10284d` a `#24608f` | `#24608f` | 6.68:1 |
| `--ipd-grad-primario-hover` | `#0a1c38` a `#1c4d7a` | `#1c4d7a` | 8.78:1 |
| `--ipd-grad-secundario` | `#0b6683` a `#307a99` | `#307a99` | 4.81:1 |
| `--ipd-grad-secundario-hover` | `#084f66` a `#2f7593` | `#2f7593` | 5.14:1 |
| `--ipd-grad-sello` | `#c6111a` a `#8f0c12` | `#c6111a` | 6.01:1 |
| `--ipd-grad-sello-hover` | `#9d0d14` a `#7d0a10` | `#9d0d14` | 8.40:1 |
| `--ipd-grad-ok` | `#1c7a44` a `#15703a` | `#1c7a44` | 5.36:1 |

Dos degradados no llevan texto encima y por eso no tienen medida:

- **`--ipd-grad-marca`** (`#06142b` a `#10284d` a `#2f7593`) para superficies
  grandes: héroe, footer, portadas, encabezado de tarjeta. Si va a llevar texto,
  el texto va en blanco y en tamaño de titular, nunca cuerpo chico.
- **`--ipd-grad-libro`** (`#00e4ff` a `#0130db`), el del logotipo. Es
  **decorativo**: filos, barras de progreso, fondos de ilustración. Es demasiado
  claro para texto blanco, así que texto encima está prohibido.

### Cómo se usa un degradado

1. **Siempre a 135 grados.** Un solo ángulo en todo el producto. Ángulos
   distintos en la misma pantalla es lo que delata un sistema improvisado.
2. **Filo superior claro.** Una línea de `rgba(255,255,255,.34)` de 1 px arriba
   es lo que hace que el botón se lea como una superficie con volumen y no como
   un rectángulo pintado.
3. **La sombra se tiñe del color del botón**, nunca gris.
4. **El degradado no reemplaza la regla del rojo (§3).** `grad-sello` tiene
   exactamente el mismo permiso que el rojo plano: certificación y verificación.
5. **Nada de degradados en texto.** Los titulares van en color sólido.
6. **Un degradado por superficie.** No se anidan.

---

## 8. Modo oscuro

El sitio público hoy es **solo claro**, y por ahora se queda así: el panel admin
y el aula ya tienen variables `.dark` de shadcn a medio conectar, y encender el
modo oscuro en la web pública sin resolver eso deja secciones invertidas a mitad
de scroll.

Cuando se haga, la base ya está: `navy-900 #06142b` como fondo, `celeste-500`
como color de texto de acento (6.30:1 sobre navy) y blanco para el cuerpo.
**El logotipo a color no sirve sobre navy** — el birrete y la palabra IPADECP son
negros y desaparecen. Ahí va la versión de una tinta en blanco
(`logos/logo-ipadecp-blanco.svg`), que además se ve mejor. Ver `./logo-uso.md`.
