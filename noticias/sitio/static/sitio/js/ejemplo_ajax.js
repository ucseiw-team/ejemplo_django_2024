function actualizar_titulo() {
    console.log("Haciendo request para actualizar...");

    $.ajax({
        type: "GET",
        url: "/api/ultimo_titulo/",
        success: actualizar_titulo_en_html,
    });
}

function actualizar_titulo_en_html(data) {
    console.log("Llegó la data!");

    $('#ultima_noticia').html(data.titulo_ultima_noticia);
}

function on_page_load() {
    $("#boton_actualizar_noticia").on("click", actualizar_titulo);

    setInterval(actualizar_titulo, 5000);
}

$(on_page_load);
