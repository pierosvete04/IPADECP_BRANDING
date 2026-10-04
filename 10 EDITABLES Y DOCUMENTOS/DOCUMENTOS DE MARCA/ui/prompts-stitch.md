# Prompts de Stitch, pantalla por pantalla

Cada prompt va **precedido del preámbulo** de `sistema-para-stitch.md`. Sin él,
Stitch inventa su propia paleta.

Orden recomendado de generación: **ficha de curso → inicio → catálogo →
verificación → el resto.** La ficha es la que vende y la más compleja: cuando
esa queda, fija el lenguaje y las demás salen consistentes.

> **Sobre los textos de muestra.** Los testimonios, nombres y cifras de estos
> prompts son **material de maqueta**, marcados con `[MUESTRA]`. Sirven para que
> Stitch dibuje la pantalla con contenido creíble. **Antes de publicar hay que
> reemplazarlos por testimonios y cifras reales del instituto.** Publicar
> testimonios inventados como si fueran reales es otra cosa, y la marca se
> apoya justamente en lo contrario.

---

# 1. Ficha de curso (la página de producto)

**Esta es la pantalla más importante del sitio.** Es donde se decide la compra.
Revisada contra la referencia real de Coderhouse
(`coderhouse.com/pe/cursos/ai-automation-avanzado`).

## Lo que confirmé de la referencia

| Coderhouse hace | Ya lo tenía |
|---|---|
| Tarjeta de compra fija a la derecha con precio tachado, % de descuento y precio final | Sí |
| Bloque "Para quién es" | Sí |
| Certificado mostrado como imagen, no descrito | Sí |
| Testimonios con nombre, cargo y empresa | Sí |
| Preguntas frecuentes en acordeón | Sí |
| Barra de anclas pegada (Información, Programa, Fechas) | No, lo agrego |
| Tarjeta de datos rápidos bajo el héroe (nivel, duración, módulos, formato) | No, lo agrego |
| Bloque "Al finalizar, podrás" con las competencias que se llevan | No, lo agrego |
| Alternancia de secciones claras y oscuras a lo largo del scroll | No, lo agrego como regla |

## Las cuatro diferencias que cambian el diseño

**No se puede copiar la página tal cual, porque el producto no es el mismo.**

### 1. Coderhouse vende clases EN VIVO. IPADECP no.

Toda su página gira alrededor de **"Ver fechas"**: el botón principal no dice
comprar, dice ver fechas, y hay un bloque grande de próximas cohortes con
horarios y "quedan 11 lugares". Es coherente con lo que venden: clases en vivo,
dos veces por semana, en un horario fijo.

**IPADECP es 100 % asincrónico y sin horarios.** Ese bloque de fechas
sencillamente no existe, y no hay que inventarlo.

Y acá está lo interesante: **eso que para Coderhouse es un bloque, para IPADECP
es una ventaja.** Donde ellos ponen "empieza el 10 de setiembre, martes y
jueves de 17:00 a 19:00", nosotros ponemos **"empiezas hoy, a la hora que
puedas"**. A alguien que trabaja por turnos, eso le resuelve el problema que la
cohorte le crea. Por eso el bloque de fechas se reemplaza por una línea en la
tarjeta de compra que lo dice en positivo.

### 2. El temario: ellos lo muestran abierto, este proyecto ya lo plegó

Coderhouse lista sus 11 módulos **siempre visibles**, numerados 1/11 a 11/11.
Les funciona porque su producto **es** el programa: lo que venden es la
profundidad del learning path.

Pero este proyecto ya tomó la decisión contraria, y con un motivo escrito en el
propio código: la ficha con ocho bloques abiertos medía varias pantallas y los
enlaces de la barra de secciones saltaban dentro del mismo tocho.

**La salida es intermedia, y es mejor que cualquiera de los dos extremos:**
los **títulos de los 6 módulos siempre visibles** y numerados, como Coderhouse,
y **las lecciones de cada módulo plegadas**. Se ve de un vistazo todo el
programa sin que la página mida cinco pantallas.

### 3. El contador regresivo

Coderhouse tiene un cronómetro de oferta en la tarjeta de compra. Mis reglas lo
prohibían de plano, y ahí me pasé de rígido. El matiz correcto:

- **Un contador con fecha real de fin de promoción es legítimo.** Es
  información verdadera y ayuda a decidir.
- **Lo prohibido es el contador que se reinicia** cada vez que entras, o el
  "quedan 3 cupos" sin stock real detrás. Eso es urgencia falsa y contradice
  todo lo que la marca dice sobre ser comprobable.

Si la promoción tiene fecha real en el panel, ponlo. Si no, no.

### 4. Las capturas de la plataforma

Coderhouse llena la página con **simulaciones** de su aula: un chat de clase,
una entrega corregida, un quiz con XP, un ranking de puntos. Es lo que más
espacio ocupa en toda su página.

Mis reglas prohibían "pantallazos falsos dibujados con divs", y eso sigue en
pie. Pero el matiz importa: **IPADECP tiene aula de verdad**, así que puede
mostrar lo mismo con **capturas reales**. Y tiene además gamificación ya
construida (rachas, puntos, estados de logro con el oro de marca). Eso es
material real que hoy no se está usando para vender, y debería.

## Prompt

