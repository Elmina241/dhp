//Функция для отображения полей выбранного типа характеристики
function getCharVal(groups){
  var selType = $("#type").val();
  switch (selType){
    case "1":
      $("#charVal").html("<div class='form-group'><label for='range' class='col-sm-12 control-label' style='font-size: medium'>Числовой диапазон: </label><label for='from' class='col-sm-2 control-label' style='font-size: medium'>От: </label><div class='col-sm-4'><input id='from' name='from' type='number' class='form-control' required><label for='to' class='col-sm-2 control-label' style='font-size: medium'>До: </label><div class='col-sm-4'><input id='to' name='to' type='number' class='form-control' required></div>");
      break;
    case "2":
      $("#charVal").html("<div class='form-group'><label for='range' class='col-sm-12 control-label' style='font-size: medium'>Числовой диапазон: </label><label for='from' class='col-sm-2 control-label' style='font-size: medium'>От: </label><div class='col-sm-4'><input id='from' name='from' type='number' class='form-control' required><label for='to' class='col-sm-2 control-label' style='font-size: medium'>До: </label><div class='col-sm-4'><input id='to' name='to' type='number' class='form-control' required></div>");
      break;
    case "3":
    $("#charVal").html("<div class='panel panel-default'>" +
      "<div class='panel-heading'>" +
          "<div class='form-group'><div class='col-sm-10'><input id='elem' name='elem' type='text' class='form-control'></div><div class='col-sm-2'><button class='form-control btn btn-default'>Добавить</button></div></div>" +
      "</div>"+
    "<div class='panel-body'>" +
    "<table class='table table-sm' id='elems'>" +
      "<thead><tr><th>Значение</th></tr></thead><tbody></tbody></table>" +
    "</div></div>");
      break;
    default:
      return false;
  }
}

function addElem(){
  var name = $('#elem').val();
  $("<tr><td>" + name + "</td></tr>").appendTo("#elems tbody");
}
