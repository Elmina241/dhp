function CustomValidation() { }

CustomValidation.prototype = {
  // Установим пустой массив сообщений об ошибках
  invalidities: [],

  // Метод, проверяющий валидность
  checkValidity: function(input) {

    var validity = input.validity;

    if (validity.rangeOverflow) {
      var max = getAttributeValue(input, 'max');
      this.addInvalidity('Максимальное возможное значение: ' + max);
    }

    if (validity.rangeUnderflow) {
      var min = getAttributeValue(input, 'min');
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
  }
};

var submit = document.getElementById("send");
// Добавляем обработчик клика на кнопку отправки формы
submit.addEventListener('click', function(e) {
  // Пройдёмся по всем полям
  for (var i = 0; i < inputs.length; i++) {

    var input = inputs[i];

    // Проверим валидность поля, используя встроенную в JavaScript функцию checkValidity()
    if (input.checkValidity() == false) {

      var inputCustomValidation = new CustomValidation(); // Создадим объект CustomValidation
      inputCustomValidation.checkValidity(input); // Выявим ошибки
      var customValidityMessage = inputCustomValidation.getInvalidities(); // Получим все сообщения об ошибках
      input.setCustomValidity(customValidityMessage); // Установим специальное сообщение об ошибке

    } // закончился if
  } // закончился цикл
});