```
Diseña la página de detalle de un curso para IPADECP, en español. Escritorio
1440 px y móvil 390 px.

ESTRUCTURA: dos columnas. La izquierda (62 %) scrollea con todo el contenido.
La derecha (38 %) es una tarjeta de compra PEGADA que sigue el scroll y queda
siempre visible. En móvil todo pasa a una columna y la tarjeta se convierte en
una barra fija en el borde inferior con el precio y el botón de compra.

RITMO DE FONDOS: las secciones alternan a lo largo del scroll, pero con una
regla, no al azar. Fondo claro (#f4f7fa o blanco) por defecto. Fondo navy con
el degradado de marca SOLO en tres momentos: el aula por dentro, el
certificado, y el cierre de WhatsApp. Esos son los momentos de marca.

ENCABEZADO DE LA PÁGINA (ancho completo, fondo #f4f7fa)
- Migas de pan pequeñas: Inicio / Cursos / Enfermería
- Chip con la categoría: "Enfermería"
- Título grande en Hanken Grotesk 800: "Cuidados intensivos en el paciente
  crítico adulto"
- Párrafo de dos líneas: "Manejo del paciente crítico en UCI: monitoreo
  hemodinámico, ventilación mecánica y sedoanalgesia. Con bibliografía fechada
  y certificado verificable."
- Estrellas doradas en #ad8420 con "4.8" y "(127 opiniones)" al lado

DATOS RÁPIDOS: una tira horizontal de 5 datos justo debajo del título, dentro
de una tarjeta blanca de esquinas de 16 px, separados por líneas verticales
finas #e1e8ed. Cada dato con un ícono chico en #2f7593, la etiqueta arriba en
gris y el valor abajo en Hanken Grotesk 700:
MODALIDAD "100 % virtual" · DURACIÓN "120 horas académicas" ·
MÓDULOS "6" · NIVEL "Intermedio" · CERTIFICADO "Verificable por QR"
En móvil pasa a una rejilla de 2 columnas.

AL FINALIZAR, PODRÁS: bloque corto de tres competencias, cada una con un ícono
de check en #15703a. No son temas del temario: son resultados.
"Valorar y monitorizar a un paciente crítico con criterio propio"
"Manejar los parámetros básicos de ventilación mecánica"
"Aplicar los protocolos de prevención de infecciones en tu servicio"

BARRA DE ANCLAS PEGADA: bajo el header, una barra fina de fondo blanco con
borde inferior, con los enlaces internos: Programa · Qué incluye · Certificado ·
Opiniones · Preguntas. El activo con una barra de 3 px en #2f7593 debajo.
Se pega al hacer scroll, justo debajo del header. Desplazable en móvil.

TARJETA DE COMPRA PEGADA (derecha, fondo blanco, esquinas de 16 px, sombra
media, borde #e1e8ed)
- Imagen del curso arriba, esquinas superiores de 16 px, foto real de una
  enfermera en una unidad de cuidados intensivos
- Precio: "S/ 250" tachado en gris pequeño, y debajo "S/ 149" grande en Hanken
  Grotesk 800 color #001331. Al lado un chip verde #15703a con "40 % dto."
- Debajo del precio, en texto chico gris: "Pago único. Sin mensualidades."
- Botón principal ancho completo, degradado navy #10284d a #24608f, texto
  blanco, esquinas de 10 px: "Llevar este curso"
- Botón secundario ancho completo, borde #768495 sobre blanco, texto #10284d:
  "Consultar por WhatsApp"
- Un recuadro con fondo #f0f9fd y borde izquierdo de 4 px en #2f7593, con un
  ícono de reloj: "Empiezas hoy mismo. No esperas a que abra un grupo."
- Separador fino, y debajo una lista de 5 líneas con íconos pequeños en
  #2f7593, sin viñetas de punto:
  "Acceso de por vida"
  "Material en Word y PowerPoint editables"
  "Certificado digital con código QR"
  "Certificado físico opcional, a todo el Perú"
  "Sin horarios: estudias cuando puedas"
- Al pie, los medios de pago en gris chico: tarjeta, Yape, transferencia.

COLUMNA IZQUIERDA, en este orden exacto:

1. PARA QUIÉN ES
   Dos columnas de texto con una lista de perfiles, cada uno con un ícono de
   check en #15703a:
   "Enfermeras y enfermeros de UCI, emergencia y hospitalización"
   "Técnicos en enfermería que rotan por áreas críticas"
   "Estudiantes de enfermería en internado"
   Debajo, en un recuadro de fondo #f0f9fd con borde izquierdo de 4 px en
   #2f7593: "No necesitas experiencia previa en UCI. El curso empieza por el
   monitoreo básico y avanza hasta ventilación mecánica."

2. PROGRAMA
   Los 6 módulos SIEMPRE VISIBLES en una lista numerada vertical. Cada módulo:
   el número grande en gris claro a la izquierda ("1/6", "2/6"...), el nombre
   en Hanken Grotesk 700, y la cantidad de lecciones a la derecha. Dentro de
   cada módulo, la lista de temas va PLEGADA tras un botón de texto "Ver los
   temas". Los títulos de módulo no se pliegan nunca.
   Entre módulos, una línea fina. No uses tarjetas.
   1/6 Valoración inicial del paciente crítico (5 lecciones)
   2/6 Monitoreo hemodinámico (6 lecciones)
   3/6 Ventilación mecánica invasiva y no invasiva (7 lecciones)
   4/6 Sedoanalgesia y delirio en UCI (5 lecciones)
   5/6 Prevención de infecciones asociadas al cuidado (6 lecciones)
   6/6 Cuidados de enfermería en el paciente crítico (6 lecciones)
   Al pie: "Temario actualizado en agosto de 2026. Cada módulo lleva su
   bibliografía con año y fuente."

3. QUÉ INCLUYE
   Rejilla tipo bento de 5 celdas, de tamaños distintos, NO cinco tarjetas
   iguales. Dos celdas llevan imagen o un fondo con degradado suave de marca;
   las otras tres son texto sobre blanco.
   - Celda grande: "6 módulos con material descargable" y el detalle "Cada
     módulo trae el documento en Word, la presentación en PowerPoint, los
     videos de clase, una tarea práctica y su evaluación."
   - "Material editable" con "Te lo damos en Word y PowerPoint para que puedas
     adaptarlo y capacitar a tu propio servicio."
   - "Bibliografía fechada" con "Cada afirmación con su estudio, su año y dónde
     encontrarlo."
   - "Evaluación por módulo" con "Tareas y exámenes que sí se corrigen."
   - "Certificado automático" con "Al llegar al 100 % se emite solo, con tu QR."

4. ASÍ SE VE POR DENTRO (fondo navy con el degradado de marca, texto blanco)
   Dos columnas. A la izquierda, una CAPTURA REAL del aula virtual de IPADECP
   mostrando un módulo con su lista de lecciones y la barra de progreso, dentro
   de un marco de navegador simple con esquinas de 16 px.
   A la derecha:
   Título "Estudias desde el celular, cuando puedas"
   Párrafo: "No hay clases en vivo obligatorias. El avance se guarda solo, así
   que puedes dejar una lección a la mitad y retomarla en el siguiente
   descanso."
   Tres líneas con íconos en #6cb3d3: "Progreso guardado automáticamente",
   "Material descargable en cada módulo", "Tu racha de estudio y tus logros".
   Debajo, una segunda captura más chica del panel de progreso con la racha y
   los puntos, donde aparece el oro de logro #d4af37.
   IMPORTANTE: son capturas reales del producto, no interfaces inventadas
   dibujadas con rectángulos.

5. EL CERTIFICADO QUE RECIBES (fondo navy con el degradado de marca)
   Dos columnas. A la izquierda, la fotografía de un certificado impreso, en
   perspectiva ligera, con un código QR visible. A la derecha:
   Título "Se verifica en segundos, sin crear ninguna cuenta"
   Párrafo: "Tu empleador escanea el QR con la cámara del celular y ve al
   instante si el certificado es válido. No es un archivo que subimos: se
   genera en el momento desde nuestros registros."
   Tres líneas con íconos: "Certificado digital en PDF, ilimitado",
   "Certificado físico por courier a todo el Perú",
   "Verificable por QR, código corto o número de registro"
   Un recuadro con fondo blanco al 10 % y borde izquierdo de 4 px en #c6111a:
   "Si un certificado se anula, la verificación también lo dice. Eso es lo que
   protege el valor del tuyo."
   Un botón blanco con texto #10284d: "Ver cómo se verifica".
   ESTE es el único lugar de la página donde aparece el rojo.

6. OPINIONES
   Encabezado con "4.8" muy grande en Hanken Grotesk 800, cinco estrellas en
   #ad8420 y "127 opiniones". Debajo, un carrusel horizontal de testimonios con
   desplazamiento por tarjeta, cada uno con foto circular, comillas
   tipográficas, máximo tres líneas, y al pie el nombre en Hanken Grotesk 700
   con la profesión y la ciudad en gris.
   [MUESTRA, reemplazar antes de publicar]
   - "Lo llevé en las noches después del turno. El material en Word me sirvió
     para capacitar a mi propio servicio." Milagros Quispe Ccahuana, Enfermera,
     Huancayo.
   - "En el concurso me pidieron comprobarlo. Escanearon el QR delante mío y
     salió al toque." Elmer Huamán Vargas, Técnico de laboratorio, Trujillo.
   - "Trabajo hace once años y no tenía nada que lo respaldara. El sobre me
     llegó a Juliaca en cinco días." Rosa Ccopa Mamani, Enfermera, Juliaca.
   - "Estudié desde el celular en los descansos. El avance se guardaba solo y
     no perdí nada." Jhoselyn Ramírez Tapia, Obstetra, Piura.

7. PREGUNTAS FRECUENTES
   Acordeón plegado, 6 preguntas:
   "¿En cuánto tiempo lo termino?"
   "¿Hay clases en vivo obligatorias?"
   "¿El certificado físico llega a provincia?"
   "¿Puedo verificar un certificado sin tener cuenta?"
   "¿Qué pasa si no apruebo una evaluación?"
   "¿Puedo usar el material para capacitar a mi equipo?"

8. CONSULTA POR WHATSAPP (fondo navy con el degradado de marca)
   Banda de ancho completo, texto blanco. Título "¿Te quedó alguna duda?" y
   párrafo "Escríbenos y te decimos si este curso es el que te conviene. Te
   respondemos apenas veamos tu mensaje." Un botón blanco con texto #10284d:
   "Escribir por WhatsApp".

NO INCLUYAS: bloque de próximas fechas ni de cohortes (este curso no tiene
horarios), pago en cuotas ni el precio dividido entre meses (no hay
financiamiento), botones de prueba gratis o clase de muestra (no se regala
ningún módulo), contadores regresivos sin fecha real, avisos de "quedan N
lugares", logos de empresas donde trabajan los egresados, ni ninguna mención a
que el certificado esté avalado, acreditado o reconocido por alguna entidad
(MINSA, SUNEDU, colegios profesionales, universidades): el instituto no tiene
esa validación y la web no puede insinuarla.

FOOTER de fondo #06142b con el logotipo en blanco.
```

