const presentation = document.getElementById('apresentacao');
const slides = Array.from(presentation.querySelectorAll('.slide-card'));
const links = presentation.querySelectorAll('.slide-index a');
let slideAtual = slides[0];

function mostrarSlide(focar = false) {
  const destino = slides.find((slide) => '#' + slide.id === location.hash);
  slideAtual = destino || (location.hash ? slideAtual : slides[0]);
  for (const slide of slides) {
    slide.hidden = slide !== slideAtual;
  }
  for (const link of links) {
    if (link.hash === '#' + slideAtual.id) {
      link.setAttribute('aria-current', 'true');
    } else {
      link.removeAttribute('aria-current');
    }
  }
  if (focar && destino) {
    destino.querySelector('h2').focus();
  }
}

mostrarSlide(Boolean(location.hash));
window.addEventListener('hashchange', () => mostrarSlide(true));
