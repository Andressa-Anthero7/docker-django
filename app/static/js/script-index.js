$(document).on('click', '.close', function () {
    $('body').css('overflow', 'auto');
    $('html, body').animate({
        scrollTop: $("#text-copy-lp").offset().top
    }, 500);
});