## Las tres decisiones, ya resueltas

Confirmadas por el instituto el 2 de setiembre de 2026. Las tres son **no**, y
las tres cambian el prompt de arriba. Quedan escritas acá para que nadie las
vuelva a proponer dentro de seis meses.

### 1. No hay pago en cuotas

Coderhouse ofrece hasta 12 cuotas y lo pone grande en la tarjeta. **IPADECP no
tiene financiamiento.** El precio es pago único.

No se trata como una carencia, se dice en positivo: la línea **"Pago único. Sin
mensualidades."** va debajo del precio, en gris chico. A este precio y con este
público, no deber nada después es un argumento, no una disculpa.

**Prohibido en toda la web:** simular cuotas, mostrar el precio dividido entre
meses ("desde S/ 12 al mes"), o poner "financiamiento disponible".

### 2. No hay módulo gratis de prueba

Coderhouse regala 2 clases. **IPADECP no da acceso gratuito a ningún módulo.**

Lo que sí se puede hacer, y ya está en el prompt, es reducir la incertidumbre
sin regalar producto: el temario con los títulos de los 6 módulos siempre
visibles, la captura real del aula por dentro, y la salida de WhatsApp para
preguntar antes de pagar. Esa es la respuesta a "no sé si esto es para mí".

**Prohibido:** botones de "Prueba gratis", "Clase de muestra" o "Demo".

### 3. No hay sección de "dónde vale este certificado"

Coderhouse llena media página con logos de empresas donde trabajan sus
egresados y la cifra de graduados. **Esa sección no se hace.**

Y hay una razón de fondo, no solo de falta de datos: **el instituto todavía no
tiene validación ni reconocimiento de ninguna entidad externa.** Eso no le quita
valor al certificado (se puede comprobar, que es más de lo que ofrece la
competencia), pero sí marca un límite duro sobre lo que la web puede afirmar.

**Regla dura para toda la web, los anuncios y las piezas gráficas:**

- No se dice ni se insinúa que el certificado esté **avalado, acreditado,
  reconocido, autorizado o convalidado** por ninguna entidad.
- No se nombra al MINSA, a SUNEDU, a un colegio profesional, a una universidad
  ni a ningún ministerio, ni siquiera para decir que "cumple sus estándares".
- No se promete **puntaje en concursos**, ascensos ni bonificaciones.
- No se muestran logos de instituciones con las que no hay convenio firmado.

Esto ya está bien resuelto en `/nosotros`, que dice de frente que el certificado
no reemplaza la colegiatura ni otorga créditos académicos oficiales. Esa página
es el modelo: el resto del sitio no debe contradecirla.

> **Lo que sí se puede afirmar, y es más fuerte:** que el certificado **se puede
> comprobar en segundos**. Ese es el único terreno donde IPADECP gana, y no
> necesita el permiso de nadie para decirlo.

---

# 2. Inicio

## La portada es una imagen, y eso ya está construido

Lo que pediste (una imagen de portada que se cambie por campaña, sin tocar
código) **ya existe en el sitio y está bien resuelto**. El componente
`BannerPortada` es un carrusel de imágenes que abre la home, con el texto
DENTRO de la imagen que sube el administrador, y se gestiona desde el panel
(`BannersSection`). Cambias la promoción subiendo otra imagen, sin deploy.

Y está resuelta la parte que suele salir mal: acepta **dos piezas por banner**,
una de escritorio y otra de móvil, porque un banner apaisado con texto se vuelve
ilegible en un celular.

| Pieza | Medida | Proporción |
|---|---|---|
| Escritorio | **1600 × 500 px** | 1600 / 500 |
| Móvil | **1200 × 900 px** | 1200 / 900 |

