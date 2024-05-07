function add_material(){

    container = document.getElementById("form-material")

    html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='Tipo Material' class='form-control' name='tipo_material'></div>"
    html += "<div class='col-md'><input type='text' placeholder='Unidade' class='form-control'name='unidade_material'></div>"
    html += "<div class='col-md'><input type='number' placeholder='Quantidade' class='form-control' name='quantidade'></div>"

    container.innerHTML += html


}