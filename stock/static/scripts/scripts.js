function getReq(period) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'get_req/',
        data: {
            'period': period
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            addRows("stock-tbody", data);
            $("#stock-tbody tr").each(function () {
                $(this).click(function () {
                    getDoc($(this).prop("id"));
                });
            });
        }
    });
}

function getPrices(price) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'get_price/',
        data: {
            'price': price
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
            $("#loader").show();
        },
        success: function onAjaxSuccess(data) {
            var goods = JSON.parse(data);
            $("#tree").html("");
            initTree(goods);
            $("#loader").hide();
        }
    });
}



function getDoc(id) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'get_doc/',
        data: {
            'id': id
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            addRows("doc-tbody", data);
            var rows = JSON.parse(data);
            num_b = 0;
            num = 0;
            for (r in rows) {
                num_b = num_b + parseInt(rows[r]["num_b"]);
                num = num + parseInt(rows[r]["num"]);
            }
            $("<tr class='table-info'><td><b>Итого</b></td><td></td><td>" + num_b + "</td><td></td><td></td><td></td><td>" + num + "</td></tr>").appendTo("#doc-tbody");
        }
    });
}

function sendProp() {
    var data = null;
    var t = $('#type').prop('value');
    if (t == 0){
        data = {'from': $('#from').prop('value'), 'to': $('#to').prop('value')};
    }
    else if (t == 2){
         data = [];
         tbody = document.getElementById("elems");
         for (i = 1; i < tbody.rows.length; i++) {
             var tr = $("#elems tr").eq(i);
             data.push(tr.find("td").eq(0).text());
         }
    }
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'send_prop/',
        data: {
            'name': $('#name').prop('value'),
            'type': t,
            'data': JSON.stringify(data)
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            window.location.reload();
        }
    });
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
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function addGoods(table, rows) {
    row = "";
    for (r in rows) {
        row = row + "<tr id=id-" + r + ">";
        for (d in rows[r]) {
            if (rows[r][d] == null) {
                row = row + "<td>--</td>";
            }
            else row = row + "<td>" + rows[r][d] + "</td>";
        }
        row = row + "</tr>";
    }
    var tableBody = $("#" + table);
    //var rowCount = $("#" + table + " tr").length;
    $(tableBody).html("");
    if (row == "") {
        row = "<tr><td></td><td></td><td class='no-data text-right'>Нет записей</td><td></td><td></td></tr>";
    }
    //for (i = 0; i < rowCount; i++) $("#" + table + " tr").eq(0).remove();
    $(row).appendTo(tableBody);
}

function addRows(table, data) {
    var rows = JSON.parse(data);
    row = "";
    for (r in rows) {
        row = row + "<tr id=id-" + r + ">";
        for (d in rows[r]) {
            if (rows[r][d] == null) {
                row = row + "<td>--</td>";
            }
            else row = row + "<td>" + rows[r][d] + "</td>";
        }
        row = row + "</tr>";
    }
    var tableBody = $("#" + table);
    //var rowCount = $("#" + table + " tr").length;
    $(tableBody).html("");
    //for (i = 0; i < rowCount; i++) $("#" + table + " tr").eq(0).remove();
    $(row).appendTo(tableBody);
}


function addBranch(code, branch) {
    menu = "<span style='font-size: 15px; color: yellowgreen;' onclick='tr.addGroup(this.parentElement)' id='a" + branch.id + "'><i class='fas fa-plus-circle menu-btn'></i></span><span style='font-size: 15px; color: dodgerblue;' onclick='tr.editGroup(this.parentElement, " + branch.id + ")'  id='e" + branch.id + "'><i class='fas fa-pencil-alt menu-btn'></i></span><span style='font-size: 15px; color: red;' onclick='tr.delGroup(this.parentElement)' id='d" + branch.id + "'><i class='fas fa-minus-circle menu-btn'></i></span>";
    code = code + "<li id=" + branch.id + ">" + branch["name"] + menu;
    if (branch["nodes"] != undefined) {
        code = code + "<ul>";
        for (br in branch["nodes"]) {
            code = addBranch(code, branch["nodes"][br]);
        }
        code = code + "</ul>";
    }
    code = code + "</li>";
    return code;
}

