const user = 'admin';
const passw = 'admin';

let botao = document.getElementById('btnLogar')

botao.addEventListener('click', function logar(){

    let pegaUsuario = document.getElementById('input-user').value
    let pegaSenha = document.getElementById('input-password').value

    if(pegaUsuario === user && pegaSenha === passw){
        alert('Senha válida!')
        document.querySelector('.display_none').style.display = "none";
        document.querySelector('.display_none_p').style.display = "none";
        document.getElementById('add_h1').innerHTML = '<h1>Você logou com sucesso!</h1>';
        document.getElementById('add_h1').style.textAlign = "center"
    } else {
        alert('Senha Invalida!')
    }


})


// carrossel

const box = document.querySelector(".container");
const imagens = document.querySelectorAll(".container img");

let contador = 0;

function slider() {
  contador++;

  if (contador > imagens.length - 1) {
    contador = 0;
  }

  box.style.transform = `translateX(${-contador * 300}px)`;
}

setInterval(slider, 2000);

