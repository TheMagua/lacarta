let enlacesInternos = document.querySelectorAll('a[href^="#"]');
          // Itera sobre cada enlace
          enlacesInternos.forEach(function(enlace) {
            // Agrega un listener para el evento click
            enlace.addEventListener('click', function(event) {
              // Evita el comportamiento predeterminado
              event.preventDefault();

              // Obtiene el destino del hash del enlace
              let destino = document.querySelector(this.getAttribute('href'));

              // Desplaza suavemente hasta el destino
              if (destino) {
                destino.scrollIntoView({
                  behavior: 'smooth'
                });
              }
            });
          });