Si subes una sola, se usa en los dos tamaños. Si el banner no lleva enlace, se
pinta como imagen suelta y no como enlace muerto.

**La estructura que ya tiene la home es la correcta, y conviene mantenerla:**

1. `BannerPortada` arriba: **la campaña del mes**, imagen, cambia sin deploy.
2. `HeroInicio` justo debajo: **la propuesta de valor permanente**, texto real.

Esa separación importa por una razón concreta: el texto metido dentro de una
imagen no lo lee Google ni un lector de pantalla. Si la portada fuera *solo*
imagen, la home se quedaría sin titular indexable. Con las dos piezas tienes lo
mejor de cada una: la promoción se cambia en 30 segundos desde el panel, y el
mensaje permanente sigue siendo texto de verdad que posiciona en buscadores.

> Cuando encargues cada banner, exige que la imagen lleve **alt** descriptivo
> (el panel lo pide) y que el texto dentro de la pieza no baje de 32 px en la
> versión de escritorio ni de 40 px en la de móvil. Debajo de eso no se lee en
> un celular al sol.

Al final de este documento hay un prompt aparte para **generar el arte del
banner** con Stitch o con una herramienta de imagen.

## Criterio: qué llama la atención de ESTA audiencia

No es una landing de SaaS. Le habla a alguien que trabaja por turnos, entra
desde el celular y necesita un papel que le sirva en un concurso o un legajo.
En orden de lo que más mueve:

1. **El verificador en vivo, en la propia portada.** Es la recomendación más
   fuerte de todo este documento. En vez de *decir* que el certificado se
   verifica, poner el campo ahí mismo para que cualquiera lo compruebe. Nadie
   en el sector lo hace, y la página de verificación ya existe. Convierte el
   diferencial en algo que la persona toca en tres segundos.
2. **Mostrar el certificado.** Están comprando un papel. Hay que enseñarlo.
3. **Testimonios de pares, no de gente genérica.** Profesión y ciudad al lado
   del nombre. "Enfermera, Huancayo" hace más que cualquier titular.
4. **Los dos caminos separados desde arriba.** Quien viene a certificar su
   experiencia no debe toparse con un formulario: necesita el botón de WhatsApp
   a la vista.
5. **Precio y qué incluye, sin sorpresas.** El costo de envío a provincia se
   calcula antes de confirmar, y decirlo tranquiliza.

## Prompt

