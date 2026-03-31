const storageKey = `notas_usuario_${USUARIO_ID}`;
let notaEnEdicionId = null;

function obtenerNotas() {
    return JSON.parse(sessionStorage.getItem(storageKey)) || [];
}

function guardarNotas(notas) {
    sessionStorage.setItem(storageKey, JSON.stringify(notas));
}

function renderizarNotas() {
    const lista = document.getElementById("notas-lista");
    lista.innerHTML = "";

    const notas = obtenerNotas();

    if (notas.length === 0) {
        const li = document.createElement("li");
        li.className = "list-group-item text-muted text-center";
        li.textContent = "No hay notas aún";
        lista.appendChild(li);
        return;
    }

    notas.forEach((nota) => {
        const li = document.createElement("li");
        li.className =
            "list-group-item d-flex justify-content-between align-items-center";

        const texto = document.createElement("span");
        texto.textContent = nota.texto;

        const acciones = document.createElement("div");
        acciones.className = "btn-group btn-group-sm";

        const btnEditar = document.createElement("button");
        btnEditar.className = "btn btn-outline-secondary";
        btnEditar.innerHTML = "✏️";
        btnEditar.title = "Editar nota";
        btnEditar.onclick = () => editarNota(nota.id);

        const btnEliminar = document.createElement("button");
        btnEliminar.className = "btn btn-outline-danger";
        btnEliminar.innerHTML = "🗑️";
        btnEliminar.title = "Eliminar nota";
        btnEliminar.onclick = () => eliminarNota(nota.id);

        acciones.appendChild(btnEditar);
        acciones.appendChild(btnEliminar);

        li.appendChild(texto);
        li.appendChild(acciones);

        lista.appendChild(li);
    });
}

document.getElementById("nota-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const input = document.getElementById("nota-input");
    const texto = input.value.trim();
    if (!texto) return;

    let notas = obtenerNotas();
    const boton = document.querySelector("#nota-form button");

    if (notaEnEdicionId) {
        notas = notas.map(nota =>
            nota.id === notaEnEdicionId
                ? { ...nota, texto }
                : nota
        );
        notaEnEdicionId = null;
        boton.textContent = "Agregar";
        boton.classList.remove("btn-success");
        boton.classList.add("btn-primary");
    } else {
        notas.push({
            id: Date.now(),
            texto
        });
    }

    guardarNotas(notas);
    input.value = "";
    renderizarNotas();
});

function editarNota(id) {
    const notas = obtenerNotas();
    const nota = notas.find(n => n.id === id);
    if (!nota) return;

    const input = document.getElementById("nota-input");
    const boton = document.querySelector("#nota-form button");

    input.value = nota.texto;
    input.focus();
    notaEnEdicionId = id;

    boton.textContent = "Guardar";
    boton.classList.remove("btn-primary");
    boton.classList.add("btn-success");
}

function eliminarNota(id) {
    let notas = obtenerNotas();
    notas = notas.filter(nota => nota.id !== id);
    guardarNotas(notas);
    renderizarNotas();
}

document.addEventListener("DOMContentLoaded", renderizarNotas);

