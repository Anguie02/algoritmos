document.addEventListener('DOMContentLoaded', function () {
    const asistenteContainer = document.getElementById('asistente-container');
    const asistenteInput = document.getElementById('asistente-input');
    const asistenteMessages = document.getElementById('asistente-messages');

    // Función para enviar mensajes al servidor
    function enviarMensajeAsistente() {
      const mensajeUsuario = asistenteInput.value.trim();
      if (mensajeUsuario !== '') {
        // Enviar mensaje al servidor
        fetch('/enviar_mensaje', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: `mensaje_usuario=${encodeURIComponent(mensajeUsuario)}`,
        })
        .then(response => response.json())
        .then(data => {
          // Mostrar la respuesta del asistente
          asistenteMessages.innerHTML += `<p>Asistente: ${data.respuesta_asistente}</p>`;
          // Limpiar el campo de entrada
          asistenteInput.value = '';
        });
      }
    }

    // Evento para enviar mensajes cuando se presiona Enter
    asistenteInput.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') {
        enviarMensajeAsistente();
      }
    });
  });