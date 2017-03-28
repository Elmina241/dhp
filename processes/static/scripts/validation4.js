function CustomValidation() { }

CustomValidation.prototype = {
  // Установим пустой массив сообщений об ошибках
  invalidities: [],

  // Метод, проверяющий валидность
  checkValidity: function(input) {

    var validity = input.validity;

    if (validity.rangeOverflow) {
      var max = input.getAttribute('max');
      this.addInvalidity('Максимальное возможное значение: ' + max);
    }

    if (validity.rangeUnderflow) {
      var min = input.getAttribute('min');
      this.addInvalidity('Минимальное возможное значение: ' + min);
    }

    if (validity.valueMissing) {
      this.addInvalidity('Обязательное поле');
    }
  },

  // Добавляем сообщение об ошибке в массив ошибок
  addInvalidity: function(message) {
    this.invalidities.push(message);
  },

  // Получаем общий текст сообщений об ошибках
  getInvalidities: function() {
    return this.invalidities.join('. \n');
  },

  clearInvalidities: function() {
    return this.invalidities = [];
  }
};

function addValidation(){
  var submit = document.getElementById("send");
  // Добавляем обработчик клика на кнопку отправки формы
  submit.addEventListener('click', function(e) {
    // Пройдёмся по всем полям
    var inputs = document.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
      var input = inputs[i];
      input.setCustomValidity("");
      // Проверим валидность поля, используя встроенную в JavaScript функцию checkValidity()
      if (input.checkValidity() == false) {
        var inputCustomValidation = new CustomValidation(); // Создадим объект CustomValidation
        inputCustomValidation.clearInvalidities();
        inputCustomValidation.checkValidity(input); // Выявим ошибки
        var customValidityMessage = inputCustomValidation.getInvalidities(); // Получим все сообщения об ошибках
        input.setCustomValidity(customValidityMessage); // Установим специальное сообщение об ошибке
      } // закончился if
    } // закончился цикл
  });
}

function validate(){
    var inputs = document.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
      var input = inputs[i];
      input.setCustomValidity("");
      // Проверим валидность поля, используя встроенную в JavaScript функцию checkValidity()
      if (input.checkValidity() == false) {
        var inputCustomValidation = new CustomValidation(); // Создадим объект CustomValidation
        inputCustomValidation.clearInvalidities();
        inputCustomValidation.checkValidity(input); // Выявим ошибки
        var customValidityMessage = inputCustomValidation.getInvalidities(); // Получим все сообщения об ошибках
        input.setCustomValidity(customValidityMessage); // Установим специальное сообщение об ошибке
      } // закончился if
    } // закончился цикл
}
