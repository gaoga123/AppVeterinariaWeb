$(document).ready(function () {
    $("header").hide().fadeIn(1200);
});

$(".btn-opcion, .btn-turno").hover(
    function () {
        $(this).animate({ opacity: 0.85 }, 200);
    },
    function () {
        $(this).animate({ opacity: 1 }, 200);
    }
);

$(window).on("scroll", function () {
    $(".container").each(function () {
        let top = $(this).offset().top;
        let scroll = $(window).scrollTop();
        let windowHeight = $(window).height();

        if (scroll + windowHeight - 100 > top) {
            $(this).animate({ opacity: 1, top: 0 }, 700);
        }
    });
});

$(".opcion-header").on("click", function () {
    $(".opcion-header").removeClass("active");
    $(this).addClass("active");
});
