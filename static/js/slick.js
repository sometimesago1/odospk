$(document).ready(function () {
    $('.slider__main-gallery').slick({
        arrows: true,
        infinite: true,
        slidesToShow: 1,
        autoplay: true,
        autoplaySpeed: 2400,
        speed: 1200,
    });
});

$(document).ready(function () {
    $('.directions__slider').slick({
        arrows: true,
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        speed: 1200,
    });
});