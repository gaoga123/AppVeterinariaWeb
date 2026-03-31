$("#id_imagen").on("change", function(e){

const file = e.target.files[0];

if(file){

const url = URL.createObjectURL(file);

$("#previewMascota")
.attr("src", url)
.fadeIn();

}

});

// gsap.from(".card-form-mascota",{
//     opacity:0,
//     y:50,
//     duration:0.8,
//     ease:"power3.out"
// });