```
Diseña la página de inicio de IPADECP, en español. Escritorio 1440 px y móvil
390 px. Catorce bloques, en este orden. Cada bloque con una composición DISTINTA:
no repitas la misma rejilla dos veces.

1. BARRA DE ANUNCIO, ancho completo, fondo con degradado #0b6683 a #063a4c,
texto blanco centrado de 13 px: un chip claro con "Nueva convocatoria" y al
lado "Cupos abiertos para el próximo periodo académico. Certificación oficial
IPADECP."

2. HEADER pegado, 68 px, fondo blanco translúcido con desenfoque, borde
inferior fino. Izquierda: emblema de IPADECP y la palabra IPADECP. Centro:
Cursos, Certificación, Nosotros, Contacto. Derecha: ícono de carrito, botón de
borde "Iniciar sesión" y botón navy con degradado "Crear cuenta". Todo en UNA
línea.

3. BANNER DE PORTADA. Un carrusel de imágenes de ancho completo, con una
proporción de 1600 por 500 en escritorio y de 1200 por 900 en móvil. La imagen
es una pieza gráfica completa: el texto de la campaña va DENTRO de la imagen, no
como capas de HTML encima. Dibújalo con una imagen de campaña de muestra.
Debajo de la imagen, centrados, unos puntos indicadores pequeños y circulares
(el activo en #10284d, los demás en gris claro) y un botón discreto de pausa.
En los laterales, dos botones circulares de flecha con fondo blanco al 86 %.
No pongas ningún texto ni etiqueta encima de la imagen.

4. HÉROE, división asimétrica 55/45, fondo #f4f7fa. Va JUSTO DEBAJO del banner:
el banner es la campaña del mes y cambia seguido, este héroe es el mensaje
permanente y es texto real.
Izquierda: una etiqueta pequeña en mayúsculas #0b6683 "CERTIFICACIÓN
VERIFICABLE"; titular en Hanken Grotesk 800 de dos líneas máximo: "Certifica tu
experiencia. Verifícala en segundos."; párrafo de máximo 20 palabras:
"Capacitación para personal de salud, 100 % virtual, con un certificado que
cualquiera puede comprobar con un QR."; dos botones: "Ver cursos" en degradado
navy y "Verificar certificado" con borde.
Derecha: una fotografía real, no ilustración, de una enfermera peruana joven
estudiando desde su celular, con uniforme, en un ambiente hospitalario
desenfocado. Esquinas de 16 px.
NO pongas nada más en el héroe: ni logos, ni frases sueltas debajo de los
botones, ni flechas de scroll.

5. FRANJA DE CONFIANZA, fondo blanco, cuatro cifras en una fila separadas por
líneas verticales finas #e1e8ed, SIN tarjetas. Números grandes en Hanken
Grotesk 800 y la etiqueta debajo en gris:
"Desde 2015" / "[N.º] alumnos certificados" / "[N.º] cursos en catálogo" /
"Todo el Perú". Deja los corchetes tal cual: son datos por confirmar.

6. VERIFICADOR EN VIVO. Banda de ancho completo con el degradado de marca
(#06142b a #10284d a #2f7593), texto blanco, con mucho respiro vertical.
Centrado: titular "Comprueba cualquier certificado IPADECP"; párrafo "Escanea
el QR o escribe el código. No necesitas cuenta ni contraseña."; y un campo de
búsqueda grande de fondo blanco con esquinas de 10 px, con la etiqueta encima
en blanco "Código corto o número de registro", el placeholder "IPD-4K7Q" en
tipografía monoespaciada, y pegado a la derecha un botón con degradado rojo
#c6111a a #8f0c12 que dice "Verificar certificado". Debajo del campo, en texto
blanco al 70 %: "También puedes escanear el QR impreso en el certificado."
Esta es la sección más importante de la página: dale peso visual.

7. DOS CAMINOS. Dos celdas asimétricas, 58 % y 42 %, esquinas de 16 px.
Izquierda, fondo blanco con borde: etiqueta "Quiero estudiar", titular "Lleva un
curso y certifícate al terminar", párrafo "Te registras, estudias los 6 módulos
a tu ritmo y el certificado se emite solo al llegar al 100 %.", botón con
degradado navy "Ver cursos". Una foto pequeña de apoyo.
Derecha, fondo con degradado #0b6683 a #307a99 y texto blanco: etiqueta "Ya
ejerzo", titular "Certifica la experiencia que ya tienes", párrafo "Escríbenos
por WhatsApp, te decimos qué curso corresponde a tu perfil y recibes tu
certificado físico en casa.", botón blanco "Escribir por WhatsApp".

8. CURSOS DESTACADOS. NO tres tarjetas iguales en fila. Un curso destacado
grande a la izquierda (con imagen alta, categoría, título, precio antes tachado
y precio ahora, y estrellas) y tres cursos apilados en columna a la derecha en
formato horizontal compacto (miniatura cuadrada, título, precio). En móvil, un
carrusel horizontal con desplazamiento por tarjeta. Encima, el titular "Los
cursos que más se llevan" y a la derecha un enlace "Ver los [N.º] cursos".

9. CÓMO FUNCIONA. Línea de tiempo horizontal de cuatro pasos unidos por una
línea fina #6cb3d3, sin tarjetas. Cada paso: un círculo con el número en
degradado navy, el título en Hanken Grotesk 700 y dos líneas de texto.
1 "Crea tu cuenta" / "Con tu DNI, para que tu certificado salga con tus nombres
exactos."
2 "Elige y paga" / "Con tarjeta entras al toque. Con Yape o transferencia,
mandas el comprobante por WhatsApp."
3 "Estudia sin horarios" / "Desde el celular, cuando puedas. El avance se
guarda solo."
4 "Recibe tu certificado" / "Se emite automático al 100 %, con tu QR listo para
descargar."
En móvil la línea de tiempo pasa a vertical.

10. QUÉ INCLUYE CADA CURSO. Rejilla bento de 5 celdas de tamaños distintos. Al
menos dos celdas con imagen real o fondo con degradado suave, no todas blancas
con texto.
- Celda ancha: "Material que te sirve después del curso" con "Te lo entregamos
  en Word y PowerPoint editables, a propósito: muchos alumnos salen del curso
  con el material listo para capacitar a su propio servicio."
- "6 módulos" / "Documento, diapositivas, videos, tarea y evaluación en cada
  uno."
- "Bibliografía fechada" / "Cada afirmación con su estudio, su año y dónde
  encontrarlo."
- "Sin horarios" / "No hay clases en vivo obligatorias."
- "Acceso de por vida" / "Vuelve al material cuando lo necesites."

11. EL CERTIFICADO QUE RECIBES. Dos columnas. Izquierda: fotografía de un
certificado impreso sobre un escritorio, con el código QR visible. Derecha:
titular "No se guarda en un cajón: se comprueba con un QR", párrafo explicando
que el certificado se genera en el momento desde los registros y no es un
archivo cargado, tres líneas con íconos (digital en PDF ilimitado, físico por
courier a todo el Perú, verificable por QR o código corto), y un recuadro con
fondo #fdf0f1 y borde izquierdo rojo: "Si un certificado se anula, la
verificación también lo dice. Eso es lo que protege el valor del tuyo."

12. TESTIMONIOS. Tres tarjetas de alto distinto, apoyadas en una rejilla
escalonada, NO alineadas. Cada una: foto circular de 56 px de una persona
peruana real de salud, comillas tipográficas, máximo tres líneas de texto,
nombre en Hanken Grotesk 700, y debajo profesión y ciudad en gris. Estrellas
doradas #ad8420 arriba.
[MUESTRA, reemplazar antes de publicar]
- "Lo llevé en las noches después del turno. El material en Word me sirvió para
  capacitar a mi propio servicio." Milagros Quispe Ccahuana, Enfermera,
  Huancayo.
- "Trabajo hace once años y no tenía nada que lo respaldara. El sobre me llegó a
  Juliaca en cinco días." Rosa Ccopa Mamani, Enfermera, Juliaca.
- "En el concurso escanearon el QR delante mío y salió al toque. Eso me
  tranquilizó." Elmer Huamán Vargas, Técnico de laboratorio, Trujillo.

13. PREGUNTAS FRECUENTES. Acordeón plegado a dos columnas en escritorio, seis
preguntas: "¿El certificado físico llega a provincia?", "¿Puedo verificar un
certificado sin tener cuenta?", "¿Necesito conectarme a una hora fija?", "¿De
dónde sale el contenido de los cursos?", "¿Puedo llevar varios cursos?",
"¿Puedo usar el material para capacitar a mi equipo?"

14. CIERRE. Banda de ancho completo con el degradado de marca, texto blanco
centrado: titular "Empieza hoy y certifícate desde donde estés", un botón
blanco "Ver cursos" y un enlace subrayado "Escribir por WhatsApp".

FOOTER de fondo #06142b: cuatro columnas (logotipo en blanco y una línea de
descripción, Cursos, Instituto, Legal), y una barra inferior con "IPADECP.
Instituto Peruano Americano de Desarrollo y Capacitación Profesional.", el
WhatsApp 992 951 855 y el correo educacion@ipadecp.com.pe.
```

---

# 3. Catálogo de cursos

## Criterio

El catálogo se navega con el pulgar. Los filtros tienen que estar arriba y
plegables, no en una columna lateral que en móvil desaparece. Y las tarjetas
deben decir el precio: obligar a entrar para ver el precio hace que la gente se
vaya.

## Prompt

```
Diseña la página de catálogo de cursos de IPADECP, en español. Escritorio y
móvil.

- Encabezado corto de fondo #f4f7fa: título "Cursos" en Hanken Grotesk 800,
  párrafo de una línea "Cursos de 6 módulos para personal de salud, 100 %
  virtuales y con certificado verificable." y a la derecha un campo de búsqueda
  con ícono de lupa.
- Barra de filtros pegada bajo el header: una fila horizontal de chips de
  categoría con esquinas de 8 px, desplazable en móvil. El chip activo va con
  degradado navy y texto blanco; los demás en blanco con borde #e1e8ed.
  Categorías: Todos, Enfermería, Emergencias, Laboratorio, Obstetricia, Salud
  pública, Farmacia. A la derecha un selector "Ordenar por: Más llevados".
- Bajo la barra, en texto chico gris: "[N.º] cursos" y los filtros activos como
  chips con una equis para quitarlos.
- Rejilla de tarjetas de curso: 3 columnas en escritorio, 2 en tablet, 1 en
  móvil. Cada tarjeta, esquinas de 16 px, fondo blanco, borde #e1e8ed:
  imagen 16:9 real; sobre la imagen NADA superpuesto; debajo, el chip de
  categoría, el título en Hanken Grotesk 700 a máximo dos líneas, una fila con
  "6 módulos · 120 horas", estrellas doradas con la nota, y al pie el precio
  antes tachado y el precio ahora grande, con un botón compacto con degradado
  navy "Ver curso".
  Al pasar el mouse, la tarjeta sube 2 px y la sombra crece.
- Estado vacío por si no hay resultados: un ícono grande en gris claro, "No
  encontramos cursos con esos filtros", "Prueba quitando algún filtro o
  escríbenos y te decimos qué curso te conviene." y un botón "Escribir por
  WhatsApp".
- Al final, paginación simple o un botón "Ver más cursos".
```

