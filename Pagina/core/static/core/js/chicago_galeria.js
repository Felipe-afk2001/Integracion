    //scrip busqueda por id
    //https://api.artic.edu/api/v1/artworks/artworks/{id}
    //https://api.artic.edu/api/v1/artworks/27992?fields=id,title,image_id


    var url = "https://www.artic.edu/iiif/2/";

    var urlficha = 'https://www.artic.edu/artworks/'

    //https://www.artic.edu/iiif/2/{id}/
    //https://www.artic.edu/artworks/656/lion-one-of-a-pair-south-pedestal
    // /full/843,/0/default.jpg

    $(document).ready(function () {


      $("#btnBusca").click(function () {
        $("#ContenedorCartas").empty();



        var quearyBusqueda = document.getElementById('quearyBusqueda').value
        //console.log(quearyBusqueda);
        //https://api.artic.edu/api/v1/artworks/search?q=cats&query[term][is_public_domain]=true

        $.get(`https://api.artic.edu/api/v1/artworks/search?q=${quearyBusqueda}`, function (data) {

          console.log(data.data);
          $.each(data.data, function (i, item) {
            var urlApiLink = item.api_link;
            console.log(urlApiLink);

            $.get(`${urlApiLink}`, function (data) {
              //console.log(data.data.id);
              var urlImagen = url.concat(data.data.image_id, '/full/843,/0/default.jpg');
              //console.log(urlImagen);
              console.log('https://www.artic.edu/artworks/' + item.id)


              var carta = `<div class="card my-3 mx-2" style="width: 18rem;">
                                    <img src="${urlImagen}" class="card-img-top" alt="${item.title}">
                                    <div class="card-body">
                                    <h5 class="card-title">${item.title}</h5>
                                    <p class="card-text">${item.thumbnail.alt_text}</p>
                                    <a href=${urlficha}${item.id}> ir a pagina</a>                              
                                    </div>
                                    </div>`
              $("#ContenedorCartas").append(carta);
            })

          })

        })

      })

    })