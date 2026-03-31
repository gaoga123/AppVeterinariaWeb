gsap.registerPlugin(ScrollTrigger);

gsap.from("header .eslogan h1", {
    y: -50,
    opacity: 0,
    duration: 1,
    ease: "power3.out"
});

gsap.from(".seccion-mascotas", {
    scrollTrigger: {
        trigger: ".seccion-mascotas",
        start: "top 80%",
        toggleActions: "play reverse play reverse"
    },
    y: 60,
    opacity: 0,
    duration: 1
});

gsap.from(".seccion-frase h4", {
    scrollTrigger: {
        trigger: ".seccion-frase",
        start: "top 85%",
        toggleActions: "play reverse play reverse"
    },
    scale: 0.9,
    opacity: 0,
    duration: 0.8,
    ease: "power2.out"
});


gsap.from(".seccion-resenias", {
    scrollTrigger: {
        trigger: ".seccion-resenias",
        start: "top 80%",
        toggleActions: "play reverse play reverse"
    },
    y: 80,
    opacity: 0,
    duration: 1
});

gsap.from(".seccion-turno .btn-turno", {
    scrollTrigger: {
        trigger: ".seccion-turno",
        start: "top 90%",
        toggleActions: "play reverse play reverse"
    },
    scale: 0.8,
    opacity: 0,
    duration: 0.6,
    ease: "back.out(1.7)"
});

gsap.from(".anim-resenia", {
    scrollTrigger: {
        trigger: ".seccion-resenias",
        start: "top 80%",
        toggleActions: "play reverse play reverse"
    },
    opacity: 0,
    y: 40,
    duration: 0.6,
    stagger: 0.2
});

$(document).ready(function(){

    $("#carouselMascotas").carousel({
        interval: 4000,   
        ride: "carousel",
        pause: "hover",
        wrap: true
    });

    $("#carouselResenias").carousel({
        interval: 4000,   
        ride: "carousel",
        pause: "hover",
        wrap: true
    });

});

gsap.utils.toArray(".imagen-carrusel").forEach(img => {

    gsap.to(img, {
        scale: 1.1,
        duration: 8,
        ease: "none",
        repeat: -1,
        yoyo: true
    });

});