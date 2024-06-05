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

<img src="/assets/img/GIFMaker_me.gif">

## Mobile Site

<img src="/assets/img/GIF_CELL.gif">


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
        document.querySelector('.display_none').style.display = "none";
        document.querySelector('.display_none_p').style.display = "none";
        document.getElementById('add_h1').innerHTML = '<h1>Você logou com sucesso!</h1>';
        document.getElementById('add_h1').style.textAlign = "center"
    } else {
        alert('Senha Invalida!')
    }


})
```

Caso a Senha seja diferente da senha cadastrada no painel, irá dar um `alert` dizendo que a senha está incorreta, caso a senha esteja correta a validação de login é feita e aplica um `alert` dizendo que a senha está correta. Após isso usamos o DOM para alterar o Display da página e fazer com que as tags `</p> & </input>` sejam removidas e assim adicionado uma tag `</h1>` falando que o Login foi realizado.

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

É aplicado um contador e um Intervalo para passar as imagens, ele muda o eixo X para trocar para próxima imagem utilizando o `"translateX"`, criamos uma função chamada `Slider` para aplicar este contador e usamos o `Transform` para alterar as imagens.

## Soluções / Tecnologias

`Oceans 20` propõe uma abordagem multifacetada para lidar com a poluição dos oceanos:

### 1. Sistema de Monitoramento Contínuo

Implementação de um sistema de monitoramento contínuo da temperatura e elevação dos oceanos em pontos estratégicos. Utilizaremos tecnologias avançadas de sensoriamento remoto e estações de coleta de dados para identificar os países que mais contribuem para a poluição dos oceanos.

### 2. Website Interativo

Desenvolvimento de um website interativo dedicado à conscientização sobre a poluição dos oceanos e ao monitoramento contínuo dos dados coletados. Este website será uma plataforma central para divulgar informações relevantes, notícias sobre preservação marinha e iniciativas de combate à poluição dos oceanos.

### 3. Sistema de Previsão de Dados

Desenvolvimento de um sistema de previsão de dados utilizando a linguagem de programação Python. Este sistema integrará os dados coletados pelo sistema de monitoramento com modelos de análise de dados e algoritmos de aprendizado de máquina para prever tendências futuras na poluição dos oceanos, variações climáticas e impactos ambientais.



## Objetivos

<li>Monitorar continuamente os parâmetros ambientais dos oceanos.</li>
<li>Disponibilizar dados de monitoramento em tempo real para acesso público.</li>
<li>Prever tendências futuras na poluição dos oceanos e impactos ambientais.</li>
<li>Apoiar tomadores de decisão e organizações ambientais com informações atualizadas.</li>

## Benefícios

<li>Aumento da conscientização pública sobre a importância da preservação dos oceanos.</li>
<li>Melhor compreensão das causas e efeitos da poluição dos oceanos.</li>
<li>Capacidade aprimorada de resposta a desastres naturais relacionados aos oceanos.</li>
<li>Facilitação da colaboração entre pesquisadores, organizações ambientais e governos.</li>

## Agradecimentos!

### 🇧🇷 | Obrigado por ler até aqui!

### 🇺🇸 | Thank you for reading this far!

## License

Este projeto é licenciado sob a <strong>[Licença MIT](LICENSE).</strong>