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
    "</div></div>"+
    "<input type='hidden' id='json' name='json' value=''>");
      break;
    default:
      return false;
  }
}

function addElem(){
  var name = $('#elem').val();
  $("<tr><td>" + name + "</td></tr>").appendTo("#elems tbody");
  var table = $('#elems').tableToJSON(); // Convert the table into a javascript object
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
}

function addChar(charId, charType, charVal){
  var char = $('#char').val();
  $("#chars").append("<li class='list-group-item'></li>");
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
function getChar(char_id){
  var csrftoken = getCookie('csrftoken');
  $.ajax({
        type: "POST",
        url: 'get_char/',
        data: {
          'char_id': char_id
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data)
        {
          var char = JSON.parse(data);
        }
      });
}
