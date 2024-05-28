const user = 'admin';
const passw = 'admin';

let botao = document.getElementById('btnLogar')

botao.addEventListener('click', function logar(){

    let pegaUsuario = document.getElementById('input-user').value
    let pegaSenha = document.getElementById('input-password').value

    if(pegaUsuario === user && pegaSenha === passw){
        alert('Senha válida!')
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

