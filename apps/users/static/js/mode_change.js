document.addEventListener('DOMContentLoaded', function() {
    var sunIcon = document.getElementById('sun-icon');
    var moonIcon = document.getElementById('moon-icon');
    var currentTheme = localStorage.getItem('theme') || 'light';

    // Inicialmente, establece el icono correcto basado en el tema actual
    if (currentTheme === 'dark') {
        document.body.classList.add('light-mode');
        moonIcon.style.display = 'none'; // Oculta el icono de la luna
        sunIcon.style.display = 'flex'; // Muestra el icono del sol
    } else {
        document.body.classList.remove('light-mode');
        moonIcon.style.display = 'flex'; // Muestra el icono de la luna
        sunIcon.style.display = 'none'; // Oculta el icono del sol
    }

    // Función para cambiar el icono de sol a luna y viceversa
    function toggleIcons(isDarkMode) {
        if (isDarkMode) {
            moonIcon.style.display = 'none'; // Oculta el icono de la luna
            sunIcon.style.display = 'flex'; // Muestra el icono del sol
        } else {
            moonIcon.style.display = 'flex'; // Muestra el icono de la luna
            sunIcon.style.display = 'none'; // Oculta el icono del sol
        }
    }

    // Evento click para el SVG del sol
    sunIcon.addEventListener('click', function() {
        document.body.classList.remove('light-mode');
        localStorage.setItem('theme', 'light');
        toggleIcons(false);
    });

    // Evento click para el SVG de la luna
    moonIcon.addEventListener('click', function() {
        document.body.classList.add('light-mode');
        localStorage.setItem('theme', 'dark');
        toggleIcons(true);
    });
});