---

# 4. Verificación de certificado (pública)

## Criterio

Es la pantalla donde se juega toda la credibilidad de la marca. Quien llega
**no es un alumno**: es un empleador o una jefatura de personal que viene a
comprobar un dato y se va. Cero venta. La respuesta primero, los datos después.

## Prompt

```
Diseña la pantalla pública de verificación de certificado de IPADECP, en
español. Es la pantalla que ve un empleador después de escanear un código QR.
No intentes venderle nada.

ESTADO VÁLIDO
- Header mínimo: solo el logotipo de IPADECP centrado, sin navegación.
- Tarjeta centrada de máximo 620 px de ancho, fondo blanco, esquinas de 16 px,
  sombra media.
- Franja superior de la tarjeta con el degradado de marca (#06142b a #10284d a
  #2f7593): el logotipo de IPADECP en blanco a la izquierda, con 120 px de
  ancho, y a la derecha, en mayúsculas pequeñas, "VERIFICACIÓN DE CERTIFICADO".
- Dentro, lo primero: un chip con degradado verde #1c7a44 a #15703a, texto
  blanco, con un ícono de check: "Certificado vigente".
- Debajo, el nombre de la persona en Hanken Grotesk 800 de 26 px:
  "Milagros Quispe Ccahuana"
- Una línea gris: "Cuidados intensivos en el paciente crítico adulto. Curso de
  6 módulos completado el 12 de agosto de 2026."
- Un panel de fondo #f4f7fa con borde y esquinas de 8 px, con cuatro datos en
  dos columnas, las etiquetas en mayúsculas pequeñas grises y los valores en
  tipografía MONOESPACIADA con interletrado abierto:
  NÚMERO DE REGISTRO 000075 · CÓDIGO CORTO IPD-4K7Q · LIBRO 09000 ·
  FECHA DE EMISIÓN 01/09/2026
- Al pie, separado por una línea fina, una barra vertical de 4 px con el
  degradado rojo #c6111a a #8f0c12 y al lado, en texto chico:
  "Emitido por IPADECP. Generado desde nuestros registros en el momento de la
  consulta, no es un archivo cargado."
- Como marca de agua, el emblema de IPADECP al 4 % de opacidad al fondo de la
  tarjeta.
- Debajo de la tarjeta, fuera de ella, un enlace discreto: "Verificar otro
  certificado".

ESTADO ANULADO (segunda variante de la misma tarjeta)
- El chip pasa a fondo #b53232 con texto blanco: "Certificado anulado".
- Se agrega una fila al panel de datos: "FECHA DE ANULACIÓN 14/07/2026".
- El texto al pie cambia a: "Este certificado fue anulado y ya no es válido.
  Si necesitas confirmarlo, escríbenos por WhatsApp."

ESTADO NO ENCONTRADO (tercera variante)
- Tarjeta más corta, sin franja de color, con un ícono de interrogación gris.
- "No encontramos ningún certificado con ese código"
- "Revisa que lo hayas escrito completo, tal como aparece en el certificado.
  Si el problema sigue, escríbenos por WhatsApp."
- Un campo para reintentar y un botón "Verificar certificado".
```

---

# 5. Carrito

```
Diseña el carrito de IPADECP, en español. Panel lateral que entra desde la
derecha en escritorio (400 px de ancho) y ocupa toda la pantalla en móvil.

- Cabecera: "Tu carrito" en Hanken Grotesk 700 y una equis para cerrar.
- Cada curso en una fila: miniatura cuadrada de 64 px con esquinas de 8 px,
  título a dos líneas, precio, y debajo un botón de texto "Quitar" en gris.
  Entre filas, una línea fina, no tarjetas.
- Si hay descuento, el precio antes tachado en gris al lado del precio ahora.
- Al pie, pegado: subtotal, y si aplica una fila de descuento en verde
  #15703a, luego el total en Hanken Grotesk 800. Debajo un botón ancho completo
  con degradado navy "Ir a pagar" y un enlace centrado "Seguir viendo cursos".
- Texto chico gris bajo el botón: "El certificado físico es opcional y se pide
  después, desde tu cuenta."
- Estado vacío: ícono grande gris claro, "Tu carrito está vacío", "Cuando
  agregues un curso aparece acá.", botón "Ver cursos".
```

---

# 6. Checkout

```
Diseña el checkout de IPADECP, en español. Dos columnas en escritorio: el
formulario a la izquierda (60 %) y el resumen del pedido pegado a la derecha
(40 %). Una sola columna en móvil, con el resumen plegado arriba.

- Encabezado simple: logotipo centrado y, debajo, un indicador de tres pasos
  con la etapa actual marcada: Datos, Pago, Listo. Sin navegación completa: en
  el checkout no se sale de la página.
- Bloque "Tus datos": campos de DNI, nombres, apellidos, correo y celular. La
  ETIQUETA VA ARRIBA de cada campo, nunca dentro. Bordes #768495, esquinas de
  10 px. Bajo el campo de DNI, un texto de ayuda: "Validamos tu DNI en línea
  para que tu certificado salga con tus nombres exactos."
- Bloque "Cómo quieres pagar": tres opciones grandes seleccionables con radio,
  cada una una fila con borde que se marca en #2f7593 al elegirla:
  "Tarjeta de crédito o débito" con "Acceso inmediato al curso"
  "Yape" con "Nos envías el comprobante por WhatsApp y activamos tu curso"
  "Transferencia bancaria" con "Nos envías el comprobante por WhatsApp"
- Resumen pegado: lista de cursos, subtotal, descuento, total grande, y un
  botón ancho completo con degradado navy "Pagar S/ 149".
- Bajo el botón, tres líneas con íconos chicos: "Pago seguro",
  "Acceso de por vida", "Certificado verificable incluido".
- Muestra también el estado de error de un campo: borde #b53232 y el mensaje
  DEBAJO del campo, en #b53232: "No pudimos validar ese DNI en línea. Revisa
  que los 8 dígitos estén bien, o escríbenos por WhatsApp y lo vemos contigo."
```

---

# 7. Registro y 8. Inicio de sesión

