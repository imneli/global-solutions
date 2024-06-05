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


## Validações - Web Development


## `Código - Validate Form`

```JS

class ValidateForm {
    constructor() {
      this.formulario = document.querySelector('.formulario');
      this.eventos();
    }
  
    eventos() {
      this.formulario.addEventListener('submit', e => {
        this.handleSubmit(e);
      });
    }
  
    handleSubmit(e) {
      e.preventDefault();
      const validFields = this.isValid();

      if(validFields) {
        alert('Formulário enviado.');
        this.formulario.submit();
      }
    }
  
    isValid() {
      let valid = true;
      return valid;
    }
  
    validaUsuario(campo) {
      let valid = true;
      return valid;
    }
  }
  
  const validate = new ValidateForm();

```

### 1. Construtor:

Quando uma instância de `ValidateForm` é criada, ela seleciona o elemento do formulário com o nome de classe `.formulario` no documento HTML e configura os ouvintes de eventos.

### 2. Manipulação de Eventos: 

O método `eventos()` adiciona um ouvinte de evento ao evento de envio do formulário. Quando o formulário é enviado, ele chama o método `handleSubmit()`.

### 3. Tratamento do Envio do Formulário:

No método `handleSubmit()`, ele impede o comportamento padrão de envio do formulário usando `e.preventDefault()`. Em seguida, chama o método `isValid()` para verificar se os campos do formulário são válidos. Se forem, exibe uma mensagem de alerta informando que o formulário foi enviado e envia o formulário programaticamente.

### 4. Tratamento do Envio do Formulário:

 O método `isValid()` atualmente retorna `true` por padrão, indicando que todos os campos do formulário são válidos. Este método normalmente conteria lógica de validação para cada campo do formulário, retornando `false` se algum campo não passar na validação.

### 5. Validação Individual dos Campos:

O método `validaUsuario()` está definido, mas não utilizado neste código. Parece ser destinado a validar campos individuais dentro do formulário, mas atualmente retorna `true` por padrão.

### 6. Inicialização:

Por fim, uma instância de `ValidateForm` é criada, o que inicia o processo de validação para o formulário no documento `HTML`.






## `Código - Login`

<p>Usuário: admin</p>
<p>Senha: admin</p>

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