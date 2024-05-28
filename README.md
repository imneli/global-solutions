# Global Solution - Blue Future 🌊

## Nomes & RM's

<h2>

<li>RM 555499 - Matheus Montovaneli</li>
<li>RM 557789 - Thomaz Morais Neves </li>
<li>RM 555768 - Guilherme Linard </li>

# Responsive Website

<p>🇧🇷 | Usando HTML, CSS e Javascript!</p>
<p>🇺🇸 | Using HTML, CSS and Javascript!</p>


## Desktop Site

<img src="https://s7.ezgif.com/tmp/ezgif-7-60526bf0d9.gif">

## Mobile Site

<img src="https://s7.ezgif.com/tmp/ezgif-7-da5cc01f38.gif">


## Validação de Login - Web Development

<p>Usuário: admin</p>
<p>Senha: admin</p>

## `Código - Login`

```JS
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
```

Caso a Senha seja diferente da senha cadastrada no painel, irá dar um alert dizendo que a senha está incorreta, caso a senha esteja correta a validação de login é feita e aplica um alert dizendo que a senha está correta.

## `Código - Carrossel`

```JS

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
```

È aplicado um contador e um Intervalo para passar as imagens, ele muda o eixo X para trocar para próxima imagem utilizando o "translateX", criamos uma função chamada Slider para aplicar este contador e usamos o Transform para alterar as imagens.

<h2>🇧🇷 | Obrigado por ler até aqui!</h2>
<h2>🇺🇸 | Thank you for reading this far!</h2>