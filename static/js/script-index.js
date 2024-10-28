$( document ).ready(function() {
    // Quando o modal for fechado
    $(document).on('click','.close', function () {
        // Scroll até o formulário
        $('html, body').animate({
            scrollTop: $("#text-copy-lp").offset().top
        }, 500); // Tempo em milissegundos para o scroll (0.5 segundo)
    });

});