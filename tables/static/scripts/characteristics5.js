//Функция для отображения полей выбранного типа характеристики
function getCharVal(groups){
  var selType = $("#type").val();
  switch (selType){
    case "1":
      $("#charVal").html("<div class='form-group'>" +
        "<label for='range' class='col-sm-12 control-label' style='font-size: medium; margin-bottom: 20pt;'>Числовой диапазон: </label>" +
        "<label for='from' class='col-sm-2 control-label' style='font-size: medium'>От: </label>" +
        "<div class='col-sm-4'><input id='from' name='from' type='number' class='form-control' required></div>" +
          "<label for='to' class='col-sm-2 control-label' style='font-size: medium'>До: </label>" +
          "<div class='col-sm-4'><input id='to' name='to' type='number' class='form-control' required></div>" +
        "</div>");
      break;
    case "2":
      $("#charVal").html("<div class='form-group'>" +
        "<label for='range' class='col-sm-12 control-label' style='font-size: medium; margin-bottom: 20pt;'>Числовой диапазон: </label>" +
        "<label for='from' class='col-sm-2 control-label' style='font-size: medium'>От: </label>" +
        "<div class='col-sm-4'><input id='from' name='from' type='number' class='form-control' required></div>" +
          "<label for='to' class='col-sm-2 control-label' style='font-size: medium'>До: </label>" +
          "<div class='col-sm-4'><input id='to' name='to' type='number' class='form-control' required></div>" +
        "</div>");
      break;
    case "3":
    $("#charVal").html("<div class='modal fade' id='newComp'>"+
      "<div class='modal-dialog'>" +
        "<div class='modal-content'>" +
          "<div class='modal-header'>" +
            "<button class='close' data-dismiss='modal'>x</button>" +
            "<h4>Добавление элемента</h4>" +
          "</div>" +
          "<div class='modal-body'>" +
            "<div class='form-group' style='margin-bottom: 20pt'><input id='elem' name='elem' class='form-control' type='text'></div>" +
          "</div>" +
          "<div class='modal-footer'><button type='button' class='btn btn-primary' onclick='addElem()' data-dismiss='modal'>Добавить</button></div>" +
        "</div>" +
      "</div>" +
    "</div>" +
    "<div class='panel panel-default'>" +
      "<div class='panel-heading'>" +
        "<button class='btn btn-success' data-toggle='modal' data-target='#newComp'><i class='glyphicon glyphicon-plus'></i> Добавить элемент множества</button>" +
      "</div>" +
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