```
Diseña las pantallas de crear cuenta e iniciar sesión de IPADECP, en español,
como dos variantes del mismo diseño.

Composición dividida: 45 % a la izquierda es una banda con el degradado de
marca (#06142b a #10284d a #2f7593) con el logotipo de IPADECP en blanco, un
titular y tres puntos de valor con íconos en #6cb3d3:
"Todos tus cursos en una sola cuenta"
"Tus certificados en PDF, para descargar cuando quieras"
"Con tu DNI, para que tus nombres salgan exactos"
El 55 % de la derecha es el formulario sobre fondo blanco, centrado
verticalmente, con máximo 420 px de ancho.

CREAR CUENTA: título "Crea tu cuenta", campos de DNI, nombres, apellidos,
correo, celular y contraseña, con la etiqueta arriba de cada uno. Texto de
ayuda bajo el DNI y bajo la contraseña ("Mínimo 8 caracteres"). Botón ancho
completo con degradado navy "Crear cuenta". Debajo, centrado: "¿Ya tienes
cuenta? Iniciar sesión."

INICIAR SESIÓN: título "Inicia sesión", campos de correo y contraseña, un
enlace "Olvidé mi contraseña" alineado a la derecha, botón "Iniciar sesión", y
debajo "¿Primera vez? Crear cuenta."
Agrega un tercer enlace discreto: "¿Te certificaste de forma directa? Activa tu
cuenta."

En móvil la banda del degradado se reduce a una franja superior de 180 px.
```

---

# 9. Activar cuenta

## Criterio

Esta pantalla la usa el perfil que **no estudió con nosotros**: recibió un sobre
con un código de 6 dígitos. Suele ser mayor y suele entrar desde el celular. El
campo del código tiene que ser enorme y evidente.

```
Diseña la pantalla "Activar mi cuenta" de IPADECP, en español. Es para quien
recibió su certificado físico con un volante que trae un código de 6 dígitos.

- Tarjeta centrada de 520 px sobre fondo #f4f7fa.
- Título "Activa tu cuenta" y párrafo de dos líneas: "Con el código de 6
  dígitos que vino en tu sobre. Es un trámite de dos minutos y se hace una sola
  vez."
- Campo de DNI con etiqueta arriba.
- Campo del CÓDIGO DE ACCESO: seis casillas separadas, cada una de 56 px, con
  tipografía monoespaciada grande y centrada, esquinas de 10 px, borde #768495
  que pasa a #2f7593 al enfocar.
- Botón ancho completo con degradado navy: "Activar mi cuenta".
- Debajo, un recuadro de fondo #f0f9fd con borde izquierdo de 4 px en #2f7593:
  "Al activar tu cuenta aparecen TODOS tus certificados, incluidos los de
  certificaciones anteriores."
- Un enlace al pie: "Perdí mi código. Escribir por WhatsApp."
- Diseña también el segundo paso: elegir correo y contraseña propios, con un
  recuadro de confirmación que muestre el correo escrito y pregunte "¿Está bien
  escrito?" antes de crear el acceso.
```

---

# 10. Aula, mis cursos

```
Diseña el aula del alumno de IPADECP, en español. Barra lateral fija de 225 px
con fondo navy #10284d, y el contenido a la derecha sobre #f4f7fa.

- Barra lateral: logotipo en blanco arriba, y enlaces con ícono: Mis cursos,
  Mis certificados, Certificado físico, Mi perfil. El activo con fondo
  #1c3d6b y esquinas de 10 px. Abajo del todo, el nombre del alumno con su
  avatar circular y "Cerrar sesión".
- Contenido: saludo "Hola, Milagros" en Hanken Grotesk 800 y debajo una línea
  gris "Tienes 2 cursos en progreso."
- "Continúa donde lo dejaste": una tarjeta ancha destacada con la imagen del
  curso a la izquierda, el nombre, el módulo actual, una barra de progreso
  delgada SIN pista de fondo rellena (solo la barra de avance en degradado
  navy sobre una línea fina gris), el porcentaje, y un botón "Continuar".
- "Mis cursos": rejilla de tarjetas con miniatura, título, barra de progreso y
  porcentaje. Las completadas llevan un chip verde #15703a "Completado" y un
  botón "Descargar certificado".
- Estado vacío: "Todavía no tienes cursos. Cuando compres uno, aparece acá y
  puedes empezar al toque." con un botón "Ver cursos".
```

---

# 11. Curso dentro del aula

```
Diseña la pantalla de un curso dentro del aula de IPADECP, en español. Tres
zonas: barra lateral de navegación del aula (igual que la anterior), un panel
de módulos plegable de 300 px, y el contenido de la lección al centro.

- Panel de módulos: acordeón de 6 módulos. Cada lección es una fila con un
  ícono de estado a la izquierda (círculo vacío, check verde #15703a si está
  hecha, o candado gris si está bloqueada), el nombre y la duración. La lección
  activa con fondo #e8eef6.
  Arriba del panel, el progreso del curso: "4 de 6 módulos" y una barra fina.
- Contenido: migas de pan del módulo, título de la lección en Hanken Grotesk
  700, el reproductor de video con esquinas de 16 px, y debajo tres pestañas
  con esquinas de 10 px: Material, Tarea, Evaluación.
  En "Material", una lista de descargas: cada archivo en una fila con su ícono
  de tipo (Word, PowerPoint, PDF), el nombre, el peso y un botón de descarga.
  Entre filas, línea fina.
- Al pie del contenido, dos botones de navegación: "Lección anterior" con borde
  y "Siguiente lección" con degradado navy.
- Diseña también el estado de módulo bloqueado: un recuadro centrado con un
  candado, "Termina el módulo 3 para desbloquear este" y la tarea que falta.
```

---

# 12. Mis certificados

```
Diseña la pantalla "Mis certificados" del aula de IPADECP, en español.

- Título "Mis certificados" y una línea gris "Descárgalos las veces que
  necesites."
- Cada certificado en una tarjeta ancha horizontal, esquinas de 16 px, fondo
  blanco: a la izquierda una miniatura del certificado en vertical; al centro,
  el nombre del curso en Hanken Grotesk 700, y debajo dos datos en tipografía
  monoespaciada: el número de registro y el código corto; a la derecha, un chip
  verde "Vigente" y dos botones apilados: "Descargar PDF" con degradado navy y
  "Ver verificación" con borde.
- Sobre la miniatura NO pongas ninguna etiqueta superpuesta.
- Bajo la lista, un recuadro de fondo #f0f9fd con borde izquierdo #2f7593:
  "¿Necesitas el certificado impreso? Pídelo desde Certificado físico y te lo
  enviamos por courier a cualquier parte del Perú. El costo depende del
  departamento y lo ves antes de confirmar."
- Estado vacío: "Todavía no tienes certificados. Al completar el 100 % de un
  curso, el certificado se emite solo y aparece acá."
```

---

# 13. Nosotros

