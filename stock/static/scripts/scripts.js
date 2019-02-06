function sendProp() {
    var data = null;
    var t = $('#type').prop('value');
    if (t == 0) {
        data = {'from': $('#from').prop('value'), 'to': $('#to').prop('value')};
    }
    else if (t == 2) {
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

function sendCounter() {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'send_counter/',
        data: {
            'name': $('#name').prop('value'),
            'kind': $('#kind').val(),
            'category': $('#category').val(),
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

function editProp(id) {
    var data = null;
    var t = $('#e_type').prop('value');
    if (t == 0) {
        data = {'from': $('#e_from').prop('value'), 'to': $('#e_to').prop('value')};
    }
    else if (t == 2) {
        data = [];
        tbody = document.getElementById("e_elems");
        for (i = 1; i < tbody.rows.length; i++) {
            var tr = $("#e_elems tr").eq(i);
            data.push(tr.find("td").eq(0).text());
        }
    }
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'edit_prop/',
        data: {
            'name': $('#e_name').prop('value'),
            'id': id,
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

function e_addUnit() {
    e_unitNum++;
    var code = "<div class='form-inline' style='margin-top:10px;'> - " + getUnits() +
        "                       <span style='font-size: 20px; color: #999999;' onclick='this.parentElement.remove();unitNum--;'><i class='fas fa-trash-alt menu-btn'></i></span></div>";
    var additionalUnit = $("#e_additional_unit");
    $(code).appendTo(additionalUnit);
}

function e_addProp() {
    e_propNum++;
    var code = "<div class='form-inline' style='margin-top:10px;'> - " + getPropsCode() + " <input type='checkbox' class='form-control inline-el visible'> Скрытое <input type='checkbox' class='form-control inline-el editable'> Неизменяемое <input type='checkbox' class='form-control inline-el isDefault' onclick='addDefault(this)'> Предустановленное <span style='font-size: 20px; color: #999999;' onclick='this.parentElement.remove();propNum--;'><i class='fas fa-trash-alt menu-btn'></i></span></div>";
    var additionalProp = $("#e_additional_prop");
    $(code).appendTo(additionalProp);
}

function searchModel(text) {
    if (text == "") {
        changeGroup();
    }
    else {
        $("#goods-body").html("");
        for (m in models) {
            if (models[m].name.toUpperCase().indexOf(text.toUpperCase()) != -1) {
                $("<tr onclick='getInf(" + models[m].id + ")'><td>" + models[m].id + "</td><td>" + models[m].name + "</td><td><button class='btn btn-danger' onclick='delModel(this.parentElement)'>Удалить</button></td></tr>").appendTo("#goods-body");
            }
        }
        if ($("#goods-body tr").length == 0) $("#goods-body").html("<tr><td class='no-data text-right'>Нет записей</td><td></td></tr>");
    }
}

function getInf(id) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'get_model_inf/',
        data: {
            'id': id
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            inf = JSON.parse(data);
            $("#e_additional_unit").html("");
            $("#e_additional_prop").html("");
            $("#e_name").prop("value", inf.name);
            $("#e_group option[value=" + inf.group + "]").prop('selected', true);

            for (u in inf.units) {
                e_addUnit();
                $("option[value=" + inf.units[u] + "]", $("#e_additional_unit").find("select").last()).prop('selected', true);
            }
            temp = inf.props;
            for (i in temp) {
                e_addProp();
                $("option[value=" + inf.props[i].id + "]", $("#e_additional_prop").find("select").last()).prop('selected', true);
                obj = $("#e_additional_prop").find("select").last()[0];
                $(obj.parentElement).find(".visible").eq(0).prop("checked", !inf.props[i].visible);
                $(obj.parentElement).find(".editable").eq(0).prop("checked", !inf.props[i].editable);
                $(obj.parentElement).find(".isDefault").eq(0).prop("checked", inf.props[i].isDefault);
                if (inf.props[i].isDefault) {
                    code = "<h6 class='addDefault'>Значение по умолчанию ";
                    if (inf.props[i].default_type == "0") {
                        code = code + "<input type='number' value=" + inf.props[i].default + " class='form-control default' />";
                    }
                    else if (inf.props[i].default_type == "1") {
                        code = code + "<input type='text' value=" + inf.props[i].default + " class='form-control default' />";
                    }
                    else {
                        code = code + "<select class='form-control default'>";
                        for (p in propVars) {
                            if (propVars[p].fields.prop == inf.props[i].id) {
                                if (propVars[p].pk = inf.props[i].default) {
                                    code = code + "<option value='" + propVars[p].pk + "' selected>" + propVars[p].fields.name + "</option>";
                                }
                                else {
                                    code = code + "<option value='" + propVars[p].pk + "'>" + propVars[p].fields.name + "</option>";
                                }
                            }
                        }
                        code = code + "</select></h6>";
                    }
                    $(code).appendTo(obj.parentElement);
                }

            }
            $("#editBtn").unbind('click');
        $("#editBtn").click(function () {
            editModel(id);
        });
            $("#inf_model").modal();

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
    code = code + "<li id=" + branch.id + "><span class='txt'>" + branch["name"] + menu + "</span>";
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

function editModel(id) {
    units = [];
    $("#e_additional_unit").find("select").each(function (item) {
        units.push($("option:selected", this).val());
    });
    props = {};
    $("#e_additional_prop").find("select").each(function (item) {
        if (!$(this).hasClass("default")) {
            props[item] = {};
            props[item]['prop'] = $("option:selected", this).val();
            props[item]['hidden'] = $(this.parentElement).find(".visible").eq(0).prop("checked");
            props[item]['uneditable'] = $(this.parentElement).find(".editable").eq(0).prop("checked");
            props[item]['isDefault'] = $(this.parentElement).find(".isDefault").eq(0).prop("checked");
            if (props[item]['isDefault'] == true) {
                props[item]['default'] = $(this.parentElement).find(".default").eq(0).prop("value");
            }
        }
    });
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'edit_model/',
        data: {
            'name': $('#e_name').prop('value'),
            'group': $("#e_group option:selected").val(),
            'units': JSON.stringify(units),
            'props': JSON.stringify(props),
            'id': id
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

function saveModel() {
    units = [];
    $("#additional_unit").find("select").each(function (item) {
        units.push($("option:selected", this).val());
    });
    props = {};
    $("#additional_prop").find("select").each(function (item) {
        if (!$(this).hasClass("default")) {
            props[item] = {};
            props[item]['prop'] = $("option:selected", this).val();
            props[item]['hidden'] = $(this.parentElement).find(".visible").eq(0).prop("checked");
            props[item]['uneditable'] = $(this.parentElement).find(".editable").eq(0).prop("checked");
            props[item]['isDefault'] = $(this.parentElement).find(".isDefault").eq(0).prop("checked");
            if (props[item]['isDefault'] == true) {
                props[item]['default'] = $(this.parentElement).find(".default").eq(0).prop("value");
            }
        }
    });
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'save_model/',
        data: {
            'name': $('#name').prop('value'),
            'group': $("#group option:selected").val(),
            'units': JSON.stringify(units),
            'props': JSON.stringify(props)
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

function Tree(tree) {
    this.tree = tree;
    this.selected = 1;
    var self = this;
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

    this.saveGroup = function (obj, id = null) {
        self = this;
        parent = $(obj).prop("id");
        val = $(obj).children().children("input")[0];
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'save_group/',
            data: {
                'name': $(val).prop('value'),
                'id': id,
                'parent': parent.split('-')[0]
            },
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function onAjaxSuccess(data) {
                id = data;
                menu = "<span style='font-size: 15px; color: yellowgreen;' onclick='tr.addGroup(this.parentElement)' id='a" + id + "'><i class='fas fa-plus-circle menu-btn'></i></span><span style='font-size: 15px; color: dodgerblue;' onclick='tr.editGroup(this.parentElement, " + id + ")'  id='e" + id + "'><i class='fas fa-pencil-alt menu-btn'></i></span><span style='font-size: 15px; color: red;' onclick='tr.delGroup(this.parentElement)' id='d" + id + "'><i class='fas fa-minus-circle menu-btn'></i></span>";
                $(obj).html("<span class='txt'>" + $(val).prop('value') + menu + "</span>");
                $(obj).prop("id", id);
                self.updEvent();
            }
        });
    };

    this.editGroup = function (obj, id) {
        //menu = "<span style='font-size: 15px; color: yellowgreen;' onclick='tr.addGroup(this.parentElement)' id='a" + id + "'><i class='fas fa-plus-circle menu-btn'></i></span><span style='font-size: 15px; color: dodgerblue;' id='e" + id + "'><i class='fas fa-pencil-alt menu-btn'></i></span><span style='font-size: 15px; color: red;' id='d" + id + "'><i class='fas fa-minus-circle menu-btn'></i></span>";
        //obj = $(obj).find(".txt").eq(0);
        val = $(obj).text();
        $(obj).html("<div class='form-inline'><input class='form-control form-control-sm' value='" + val + "'  type='text'/><span style='font-size: 20px; color: yellowgreen; margin-left: 5px' onclick='tr.saveGroup(this.parentElement.parentElement, " + id + ")'><i class='fas fa-check-circle'></i></span></div>");
        //this.updEvent();
    };

    this.delGroup = function (obj) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'del_group/',
            data: {
                'id': $(obj.parentElement).prop("id")
            },
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function onAjaxSuccess(data) {
                $(obj).remove();
            }
        });
        $(obj).remove();
        //this.updEvent();
    };

    this.addGroup = function (branch) {
        branch = branch.parentElement;
        openedClass = 'fa-folder-open';
        closedClass = 'fa-folder';
        id = $(branch).prop('id') + "-" + ($(branch).children("ul").length + 1).toString();
        if ($(branch).children("ul").length == 0) {
            $(branch).append("<ul><li id='" + id + "'><div class='form-inline'><input class='form-control form-control-sm' type='text'/><span style='font-size: 20px; color: yellowgreen; margin-left: 5px' onclick='tr.saveGroup(this.parentElement.parentElement)'><i class='fas fa-check-circle'></i></span></div></li></ul>");
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
            $($(branch).children("ul")[0]).append("<li id='" + id + "'><div class='form-inline'><input class='form-control form-control-sm' type='text'/><span style='font-size: 20px; color: yellowgreen; margin-left: 5px' onclick='tr.saveGroup(this.parentElement.parentElement)'><i class='fas fa-check-circle'></i></span></div></li></li>");
        }
    };

    this.init();
    this.updEvent();
    $("#tree li").click(function (event) {
        id = $(this).prop("id");
        self.selected = id;
        $("#tree span").removeClass('active');
        obj = $(this).children("span");
        $(this).children("span").eq(0).addClass('active');
        $("#group option[value=" + id + "]").prop('selected', true);
        changeGroup();
        //event.stopPropagation();
    });
}

function changeGroup() {
    $("#goods-body").html("");
    for (m in models) {
        if (models[m].group == tr.selected) {
            $("<tr id=" + models[m].id + "><td>" + models[m].id + "</td><td  onclick='getInf(" + models[m].id + ")'>" + models[m].name + "</td><td><button class='btn btn-danger' onclick='delModel(this.parentElement)'>Удалить</button></td></tr>").appendTo("#goods-body");
        }
    }
    if ($("#goods-body tr").length == 0) $("#goods-body").html("<tr><td class='no-data text-right'>Нет записей</td><td></td><td></td></tr>");
}

function delModel(obj) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'del_model/',
        data: {
            'id': $(obj.parentElement).prop("id")
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            $(obj.parentElement).remove();
        }
    });
    //this.updEvent();
};

function getDefault(sel) {
    t = $("option:selected", sel).prop("class");
    id = $("option:selected", sel).val();
    code = "<h6 class='addDefault'>Значение по умолчанию ";
    if (t == "0") {
        code = code + "<input type='number' class='form-control default' />";
    }
    else if (t == "1") {
        code = code + "<input type='text' class='form-control default' />";
    }
    else {
        code = code + "<select class='form-control default'>";
        for (p in propVars) {
            if (propVars[p].fields.prop == id) {
                code = code + "<option value='" + propVars[p].pk + "'>" + propVars[p].fields.name + "</option>";
            }
        }
        code = code + "</select></h6>";
    }
    return code;
}

function addDefault(obj) {
    $(obj.parentElement).find(".addDefault").remove();
    if ($(obj).prop("checked") == true) {
        $(getDefault($(obj.parentElement).find('select').eq(0))).appendTo(obj.parentElement);
    }
}

function addDefault2(obj) {
    addDefault($(obj.parentElement).find(".isDefault").eq(0)[0]);
}

function getProps(selType) {
    switch (selType) {
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
                "</div>" +
                "<input type='hidden' id='json' name='json' value=''>");
            break;
        default:
            return false;
    }
}

function addEl() {
    $("<tr><td><input type='text' class='form-control input-sm' style='height:32px'></td><td><button class='btn btn-success btn-sm' onclick='saveEl(this)'>Сохранить</button></td></tr>").appendTo("#elems");
}

function addEl2() {
    $("<tr><td><input type='text' class='form-control input-sm' style='height:32px'></td><td><button class='btn btn-success btn-sm' onclick='saveEl(this)'>Сохранить</button></td></tr>").appendTo("#e_elems");
}

function saveEl(el) {
    var text = $(el.parentElement.parentElement).find('input').prop('value');
    $(el.parentElement.parentElement).html("<td>" + text + "</td><td><button class='btn btn-danger btn-sm' onclick='$(this.parentElement.parentElement).remove()'>Удалить</button></td>");
}

function Property(data) {
    this.props = JSON.parse(data);
    this.getInf = function (id) {
        $("#e_name").prop("value", this.props[id].name);
        $("#e_type [value=" + this.props[id].type + "]").prop("selected", "selected");
        switch (this.props[id].type) {
            case 0:
                $("#e_charVal").html("<h6 style='margin-top: 10px'>Числовой диапазон: </h6>" +
                    "<h7>От: </h7>" +
                    "<input id='e_from' name='from' type='number' class='form-control' value='" + this.props[id].from + "' required>" +
                    "<h7>До: </h7>" +
                    "<input id='e_to' name='to' type='number' class='form-control'  value='" + this.props[id].to + "' required>");
                break;
            case 1:
                $("#e_charVal").html("");
                break;
            case 2:
                $("#e_charVal").html(
                    "<div class='card' style='margin-top: 10px'>" +
                    "<div class='card-header'>" +
                    "<button class='btn btn-success btn-sm' onclick='addEl2()'>Добавить элемент множества</button>" +
                    "</div>" +
                    "<table class='table table-sm' id='e_elems'>" +
                    "<thead><tr><th style='text-align: center'>Значение</th><th></th></tr></thead><tbody></tbody></table>" +
                    "</div>");
                for (p in this.props[id].vals) {
                    $("<tr><td>" + this.props[id].vals[p] + "</td><td><button class='btn btn-danger btn-sm' onclick='$(this.parentElement.parentElement).remove()'>Удалить</button></td></tr>").appendTo("#e_elems");
                }
                break;
            default:
                return false;
        }
        ;
        $("#editBtn").unbind('click');
        $("#editBtn").click(function () {
            editProp(id);
        });
        $("#inf_prop").modal();
    }
}

function getModelInfo(){
    var code = "";
    id = $("#model").val();
    $("#units").html("");
    $("#props").html("");
    //получение единиц измерения
    for (u in models[id]['units']){
        code = code + "<div class='form-inline'><div class='form-group col-md-6'><h6>- " + models[id]['units'][u].name + "</h6></div><div class='form-group inline-group col-md-6'>Коэффициент <input type='number' class='form-control inline-el'/></div></div>";
        code = code + "<div class='form-inline'><div class='form-group col-md-6'><input type='checkbox' class='form-control' /> <span class='inline-el'>Применимая</span></div><div class='form-group col-md-6'><input type='radio' class='form-control'/><span class='inline-el'> Базовая</span></div></div>";
    }
    $(code).appendTo("#units");
    //получение свойств
    code = "";
    for (p in models[id]['props']){
        code = code + "<div class='form-inline'><h6>- " + models[id]['props'][p].name + "</h6>" + getPropCode(models[id]['props'][p]['type'], models[id]['props'][p]['value'], models[id]['props'][p]['choises']) + "</div>";
        code = code + "<div class='form-inline'><input type='checkbox' class='form-control' /> <span class='inline-el'>Скрытое</span><input type='checkbox' class='form-control'/><span class='inline-el'> Неизменяемое</span><input type='checkbox' class='form-control'/><span class='inline-el'> Неприменимое</span></div>";
    }
    $(code).appendTo("#props");
}

function getPropCode(t, value = "", choises = null){
    var code = "";
    switch (t){
        case 0:
            code = "<input type='number' class='form-control inline-el' value='" + value + "'/>";
            break;
        case 1:
            code = "<input type='text' class='form-control inline-el' value='" + value + "'/>";
            break;
        case 2:
            code = "<select class='form-control inline-el'>";
            for (c in choises){
                if (c == value){
                    code = code + "<option value='" + c +"' selected>" + choises[c] + "</option>";
                }
                else code = code + "<option value='" + c +"'>" + choises[c] + "</option>";
            }
            code = code + "</select>";
            break;
    }
    return code;
}