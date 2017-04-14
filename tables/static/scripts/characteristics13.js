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

function addChar(charId, charType, name, charVal){
  //var char = $('#char').val();
  var char = "";
  //var vals = JSON.parse(charVal);
  switch (charType) {
    case 1:
      char = "<li class='list-group-item' id=" + charId + ">" +
      "<button class='close' onclick='delChar(this)'>x</button>" +
      "<h4 style='text-decoration: underline; color: mediumseagreen'>" + name + "</h4>" +
      "<div class='form-group' style='margin-bottom: 40pt'><label for='from' class='col-sm-2 control-label' style='font-size: small'>От: </label>" +
      "<div class='col-sm-4'><input id='from' name=" + charId + "'from' type='number' class='form-control' required></div> " +
        "<label for='to' class='col-sm-2 control-label' style='font-size: small'>До: </label>" +
        "<div class='col-sm-4'><input id='to' name=" + charId + "'to' type='number' class='form-control' required></div></div>" +
      "</li>";
    break;
    case 2:
      var vals = JSON.parse(charVal);
      char = "<li class='list-group-item' id=" + charId + ">" +
      "<button class='close' onclick='delChar(this)'>x</button>" +
      "<h4 style='text-decoration: underline; color: mediumseagreen'>" + name + "</h4>" +
      "<div class='form-group' style='margin-bottom: 40pt'><input id='number' type='number' name=" + charId + " class='form-control' min=" + vals[0].fields.min + " max=" + vals[0].fields.max + " required></div>" +
      "</li>";
      break;
    case 3:
    var elems = "";
    for(id in charVal) {
      elems += "<div class='checkbox'><label><input type='checkbox' value=" + id + " name=" + charId + "'checked_list'>" + charVal[id] + "</label></div>";
    }
    char = "<li class='list-group-item' id=" + charId + ">" +
    "<button class='close' onclick='delChar(this)'>x</button>" +
    "<h4 style='text-decoration: underline; color: mediumseagreen'>" + name + "</h4>" +
    elems + "</li>";
      break;
    default:
      char = "<li class='list-group-item'>Неизвестная группа характеристики</li>"
  }
  $("#chars").append(char);
  var chars = [];
  $("#chars li").each(function(indx, element){
    chars.push($(element).attr("id"));
  });
  var json = JSON.stringify(chars);
  $("#json").attr('value', JSON.stringify(chars));
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
          var char = JSON.parse((JSON.parse(data))['char']);
          var vals = JSON.parse(data).char_val
          addChar(char_id, char[0].fields.char_type, char[0].fields.name, vals)
        }
      });
}
//Функция получения элементов множества
function getElems(char_id){
  var csrftoken = getCookie('csrftoken');
  $.ajax({
        type: "POST",
        url: 'get_elems/',
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
          var vars = JSON.parse((JSON.parse(data))['vars']);
          var checked = JSON.parse((JSON.parse(data))['checked']);
          elems = ""
          for (id in vars){
            elems += "<div class='checkbox'><label><input type='checkbox' value=" + id + ((checked.indexOf(vars[id]) == -1) ? "" : "checked") + " name=" + char_id + "'checked_list'>" + vars[id] + "</label></div>";
          }
          $("#" + char_id).append(elems);
        }
      });
}

function delChar(elem){
  $(elem).parent().remove();
  var chars = [];
  $("#chars li").each(function(indx, element){
    chars.push($(element).attr("id"));
  });
  $("#json").attr('value', JSON.stringify(chars));
  return false;
}