```
Diseña la página "Nosotros" de IPADECP, en español.

- Héroe editorial: fondo con el degradado de marca, texto blanco centrado,
  titular "Capacitamos al personal de salud del Perú desde 2015" y un párrafo de
  dos líneas.
- Bloque de misión: dos columnas, a la izquierda una fotografía real de
  personal de salud peruano en un ambiente hospitalario, a la derecha el texto
  de la misión.
- Bloque de valores: rejilla bento de 5 celdas de tamaños distintos, una de
  ellas con el degradado navy y texto blanco. Valores: Verificable, Trazable,
  Sin trámite, Accesible, Útil después del certificado. Cada uno con una línea
  de "Se ve en:" al pie en #0b6683.
- Bloque "Lo que no somos": fondo #f4f7fa, cuatro afirmaciones cortas separadas
  por líneas finas, sin tarjetas: "No somos una universidad", "No vendemos un
  atajo", "No inflamos cifras", "No prometemos lo que el sistema no hace." Cada
  una con una línea de explicación.
- Cierre con el degradado de marca y un botón "Ver cursos".
```

---

# 14. Contacto

```
Diseña la página de contacto de IPADECP, en español. Dos columnas.

- Izquierda: formulario con etiquetas arriba de cada campo (nombre, celular,
  correo, curso de interés como selector, mensaje como área de texto). Botón
  con degradado verde de WhatsApp o navy: "Enviar por WhatsApp". Debajo, texto
  chico gris: "Al enviar, se abre WhatsApp con tu mensaje ya redactado: solo
  debes confirmarlo."
- Derecha: una tarjeta con fondo navy #10284d y texto blanco con los datos de
  contacto: WhatsApp 992 951 855, el correo, y el horario de atención. Cada
  dato en una fila con su ícono en #6cb3d3. Debajo, un texto en blanco al 60 %:
  "Te respondemos apenas veamos tu mensaje. La vía más rápida es WhatsApp."
- Bajo las dos columnas, un acordeón corto de preguntas frecuentes de contacto.
```

---

# 15. Páginas legales (un solo patrón para seis rutas)

Sirve igual para términos, privacidad, reembolso, cookies y reclamos.

```
Diseña una página de documento legal para IPADECP, en español. Diseño de
lectura, no de venta.

- Encabezado simple sobre #f4f7fa: título del documento en Hanken Grotesk 800 y
  debajo, en gris chico, "Última actualización: 2 de setiembre de 2026".
- Dos columnas: a la izquierda un índice pegado de 240 px con los enlaces a
  cada sección, el activo marcado con una barra de 3 px en #2f7593. A la
  derecha, el texto a un ancho máximo de 65 caracteres, con títulos de sección
  en Hanken Grotesk 700, párrafos en Inter de 16 px e interlineado de 1.7.
- En móvil el índice pasa a un desplegable arriba del texto.
- Al pie, un recuadro con fondo #f0f9fd y borde izquierdo #2f7593: "¿Alguna
  duda con este documento? Escríbenos por WhatsApp."
- Para la página de reclamos, en vez de texto, un formulario con las etiquetas
  arriba de los campos y el aviso legal del Libro de Reclamaciones.
```

---

# Fuera de alcance para Stitch

**El panel de administración** (`/admin` y sus subrutas) no debería diseñarse
con esta metodología. Es una interfaz densa de gestión: tablas, filtros,
emisión masiva de certificados y rótulos de envío. Stitch está hecho para
pantallas de producto y marketing, y lo que devuelve para un panel es una
maqueta bonita que no soporta la densidad real de datos. Ese panel ya funciona
con shadcn y conviene dejarlo así, aplicándole solo los tokens de marca.

---

# 16. El arte del banner de portada

No es una pantalla: es la **pieza gráfica** que se sube al panel y que cambia
cada vez que hay una campaña nueva. Se necesitan dos por campaña.

| Pieza | Medida exacta | Dónde se ve |
|---|---|---|
| Escritorio | **1600 × 500 px** | computadora y tablet |
| Móvil | **1200 × 900 px** | celular |

Si subes una sola, se usa en las dos. No lo hagas: un banner apaisado con texto
queda ilegible en un celular.

## Prompt para la pieza de escritorio

```
Diseña una pieza gráfica de banner web para IPADECP, de 1600 × 500 px
exactos, en español. Es la portada de una campaña, así que el texto va DENTRO
de la imagen.

Composición en tres zonas de izquierda a derecha:
- Izquierda (45 %): el mensaje. Una etiqueta pequeña en mayúsculas con fondo
  translúcido; debajo el titular en Hanken Grotesk 800 de 56 px, máximo dos
  líneas; debajo una línea de apoyo de 22 px; y abajo un botón dibujado con el
  degradado navy #10284d a #24608f, esquinas de 10 px, con el texto de acción.
- Centro-derecha (55 %): una fotografía real de personal de salud peruano, sin
  ilustración y sin gente genérica de banco de imágenes. La foto se funde hacia
  la izquierda con un degradado suave para que el texto se lea sin recuadros.
- El fondo general va con el degradado de marca #06142b a #10284d a #2f7593.
- El emblema de IPADECP en blanco, chico, en la esquina inferior derecha, con
  al menos 120 px de ancho.

Reglas: ningún texto por debajo de 32 px. Contraste mínimo de 4.5:1 entre el
texto y lo que tenga detrás. Nada de rayas largas. Nada de cuentas regresivas
ni "¡última oportunidad!". Deja 60 px de margen libre en todos los bordes.

Contenido de esta campaña:
Etiqueta: "NUEVA CONVOCATORIA"
Titular: "Certifícate en cuidados intensivos"
Apoyo: "6 módulos, 100 % virtual, con certificado verificable por QR."
Botón: "Ver el curso"
```

## Prompt para la pieza de móvil

```
La misma campaña de IPADECP en formato vertical de 1200 × 900 px exactos.

Composición apilada: la fotografía ocupa la mitad superior y se funde hacia
abajo con el degradado de marca; el texto va en la mitad inferior, centrado a
la izquierda con 70 px de margen.

Reglas: ningún texto por debajo de 40 px, porque esto se ve en un celular.
Titular en Hanken Grotesk 800 de 68 px, máximo tres líneas. El botón ocupa el
ancho del texto. Emblema de IPADECP en blanco arriba a la izquierda.

Mismo contenido que la pieza de escritorio.
```

## Checklist antes de subir un banner

- [ ] Las dos piezas, escritorio y móvil.
- [ ] Texto de 32 px o más en escritorio, 40 px o más en móvil.
- [ ] El `alt` escrito en el panel dice de qué es la campaña, no "banner".
- [ ] Si el banner lleva a algún lado, el enlace está puesto. Si no, se deja
      vacío y se pinta como imagen suelta, sin enlace muerto.
- [ ] Nada de cifras sin confirmar por el instituto.
- [ ] Cero rayas largas.
