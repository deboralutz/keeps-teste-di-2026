const panorama = document.querySelector('video');

function mostrarAlternativa() {
  document.getElementById('media-error').hidden = false;
  document.getElementById('panorama-texto').open = true;
}

panorama.addEventListener('error', mostrarAlternativa);
panorama.querySelector('source').addEventListener('error', mostrarAlternativa);

window.addEventListener("load", () => {
  if (panorama.error || panorama.networkState === HTMLMediaElement.NETWORK_NO_SOURCE) {
    mostrarAlternativa();
  }
});
