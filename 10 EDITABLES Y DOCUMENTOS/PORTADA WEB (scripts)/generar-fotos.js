/*
 * Genera las fotografías de la portada con Gemini.
 * Van SIN TEXTO a propósito: el texto se compone después con las tipografías
 * reales de la marca, que es la única forma de garantizar que no salga con
 * faltas de ortografía ni con una tipografía que no es la nuestra.
 */
const fs = require('fs');
const K = process.env.GEMINI_API_KEY;
if (!K) { console.error('Falta GEMINI_API_KEY'); process.exit(1); }

const MODELO = 'gemini-3-pro-image';
const SIN_TEXTO = ' Sin ningún texto, letra, número, logotipo ni marca de agua en la imagen.';
const ESTILO = ' Fotografía realista, no ilustración. Luz natural suave, colores fieles, profundidad de campo. Personal de salud peruano, rasgos latinoamericanos, edades y contexturas variadas.';

const PIEZAS = [
  { id: 'portada-escritorio', ratio: '16:9', size: '2K',
    p: 'Enfermera peruana de unos 30 años, con uniforme azul de hospital, mirando su celular con una sonrisa tranquila mientras camina por el pasillo luminoso de un hospital moderno. Encuadre horizontal amplio. La persona está a la DERECHA del encuadre y toda la mitad IZQUIERDA queda despejada y desenfocada, para poder colocar texto encima.' },
  { id: 'portada-movil', ratio: '9:16', size: '2K',
    p: 'Enfermera peruana de unos 30 años, con uniforme azul de hospital, mirando su celular con una sonrisa tranquila, en el pasillo luminoso de un hospital moderno. Encuadre vertical. La persona ocupa la mitad SUPERIOR del encuadre y la mitad INFERIOR queda despejada y desenfocada, para poder colocar texto encima.' },
  { id: 'hero', ratio: '4:3', size: '2K',
    p: 'Técnica de enfermería peruana estudiando desde su celular, sentada en la sala de descanso de un hospital, con una taza de café al lado. Ambiente cálido y real, no de banco de imágenes. Se le ve concentrada y cómoda.' },
  { id: 'certificado', ratio: '4:3', size: '2K',
    p: 'Primer plano cenital de un certificado impreso de aspecto formal sobre un escritorio de madera clara, junto a un lapicero y unos lentes. En la esquina inferior derecha del certificado se ve claramente un código QR cuadrado, nítido y bien contrastado. El resto del certificado se ve elegante pero sin que se lean las letras.' },
  { id: 'camino-estudiar', ratio: '3:2', size: '1K',
    p: 'Estudiante peruana de enfermería, joven, con uniforme blanco, tomando apuntes frente a una laptop en una mesa junto a una ventana. Ambiente de casa, luz de tarde.' },
  { id: 'camino-certificar', ratio: '3:2', size: '1K',
    p: 'Enfermero peruano con varios años de experiencia, unos 45 años, con uniforme azul, de pie en la estación de enfermería de un hospital, mirando a cámara con expresión serena y segura.' },
];

async function generar(pieza) {
  const cuerpo = {
    contents: [{ parts: [{ text: pieza.p + ESTILO + SIN_TEXTO }] }],
    generationConfig: { responseModalities: ['IMAGE'], imageConfig: { aspectRatio: pieza.ratio, imageSize: pieza.size } },
  };
  for (let i = 0; i < 3; i++) {
    try {
      const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODELO}:generateContent?key=${K}`, {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(cuerpo),
      });
      const j = await r.json();
      if (j.error) throw new Error(j.error.message.slice(0, 150));
      const img = (j.candidates?.[0]?.content?.parts || []).find(p => p.inlineData);
      if (!img) throw new Error('la respuesta no trae imagen');
      const buf = Buffer.from(img.inlineData.data, 'base64');
      fs.writeFileSync(`.img/${pieza.id}.jpg`, buf);
      return buf.length;
    } catch (e) {
      console.log(`   intento ${i + 1} falló: ${e.message}`);
      if (i === 2) throw e;
      await new Promise(x => setTimeout(x, 5000));
    }
  }
}

(async () => {
  const sharp = require('sharp');
  for (const p of PIEZAS) {
    if (fs.existsSync(`.img/${p.id}.jpg`)) { console.log('SALTO', p.id); continue; }
    console.log('==>', p.id, p.ratio, p.size);
    try {
      await generar(p);
      const m = await sharp(`.img/${p.id}.jpg`).metadata();
      console.log('   OK', m.width + 'x' + m.height, (fs.statSync(`.img/${p.id}.jpg`).size / 1024).toFixed(0) + 'KB');
    } catch (e) { console.log('   FALLO', e.message); }
  }
  console.log('=== FIN ===');
})();
