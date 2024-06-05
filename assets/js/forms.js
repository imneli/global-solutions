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
  