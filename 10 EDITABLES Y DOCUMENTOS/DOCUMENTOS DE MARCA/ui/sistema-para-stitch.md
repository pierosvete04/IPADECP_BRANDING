# Preámbulo de sistema para Google Stitch

**Cómo se usa:** este bloque va **pegado al inicio de cada prompt**, antes del
prompt de la página. Stitch no recuerda entre generaciones: si no le repites el
sistema, cada pantalla te sale con otra paleta y otro radio.

Está en español porque Stitch responde bien en español y el copy de la pantalla
tiene que salir en español de todos modos. Si notas que interpreta mejor en
inglés, la versión traducida está al final.

---

## Bloque para pegar

```
CONTEXTO DE MARCA
IPADECP es un centro de capacitación peruano, 100 % virtual, para personal de
salud: enfermeras, técnicos, obstetras, paramédicos y estudiantes de carreras
de salud. Vende cursos de 6 módulos y certificación profesional con código QR
verificable. La mayoría de sus usuarios entra desde el celular, muchas veces
después de un turno de trabajo. El sitio tiene que verse moderno y confiable,
NO experimental: lo que se juega en cada pantalla es que la persona crea que el
certificado vale.

SISTEMA VISUAL, respétalo exactamente

Colores
- Primario, navy: #10284d. Encabezados, botón principal, superficies oscuras.
- Navy oscuro: #0a1c38. Hover del primario.
- Navy profundo: #06142b. Footer.
- Navy de texto: #001331. Titulares.
- Navy lavado: #e8eef6. Chips y fondos de sección alterna.
- Fondo del sitio: #f4f7fa.
- Secundario, celeste: #6cb3d3. SOLO decorativo (bordes, íconos, ilustración).
  Nunca como color de texto sobre fondo claro.
- Celeste accesible: #2f7593. Este sí para texto y botones sólidos.
- Celeste profundo: #0b6683. Enlaces y etiquetas de sección.
- Acento, rojo institucional: #c6111a. SOLO para certificación y verificación:
  el sello, el certificado, la pantalla de verificar. Nunca en botones de
  compra, enlaces ni encabezados.
- Oro de logro: #d4af37 en rellenos, #ad8420 en estrellas e íconos.
- Texto: #1f2d3d. Texto secundario: #5a6878. Bordes: #e1e8ed.
  Borde de campo de formulario: #768495.
- Estados: correcto #15703a, error #b53232, aviso #845c08.

Degradados, siempre a 135 grados
- Botón primario: #10284d a #24608f.
- Botón secundario: #0b6683 a #307a99.
- Sello y verificación: #c6111a a #8f0c12.
- Superficies grandes (héroe, footer): #06142b a #10284d a #2f7593.
- Los botones con degradado llevan un filo superior blanco de 1 px al 34 % y
  una sombra tintada del propio color del botón, nunca gris.

Tipografía
- Títulos, botones y cifras: Hanken Grotesk. Pesos 700 y 800, interletrado
  negativo (-0.02em) de 2rem para arriba.
- Cuerpo, formularios y tablas: Inter. Pesos 400, 500 y 600.
- Códigos que la persona copia o dicta (código corto, número de registro, DNI):
  tipografía monoespaciada, interletrado abierto.
- Párrafos a 65 caracteres de ancho máximo. Cuerpo nunca por debajo de 15 px.

Forma
- NO uses esquinas de píldora. Nada de border-radius 9999px en botones o chips.
- Chips y etiquetas: 8 px. Botones, tabs y campos: 10 px. Tarjetas, modales y
  paneles: 16 px.
- El círculo solo para avatares, puntos de estado y botones de ícono cuadrados.
- Dos niveles de sombra, tintadas de navy: 0 4px 10px rgba(10,28,56,.12) en
  reposo y 0 8px 20px rgba(10,28,56,.18) en hover. Nunca sombra negra.

Estructura
- Ancho máximo del contenido: 1180 px, centrado.
- Respiro entre secciones: 96 px en escritorio, 56 px en móvil.
- Header pegado arriba, de 68 px de alto, con fondo claro translúcido y
  desenfoque. La navegación entra en UNA sola línea en escritorio.
- Todo colapsa a una columna por debajo de 768 px.

VOZ Y TEXTO
- Tuteo. Voz activa. Una idea por oración. Español del Perú (celular,
  computadora, provincia, courier, DNI, Yape).
- CERO rayas largas. Usa punto, coma, dos puntos o paréntesis.
- Sin emojis.
- Botones de máximo 3 palabras y en verbo: "Ver cursos", "Llevar este curso",
  "Verificar certificado", "Escribir por WhatsApp", "Crear cuenta".
- Un solo texto por intención en toda la página. No pongas "Contáctanos" en un
  lado y "Escríbenos" en otro.
- Prohibidas: potencia, transforma, revoluciona, solución integral, de
  vanguardia, excelencia académica, líder en el rubro, innovador, sinergia,
  ¡última oportunidad!, algo salió mal, próximamente.

ACCESIBILIDAD, no es opcional
- Texto normal mínimo 4.5:1 de contraste; texto grande e íconos, 3:1.
- La etiqueta va ARRIBA del campo, nunca el placeholder como etiqueta.
- El texto de ayuda va debajo del campo; el de error también, en #b53232.
- Foco visible siempre.

LO QUE NO QUIERO
- Nada de marquesinas de logos que se desplazan solas.
- Nada de contadores que se reinicien en cada visita, ni avisos de "quedan N
  cupos" sin stock real. Un contador con FECHA REAL de fin de promoción sí es
  legítimo: es información verdadera.
- Nada de cintas de "scroll" ni flechas animadas al fondo del héroe.
- Nada de etiquetas superpuestas sobre las fotos.
- Nada de interfaces de producto INVENTADAS y dibujadas con rectángulos. Las
  capturas REALES del aula sí van, y conviene usarlas.
- Nada de tres tarjetas iguales en fila como recurso por defecto.
- Nada de numerar las secciones ("01 / Servicios").
- Máximo una etiqueta pequeña en mayúsculas encima de un titular cada tres
  secciones. No la pongas en todas.
- Nada de pago en cuotas ni precios divididos entre meses: no hay
  financiamiento.
- Nada de "prueba gratis", "clase de muestra" ni "demo": no se regala ningún
  módulo.
- NUNCA afirmes ni insinúes que el certificado está avalado, acreditado o
  reconocido por alguna entidad, ni nombres al MINSA, SUNEDU, colegios
  profesionales o universidades. El instituto no tiene esa validación. Lo que
  sí se puede decir, y es más fuerte, es que el certificado se comprueba en
  segundos.
```

