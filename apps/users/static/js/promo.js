document.getElementById('active-promo').addEventListener('click', function() {
    var formContainer = document.getElementById('promo');
    if (formContainer.classList.contains('active')) {
      
        formContainer.classList.remove('active');
    } else {
        formContainer.classList.add('active');
     
    }
});

document.getElementById('cancel-promo').addEventListener('click', function() {
    var formContainer = document.getElementById('promo');
    if (formContainer.classList.contains('active')) {
       
        formContainer.classList.remove('active');
    } else {
        formContainer.classList.add('active');
    
    }
});