function Tree(tree) {
    this.tree = tree;

    this.init = function () {
        $('#tree').html("");
        this.makeTree();
        $('#tree').treed({openedClass: 'fa-folder-open', closedClass: 'fa-folder'});
        $("#tree li").click(function (event) {
            event.stopPropagation();
        });
    };

    this.makeTree = function () {
        code = "";
        code = code + addBranch(code, this.tree[0]["nodes"][1]);
        $(code).appendTo("#tree");
    };

    this.updEvent = function () {
        $("#tree li").unbind('mouseover');
        $("#tree li").unbind('mouseout');
        $("#tree li").mouseover(function (event) {
            id = $(this).prop("id");
            $("#a" + id).show();
            $("#e" + id).show();
            $("#d" + id).show();
            event.stopPropagation();
        });
        $("#tree li").mouseout(function (event) {
            id = $(this).prop("id");
            $("#a" + id).hide();
            $("#e" + id).hide();
            $("#d" + id).hide();
            event.stopPropagation();
        });
    };

    this.saveGroup = function (obj, id) {
        menu = "<span style='font-size: 15px; color: yellowgreen;' onclick='tr.addGroup(this.parentElement)' id='a" + id + "'><i class='fas fa-plus-circle menu-btn'></i></span><span style='font-size: 15px; color: dodgerblue;' onclick='tr.editGroup(this.parentElement, " + id + ")'  id='e" + id + "'><i class='fas fa-pencil-alt menu-btn'></i></span><span style='font-size: 15px; color: red;' onclick='tr.delGroup(this.parentElement)' id='d" + id + "'><i class='fas fa-minus-circle menu-btn'></i></span>";
        val = $(obj).children().children("input")[0];
        $(obj).html($(val).prop('value') + menu);
        this.updEvent();
    };

    this.editGroup = function (obj, id) {
        //menu = "<span style='font-size: 15px; color: yellowgreen;' onclick='tr.addGroup(this.parentElement)' id='a" + id + "'><i class='fas fa-plus-circle menu-btn'></i></span><span style='font-size: 15px; color: dodgerblue;' id='e" + id + "'><i class='fas fa-pencil-alt menu-btn'></i></span><span style='font-size: 15px; color: red;' id='d" + id + "'><i class='fas fa-minus-circle menu-btn'></i></span>";
        val = $(obj).text();
        $(obj).html("<div class='form-inline'><input class='form-control form-control-sm' value='" + val + "'  type='text'/><span style='font-size: 20px; color: yellowgreen; margin-left: 5px' onclick='tr.saveGroup(this.parentElement.parentElement, " + id + ")'><i class='fas fa-check-circle'></i></span></div>");
        //this.updEvent();
    };

    this.delGroup = function (obj) {
        $(obj).remove();
        //this.updEvent();
    };

    this.addGroup = function (branch) {
        openedClass = 'fa-folder-open';
        closedClass = 'fa-folder';
        id = $(branch).prop('id') + ($(branch).children("ul").length + 1).toString();
        if ($(branch).children("ul").length == 0) {
            $(branch).append("<ul><li id='" + id + "'><div class='form-inline'><input class='form-control form-control-sm' type='text'/><span style='font-size: 20px; color: yellowgreen; margin-left: 5px' onclick='tr.saveGroup(this.parentElement.parentElement, " + id + ")'><i class='fas fa-check-circle'></i></span></div></li></ul>");
            $(branch).prepend("<i class='indicator fas " + openedClass + "'></i>");
            $(branch).addClass('branch');
            $(branch).on('click', function (e) {
                if (this == e.target) {
                    var icon = $(this).children('i:first');
                    icon.toggleClass(openedClass + " " + closedClass);
                    $(this).children().children().toggle();
                }
            });
        }
        else {
            $($(branch).children("ul")[0]).append("<li id='" + id + "'><div class='form-inline'><input class='form-control form-control-sm' type='text'/><span style='font-size: 20px; color: yellowgreen; margin-left: 5px' onclick='tr.saveGroup(this.parentElement.parentElement, " + id + ")'><i class='fas fa-check-circle'></i></span></div></li></li>");
        }
    };

    this.init();
    this.updEvent();
}

function getProps(selType){
    switch (selType){
    case "0":
      $("#charVal").html("<h6 style='margin-top: 10px'>Числовой диапазон: </h6>" +
        "<h7>От: </h7>" +
        "<input id='from' name='from' type='number' class='form-control' required>" +
          "<h7>До: </h7>" +
          "<input id='to' name='to' type='number' class='form-control' required>");
      break;
    case "1":
        $("#charVal").html("");
      break;
    case "2":
    $("#charVal").html(
    "<div class='card' style='margin-top: 10px'>" +
      "<div class='card-header'>" +
        "<button class='btn btn-success btn-sm' onclick='addEl();' data-target='#newComp'>Добавить элемент множества</button>" +
      "</div>" +
    "<table class='table table-sm' id='elems'>" +
      "<thead><tr><th style='text-align: center'>Значение</th><th></th></tr></thead><tbody></tbody></table>" +
    "</div>"+
    "<input type='hidden' id='json' name='json' value=''>");
      break;
    default:
      return false;
  }
}

function addEl(){
    $("<tr><td><input type='text' class='form-control input-sm' style='height:32px'></td><td><button class='btn btn-success btn-sm' onclick='saveEl(this)'>Сохранить</button></td></tr>").appendTo("#elems");
}

function saveEl(el){
    var text = $(el.parentElement.parentElement).find('input').prop('value');
    $(el.parentElement.parentElement).html("<td>" + text + "</td><td><button class='btn btn-danger btn-sm' onclick='$(this.parentElement.parentElement).remove()'>Удалить</button></td>");
}

function Property(data){
    this.props = JSON.parse(data);
    this.getInf = function(id){
        $("#e_name").prop("value", this.props[id].name);
        $("#e_type [value=" + this.props[id].type + "]").prop("selected", "selected");
        switch (this.props[id].type) {
            case 0:
                $("#e_charVal").html("<h6 style='margin-top: 10px'>Числовой диапазон: </h6>" +
                    "<h7>От: </h7>" +
                    "<input id='from' name='from' type='number' class='form-control' value='" + this.props[id].from + "' required>" +
                    "<h7>До: </h7>" +
                    "<input id='to' name='to' type='number' class='form-control'  value='" + this.props[id].to + "' required>");
                break;
            case 1:
                $("#e_charVal").html("");
                break;
            case 2:
                $("#e_charVal").html(
                    "<div class='card' style='margin-top: 10px'>" +
                    "<div class='card-header'>" +
                    "<button class='btn btn-success btn-sm' onclick=''>Добавить элемент множества</button>" +
                    "</div>" +
                    "<table class='table table-sm' id='e_elems'>" +
                    "<thead><tr><th style='text-align: center'>Значение</th><th></th></tr></thead><tbody></tbody></table>" +
                    "</div>");
                for (p in this.props[id].vals){
                    $("<tr><td>" + this.props[id].vals[p] + "</td><td><button class='btn btn-danger btn-sm' onclick='$(this.parentElement.parentElement).remove()'>Удалить</button></td></tr>").appendTo("#e_elems");
                }
                break;
            default:
                return false;
        };
        $("#inf_prop").modal();
    }
}