---

## Version in English, if Stitch reads it better

```
BRAND CONTEXT
IPADECP is a Peruvian, 100% online training institute for healthcare workers:
nurses, technicians, midwives, paramedics and health students. It sells 6-module
courses and professional certification with a verifiable QR code. Most users
browse on a phone, often after a work shift. The site must look modern and
trustworthy, NOT experimental: every screen has to make the person believe the
certificate is worth something. All on-screen copy must be in Peruvian Spanish.

Colors: primary navy #10284d (dark #0a1c38, deep #06142b, text navy #001331,
washed #e8eef6), page background #f4f7fa, secondary sky blue #6cb3d3
(DECORATIVE ONLY, never as text on light), accessible blue #2f7593 for text and
solid buttons, deep blue #0b6683 for links, institutional red #c6111a RESERVED
for certification and verification only, achievement gold #d4af37 (#ad8420 for
glyphs), body text #1f2d3d, secondary text #5a6878, borders #e1e8ed, form field
border #768495, success #15703a, error #b53232, warning #845c08.

Gradients, always 135 degrees: primary button #10284d to #24608f, secondary
#0b6683 to #307a99, seal #c6111a to #8f0c12, large surfaces #06142b to #10284d
to #2f7593. Gradient buttons get a 1px white top edge at 34% and a shadow
tinted with the button's own color, never grey.

Type: Hanken Grotesk for headings, buttons and figures (700 and 800, negative
tracking above 2rem). Inter for body, forms and tables (400, 500, 600).
Monospace for codes people copy or read aloud. Paragraphs max 65 characters
wide. Body text never below 15px.

Shape: NO pill corners. Chips 8px, buttons and fields 10px, cards 16px. Circles
only for avatars, status dots and square icon buttons. Two navy-tinted shadow
levels, never black.

Layout: 1180px max width, 96px section rhythm on desktop and 56px on mobile,
68px sticky header with a single-line nav, everything collapses to one column
below 768px.

Do NOT include: scrolling logo marquees, counters that reset on every visit or
"only N seats left" notices with no real stock (a countdown with a REAL promo
end date is fine), scroll cue arrows, labels overlaid on photos, INVENTED
product interfaces drawn with rectangles (real screenshots of the classroom are
welcome), three identical cards in a row, numbered section labels, or an
uppercase eyebrow above every heading (max one per three sections).
NEVER claim or imply the certificate is accredited, endorsed or officially
recognised by any body, and never name a ministry, university or professional
association. No instalment pricing and no free trial: neither exists.
```

---

## Notas de uso

**Stitch no recuerda.** Cada pantalla es una generación independiente. Pega el
preámbulo entero cada vez, aunque sea largo.

**Genera de a una pantalla.** Si le pides la web completa en un prompt, te
devuelve un promedio de todas las páginas y ninguna queda bien.

**Empieza por la ficha de curso.** Es la pantalla que vende, la más compleja y
la que fija el lenguaje visual del resto. Cuando esa quede, las demás salen más
rápido y más consistentes.

**Si te devuelve píldoras.** Es el error más frecuente de Stitch con este
sistema, porque su valor por defecto es redondear todo. Corrígelo con:
"Rehazlo con esquinas de 10 px en botones y 8 px en chips. Ningún elemento con
esquinas de píldora."

**Si te devuelve el celeste como texto.** Corrígelo con: "El celeste #6cb3d3 es
solo decorativo. Todo el texto azul sobre fondo claro va en #2f7593 o #0b6683."

**Si mete rojo donde no va.** Corrígelo con: "El rojo #c6111a es solo para
certificación y verificación. El botón de compra va con el degradado navy."
