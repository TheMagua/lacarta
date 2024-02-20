window.onload = function() {
    setTimeout(function() {
        if (localStorage.getItem('promo')=== null) {
            // Añadir la clase 'active' al elemento con el ID 'promo'
            var promoElement = document.getElementById('promo');
            if (promoElement) {
              promoElement.classList.add('active');
              // Crear la variable 'promo' en localStorage
              localStorage.setItem('promo', 'true');
            }
            
            
        }
    },  10000);

    setInterval(function() {
        localStorage.removeItem('promo');
    },  5 *  60 *  1000); //  5 minutos en milisegundos
    
    
    setTimeout(function() {
        var alertElement = document.getElementById('promo-alert');
        if (alertElement) {
            localStorage.setItem('promo', 'true');
            alertElement.style.display = 'none';
            
        }
    },  3000); //  2000 milisegundos son  2 segundos
  };

