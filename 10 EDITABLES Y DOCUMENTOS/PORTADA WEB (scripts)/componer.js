/*
 * Compone las dos piezas del banner de portada: la fotografía generada más el
 * texto de campaña, escrito con las tipografías reales de la marca.
 *
 * El texto NO lo escribe la IA a propósito. Un generador de imágenes comete
 * faltas de ortografía y no respeta la tipografía; acá el texto es HTML
 * rasterizado con Chrome, así que sale exacto.
 */
const fs = require('fs');
const { execFileSync } = require('child_process');
const sharp = require('sharp');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const RAIZ = 'A:/PROYECTOS/IPADECP';

// Campaña actual. Cambiar acá y volver a correr para hacer una pieza nueva.
const CAMPANA = {
  etiqueta: 'NUEVA CONVOCATORIA',
  titular: 'Certifícate en cuidados intensivos',
  apoyo: '6 módulos, 100 % virtual, con certificado verificable por QR.',
  boton: 'Ver el curso',
};

const b64 = f => fs.readFileSync(f).toString('base64');

function html({ foto, logo, ancho, alto, movil }) {
  const esc = !movil;
  return `<!doctype html><html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap">
<style>
*{margin:0;box-sizing:border-box}
body{width:${ancho}px;height:${alto}px;overflow:hidden;position:relative;font-family:Inter,sans-serif;background:#10284d}
.foto{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:${esc ? 'right center' : 'center top'}}
/* Velo: el texto se lee sobre foto solo si hay un degradado que baje la
   luminancia por debajo. En escritorio entra desde la izquierda, en móvil
   desde abajo, que es donde va el texto en cada formato. */
.velo{position:absolute;inset:0;background:${esc
    ? 'linear-gradient(90deg, rgba(6,20,43,.96) 0%, rgba(6,20,43,.90) 34%, rgba(6,20,43,.45) 56%, rgba(6,20,43,0) 74%)'
    : 'linear-gradient(180deg, rgba(6,20,43,0) 30%, rgba(6,20,43,.72) 50%, rgba(6,20,43,.96) 68%)'}}
.cont{position:absolute;${esc ? 'left:110px;top:50%;transform:translateY(-50%);width:46%' : 'left:70px;right:70px;bottom:150px'};z-index:2;color:#fff}
.etq{display:inline-block;font-size:${esc ? 22 : 30}px;font-weight:600;letter-spacing:.18em;
  background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);
  padding:${esc ? '10px 22px' : '14px 28px'};border-radius:8px;margin-bottom:${esc ? 28 : 40}px}
h1{font-family:'Hanken Grotesk',sans-serif;font-weight:800;letter-spacing:-.025em;
  font-size:${esc ? 78 : 92}px;line-height:1.04;margin-bottom:${esc ? 26 : 34}px}
p{font-size:${esc ? 28 : 36}px;line-height:1.5;color:rgba(255,255,255,.86);
  max-width:${esc ? '92%' : '100%'};margin-bottom:${esc ? 44 : 56}px}
.btn{display:inline-block;font-family:'Hanken Grotesk',sans-serif;font-weight:700;
  font-size:${esc ? 28 : 36}px;color:#fff;text-decoration:none;
  padding:${esc ? '22px 48px' : '28px 60px'};border-radius:10px;position:relative;
  background:linear-gradient(135deg,#10284d 0%,#24608f 100%);
  box-shadow:0 8px 24px rgba(6,20,43,.45)}
.btn::before{content:"";position:absolute;inset:0 0 auto 0;height:1px;background:rgba(255,255,255,.34);border-radius:10px 10px 0 0}
/* El logo solo se ve si cae sobre la zona que el velo oscurece: arriba a la
   izquierda en escritorio, y dentro del bloque de texto en móvil. Sobre la
   parte clara de la foto, un logo blanco desaparece. */
.logo{${esc ? 'position:absolute;left:110px;top:64px;width:200px;z-index:2' : 'display:block;width:230px;margin-bottom:34px'};opacity:.95}
</style></head><body>
<img class="foto" src="data:image/jpeg;base64,${foto}">
<div class="velo"></div>
${esc ? `<img class="logo" src="data:image/png;base64,${logo}">` : ''}
<div class="cont">
  ${esc ? '' : `<img class="logo" src="data:image/png;base64,${logo}">`}
  <div class="etq">${CAMPANA.etiqueta}</div>
  <h1>${CAMPANA.titular}</h1>
  <p>${CAMPANA.apoyo}</p>
  <span class="btn">${CAMPANA.boton}</span>
</div>
</body></html>`;
}

(async () => {
  const logo = b64('branding/logotipo/sin-fondo/logotipo-blanco-sin-fondo-800.png');
  const piezas = [
    { id: 'portada-escritorio', ancho: 1920, alto: 1080, movil: false },
    { id: 'portada-movil', ancho: 1080, alto: 1920, movil: true },
  ];
  for (const p of piezas) {
    const foto = b64(`.img/${p.id}.jpg`);
    const f = `.img/comp-${p.id}.html`;
    fs.writeFileSync(f, html({ foto, logo, ...p }));
    const salida = `${RAIZ}/.img/banner-${p.id}.png`;
    execFileSync(CHROME, ['--headless', '--disable-gpu', '--hide-scrollbars',
      `--window-size=${p.ancho},${p.alto}`, `--screenshot=${salida.replace(/\//g, '\\')}`,
      '--virtual-time-budget=9000', `file:///${RAIZ}/${f}`], { stdio: 'pipe' });
    const m = await sharp(salida).metadata();
    console.log(p.id, '->', m.width + 'x' + m.height, (fs.statSync(salida).size / 1024).toFixed(0) + 'KB');
  }
})();
