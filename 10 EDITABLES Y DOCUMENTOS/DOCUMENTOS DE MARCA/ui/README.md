# branding/ui/

Todo lo necesario para generar la interfaz del sitio en **Google Stitch** sin
que cada pantalla salga con otra paleta y otro criterio.

## Los tres archivos

| Archivo | Qué es |
|---|---|
| **`sistema-para-stitch.md`** | El preámbulo. Va pegado **al inicio de cada prompt**. Sin él, Stitch inventa su propia paleta. |
| **`prompts-stitch.md`** | Un prompt por pantalla, listo para copiar y pegar. 16 pantallas más el arte del banner. |
| **`ui-spec.json`** | El mismo mapa en formato legible por máquina: páginas, secciones, familia de composición e intención. Para agentes y herramientas. |

## Cómo se usa

1. Abre Stitch y crea un proyecto.
2. Copia el **bloque de sistema** de `sistema-para-stitch.md`.
3. Pégalo, y debajo pega el prompt de la pantalla que quieras.
4. Genera. Corrige con las frases de rescate que están al final del preámbulo.
5. Repite por pantalla. **Stitch no recuerda entre generaciones:** el preámbulo
   se pega cada vez.

**Empieza por la ficha de curso.** Es la que vende, la más compleja y la que
fija el lenguaje visual. Cuando esa queda, las demás salen consistentes. Está
revisada contra la página real de Coderhouse, con las cuatro diferencias que
no se pueden copiar porque el producto no es el mismo.

## Las páginas

**Prioridad 1, las que venden**
Ficha de curso (la página de producto) · Inicio · Catálogo · Verificación de
certificado

**Prioridad 2, las que convierten**
Carrito · Checkout · Registro · Iniciar sesión · Activar cuenta · Nosotros ·
Contacto

**Prioridad 3, el producto**
Aula y mis cursos · Curso dentro del aula · Mis certificados

**Prioridad 4, un solo patrón**
Términos, privacidad, reembolso, cookies y reclamos

**Fuera de alcance: el panel de administración.** Es una interfaz densa de
gestión (tablas, filtros, emisión masiva, rótulos de envío). Stitch está hecho
para pantallas de producto y marketing; para un panel devuelve una maqueta
bonita que no soporta la densidad real de datos. Ya funciona con shadcn y
conviene dejarlo así, aplicándole solo los tokens de marca.

---

## El criterio detrás de todo esto

No es una landing de software. Le habla a alguien que trabaja por turnos, entra
desde el celular y necesita un papel que le sirva en un concurso o un legajo.

**Lo que más mueve a esta audiencia, en orden:**

1. **El verificador en vivo en la propia portada.** Es la recomendación más
   fuerte del documento. En vez de *decir* que el certificado se comprueba,
   poner el campo ahí mismo para que cualquiera lo pruebe en tres segundos.
   Nadie en el sector lo hace y la página de verificación ya existe.
2. **Mostrar el certificado.** Están comprando un papel: hay que enseñarlo.
3. **Testimonios de pares.** Profesión y ciudad al lado del nombre. "Enfermera,
   Huancayo" convence más que cualquier titular.
4. **Precio y qué incluye, sin sorpresas.**
5. **Los dos caminos separados desde arriba.** Quien viene a certificar su
   experiencia no debe toparse con un formulario.
6. **Sin horarios, desde el celular, el avance se guarda solo.**

## Sobre el contenido de muestra

Los testimonios, nombres y cifras de los prompts están marcados con
`[MUESTRA]`. Sirven para que Stitch dibuje la pantalla con contenido creíble.
**Antes de publicar hay que reemplazarlos por testimonios y cifras reales.**
Las fotos de los avatares sí existen, en `public/img/avatares/`.

Las cifras que el instituto todavía no confirmó van entre `[corchetes]` a
propósito, para que se vean y no se publiquen por descuido.

## La portada es una imagen, y ya está construida

`BannerPortada` es un carrusel de imágenes que abre la home, con el texto DENTRO
de la imagen, gestionado desde el panel. Cambias la campaña subiendo otra
imagen, sin deploy.

| Pieza | Medida |
|---|---|
| Escritorio | **1600 × 500 px** |
| Móvil | **1200 × 900 px** |

Debajo del banner va `HeroInicio`, que es el mensaje permanente en **texto
real**. Esa separación importa: el texto dentro de una imagen no lo lee Google
ni un lector de pantalla. Con las dos piezas tienes la promoción que se cambia
en 30 segundos y el mensaje que posiciona en buscadores.

El prompt para generar el arte de cada banner está al final de
`prompts-stitch.md`.
