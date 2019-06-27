function sendProp() {
    if ($('#form')[0].checkValidity()) {
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
}

function sendCounter() {
    if ($('#form')[0].checkValidity()) {
        stocks = [];
        $("#stocks").find("select").each(function (item) {
            stocks.push($("option:selected", this).val());
        });
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'send_counter/',
            data: {
                'name': $('#name').prop('value'),
                'kind': $('#kind').val(),
                'stocks': JSON.stringify(stocks),
                'isProv': $("#isProv").prop('checked'),
                'isCons': $("#isCons").prop('checked'),
                'isMember': $("#isMember").prop('checked')
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
}

function editCounter(id) {
    if ($('#form2')[0].checkValidity()) {
        stocks = [];
        $("#e_stocks").find("select").each(function (item) {
            stocks.push($("option:selected", this).val());
        });
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'edit_counter/',
            data: {
                'id': id,
                'name': $('#e_name').prop('value'),
                'kind': $('#e_kind').val(),
                'stocks': JSON.stringify(stocks),
                'isProv': $("#e_isProv").prop('checked'),
                'isCons': $("#e_isCons").prop('checked'),
                'isMember': $("#e_isMember").prop('checked')
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
}

function saveStock(id) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'save_stock/',
            data: {
                'id': id,
                'name': $('#e_name').prop('value'),
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

function delStock(id) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'del_stock/',
            data: {
                'id': id,
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

function sendStock() {
    if ($('#form')[0].checkValidity()) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'send_stock/',
            data: {
                'name': $('#name').prop('value'),
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
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
    var code = "<div class='form-inline' style='margin-top:10px;'> - " + getMUnits() +
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
        changeGroup("models");
    }
    else {
        $("#goods-body").html("");
        for (m in models) {
            if (models[m].name.toUpperCase().indexOf(text.toUpperCase()) != -1) {
            $("<tr id=" + models[m].id + "><td  onclick='getInf(" + models[m].id + ", false)'>" + models[m].name + "</td><td><span onclick='getInf(" + models[m].id + ")'><i title='Редактировать' class='fas fa-edit menu-btn'></i></span><span onclick='confirmDel(\"" + models[m].name + "\", this.parentElement)'><i title='Удалить' class='fas fa-trash-alt menu-btn'></i></span></td></tr>").appendTo("#goods-body");
               // $("<tr onclick='getInf(" + models[m].id + ")'><td>" + models[m].id + "</td><td>" + models[m].name + "</td><td><span onclick='delModel(this.parentElement)'><i class='fas fa-trash-alt menu-btn'></i> Удалить</span></td></tr>").appendTo("#goods-body");
            }
        }
        if ($("#goods-body tr").length == 0) $("#goods-body").html("<tr><td align='center' class='no-data' colspan='3'>Нет записей</td></tr>");
    }
}

function searchGood(text) {
    if (text == "") {
        changeGroup("goods");
    }
    else {
        $("#goods-body").html("");
        for (g in goods) {
            if (goods[g].name.toUpperCase().indexOf(text.toUpperCase()) != -1 || goods[g].article.toUpperCase().indexOf(text.toUpperCase()) != -1) {
                id = "<td>" + goods[g].article + "</td>";
                $("<tr id=" + goods[g].id + ">" + id + "<td  onclick='getGoodInf(" + goods[g].id + ")'>" + goods[g].name + "</td><td><span onclick='getGoodInf(" + data[g].id + ")'><i title='Редактировать' class='fas fa-edit menu-btn'></i></span><span onclick='confirmDel(\"" + goods[g].name + "\" ,this.parentElement)'><i title='Удалить' class='fas fa-trash-alt menu-btn'></i></span></td></tr>").appendTo("#goods-body");
                //$("<tr onclick='getGoodInf(" + goods[g].id + ")'><td>" + goods[g].article + "</td><td>" + goods[g].name + "</td><td><button class='btn btn-danger' onclick='delGood(this.parentElement)'>Удалить</button></td></tr>").appendTo("#goods-body");
            }
        }
        if ($("#goods-body tr").length == 0) $("#goods-body").html("<tr><td class='no-data' align='center' colspan='3'>Нет записей</td></tr>");
    }
}

function getInf(id, isEdit = true) {
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
                $("#e_additional_prop").find("select").last().prop('disabled', true);
                obj = $("#e_additional_prop").find("select").last()[0];
                $(obj.parentElement).find(".visible").eq(0).prop("checked", !inf.props[i].visible);
                $(obj.parentElement).find(".editable").eq(0).prop("checked", !inf.props[i].editable);
                $(obj.parentElement).find(".isDefault").eq(0).prop("checked", inf.props[i].isDefault);
                if (inf.props[i].isDefault) {
                    code = "<h6 class='addDefault'>Значение по умолчанию ";
                    if (inf.props[i].default_type == "0") {
                        code = code + "<input type='number' value=" + inf.props[i].default + " class='form-control form-control-sm default' />";
                    }
                    else if (inf.props[i].default_type == "1") {
                        code = code + "<input type='text' value=" + inf.props[i].default + " class='form-control form-control-sm default' />";
                    }
                    else {
                        code = code + "<select class='form-control form-control-sm default'>";
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
            if (isEdit){
                $("#editBtn").show();
                $(".plus").show();
                $("#modalHeader").text("Редактирование макета");
            }
            else {
                $("#editBtn").hide();
                $(".plus").hide();
                $("#modalHeader").text("Просмотр макета");
            }
        }
    });
}

function getGoodInf(id, isEdit = true) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'get_good_inf/',
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
            $("#e_units").html("");
            $("#e_props").html("");
            $("#e_names").html("");
            var pk = id;
            $("#editBtn").unbind('click');
            $("#editBtn").click(function () {
                editGood(pk);
            });
            $("#e_model option[value=" + inf.model + "]").prop('selected', true);
            $("#e_counter option[value=" + inf.counter + "]").prop('selected', true);
            var code = "";
            for (u in inf.units) {
                code = code + "<div class='unit'  id='" + u + "'><div class='form-inline'><div class='form-group col-md-6'><h6>- " + inf['units'][u].name + "</h6></div><div class='form-group inline-group col-md-6'>Коэффициент <input type='number' value='" + inf.units[u].value + "' class='form-control form-control-sm inline-el'/></div></div>";
                if (inf.units[u].isBase) checked = "checked";
                else checked = "";
                code = code + "<div class='form-inline'><div class='form-group col-md-6'><input type='radio' name='e_isBase' class='form-control' " + checked + "/><span class='inline-el'> Базовая</span></div></div>";
            }
            $(code).appendTo("#e_units");
            code = "";
            for (n in inf.names) {
                code = code + "<tr class='name'>\n" +
                "                            <td><input type=\"text\" class=\"form-control form-control-sm\" value='" + inf.names[n].name + "'  required/></td>\n" +
                "                            <td>\n" +
                "                                <select class=\"form-control form-control-sm type\" >\n" +
                "                                    <option value=\"0\" "+ (inf.names[n].type == 0 ? "selected" : "")  +">Наименование</option>\n" +
                "                                    <option value=\"1\" "+ (inf.names[n].type == 1 ? "selected" : "")  +">Артикул</option>\n" +
                "                                    <option value=\"2\" "+ (inf.names[n].type == 2 ? "selected" : "")  +">Штрихкод</option>\n" +
                "                                </select>\n" +
                "                            </td>\n" +
                "                            <td>\n" +
                "                                <select class=\"form-control form-control-sm area\" value='" + inf.names[n].area + "' >\n" +
                "                                    <option value=\"0\"  "+ (inf.names[n].area == 0 ? "selected" : "")  +">Локальное</option>\n" +
                "                                    <option value=\"1\"  "+ (inf.names[n].area == 1 ? "selected" : "")  +">Транзитное</option>\n" +
                "                                    <option value=\"2\"  "+ (inf.names[n].area == 2 ? "selected" : "")  +">Оригинальное</option>\n" +
                "                                </select>\n" +
                "                            </td><td style='padding-top: 12px'><span onclick='this.parentElement.parentElement.remove()'><i class='fas fa-trash-alt'></i></span></td>\n" +
                "                        </tr>";
            }
            code = code + "<tr><td colspan='4'><button onclick='addName(this)' class='btn btn-sm btn-outline-success add-btn' style='float: right'>Добавить</button></td></tr>";
            $(code).appendTo("#e_names");
            code = "";
            for (p in inf.props) {
                code = code + "<div class='prop'  id='" + p + "'><div class='form-inline'><div class='form-group col-md-3'><h6>- " + inf['props'][p].name + "</h6></div><div class='form-group col-md-6'>" + getPropCode(inf['props'][p]['type'], inf['props'][p]['value'], inf['props'][p]['choises'], inf['props'][p]['editable']) + "</div></div>";
            }
            $(code).appendTo("#e_props");
            $("#e_props").find(".prop").each(function (item) {
                id = $(this).prop("id");
                $(this).find("input").eq(0).prop("disabled", !inf.props[id].editable);
            });

            if (isEdit){
                $("#editBtn").show();
                $(".plus").show();
                $("#modalHeader").text("Редактирование МЦ");
            }
            else {
                $("#editBtn").hide();
                $(".plus").hide();
                $("#modalHeader").text("Просмотр МЦ");
            }
            $("#inf_good").modal();

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
        row = "<tr><td class='no-data' align='center' colspan='5'>Нет записей</td></tr>";
    }
    //for (i = 0; i < rowCount; i++) $("#" + table + " tr").eq(0).remove();
    $(row).appendTo(tableBody);
}

function addGoodsReq(table, data) {
    var rows = JSON.parse(data);
    var row = "";
    for (r in rows) {
        row = row + "<tr id=id-" + r + "><td>" + rows[r].article + "</td><td>" + rows[r].name + "</td><td>" + rows[r].amount + "</td><td>" + rows[r].unit + "</td>";
        row = row + "</tr>";
    }
    colNum = $("#" + table).parent().find("th").length;
    var tableBody = $("#" + table);
    $(tableBody).html("");
    if (row == "") row = "<tr><td colspan='" + colNum + "' class='no-data'>Нет записей</td></tr>";
    $(row).appendTo(tableBody);
}

function addGoodsOp(table, data) {
    var rows = JSON.parse(data);
    var row = "";
    for (r in rows) {
        if (rows[r].article != undefined) {
            row = row + "<tr id=id-" + r + "><td>" + rows[r].article + "</td><td>" + rows[r].name + "</td><td>" + rows[r].amount + "</td><td>" + rows[r].unit + "</td><td>" + rows[r].cost + "</td>";
            row = row + "</tr>";
        }
    }
    colNum = $("#" + table).parent().find("th").length;
    var tableBody = $("#" + table);
    $(tableBody).html("");
    if (row == "") row = "<tr><td colspan='" + colNum + "' class='no-data'>Нет записей</td></tr>";
    $(row).appendTo(tableBody);
}

function addGoodsSh(table, data) {
    var rows = JSON.parse(data);
    var row = "";
    for (r in rows) {
        if (rows[r].article != undefined) {
            row = row + "<tr id=id-" + r + "><td>" + rows[r].article + "</td><td>" + rows[r].name + "</td><td>" + rows[r].amount + "</td><td>" + rows[r].unit + "</td><td>" + rows[r].balance + "</td>";
            row = row + "</tr>";
        }
    }
    colNum = $("#" + table).parent().find("th").length;
    var tableBody = $("#" + table);
    $(tableBody).html("");
    if (row == "") row = "<tr><td colspan='" + colNum + "' class='no-data'>Нет записей</td></tr>";
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
    colNum = $("#" + table).parent().find("th").length;
    var tableBody = $("#" + table);
    //var rowCount = $("#" + table + " tr").length;
    $(tableBody).html("");
    if (row == "") row = "<tr><td colspan='" + colNum + "' class='no-data'>Нет записей</td></tr>";
    //for (i = 0; i < rowCount; i++) $("#" + table + " tr").eq(0).remove();
    $(row).appendTo(tableBody);
}


function addBranch(code, branch, t="model") {
    menu = "";
    if (t == "model") menu = "<span style='font-size: 15px; color: yellowgreen; display: none' onclick='tr.addGroup(this.parentElement)' id='a" + branch.id + "'><i class='fas fa-plus-circle menu-btn'></i></span><span style='font-size: 15px; color: dodgerblue; display: none' onclick='tr.editGroup(this.parentElement, " + branch.id + ")'  id='e" + branch.id + "'><i class='fas fa-pencil-alt menu-btn'></i></span><span style='font-size: 15px; color: red; display: none' onclick='tr.delGroup(this.parentElement)' id='d" + branch.id + "'><i class='fas fa-minus-circle menu-btn'></i></span>";
    code = code + "<li id=" + branch.id + "><span class='txt'>" + branch["name"] + menu + "</span>";
    if (branch["nodes"] != undefined) {
        code = code + "<ul>";
        for (br in branch["nodes"]) {
            code = addBranch(code, branch["nodes"][br], t);
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
    if ($('#form')[0].checkValidity()) {
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
}

function validateDemand() {
    var err = true;
    err = err && ($("#date").val() != "");
    return err;
}

function saveDemand(isDemand) {
    if ($('#form')[0].checkValidity()) {
        goods = {};
        $("#add_goods").find(".good-item").each(function (item) {
            goods[item] = {};
            goods[item]['product'] = $(this).find(".goodInp").eq(0).prop("name");
            //goods[item]['name'] = $(this).find("select").eq(0).val();
            goods[item]['unit'] = $(this).find("select").eq(0).val();
            goods[item]['num'] = $(this).find("input").eq(1).prop("value");
        });
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'save_demand/',
            data: {
                'consumer': $("#consumer").val(),
                'provider': $("#provider").val(),
                'donor': $("#donor").val(),
                'acceptor': $("#acceptor").val(),
                'date': $("#date").prop('value'),
                'goods': JSON.stringify(goods),
                'is_demand': isDemand
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
}

function saveSupply() {
    if ($('#form')[0].checkValidity()) {
        goods = {};
        cause = $("#cause").val();
        var operation = isSupply ? '0' : '1';
        $("#add_goods").find(".good-item").each(function (item) {
            goods[item] = {};
            goods[item]['product'] = $(this).find(".goodInp").eq(0).prop("name");
            //obj = this.nextElementSibling;
            goods[item]['unit'] = $(this).find("select").eq(0).val();
            goods[item]['num'] = $(this).find("input").eq(1).prop("value");
        });
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'save_supply/',
            data: {
                'consumer': $("#consumer").val(),
                'acceptor': $("#acceptor").val(),
                'date': $("#date").prop('value'),
                'goods': JSON.stringify(goods),
                'operation': operation,
                'cause': $("#cause").val()
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
}

function saveGood() {
    if ($('#form')[0].checkValidity()) {
        units = {};
        $("#units").find(".unit").each(function (item) {
            id = $(this).prop('id');
            units[id] = {};
            units[id]['coeff'] = $(this).find(":input[type='number']").eq(0).prop("value");
            units[id]['applicable'] = !$(this).find(":input[type='checkbox']").eq(0).prop("checked");
            units[id]['isBase'] = $(this).find(":input[type='radio']").eq(0).prop("checked");
        });
        names = {};
        $("#names").find(".name").each(function (item) {
            names[item] = {};
            names[item]['name'] = $(this).find(":input[type='text']").eq(0).prop("value");
            names[item]['type'] = $(this).find(".type").eq(0).prop("value");
            names[item]['area'] = $(this).find(".area").eq(0).prop("value");
        });
        props = {};
        $("#props").find(".prop").each(function (item) {
            id = $(this).prop('id');
            props[id] = {};
            props[id]['value'] = $(this).find(".value").eq(0).val();
            props[id]['visible'] = !$(this).find(".visible").eq(0).prop("checked");
            props[id]['editable'] = !$(this).find(".editable").eq(0).prop("checked");
            props[id]['applicable'] = !$(this).find(".applicable").eq(0).prop("checked");
        });
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'save_good/',
            data: {
                'name': $('#name').prop('value'),
                'model': $("#model option:selected").val(),
                'counter': $("#counter option:selected").val(),
                'names': JSON.stringify(names),
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
    else {
        $('<input type="submit">').hide().appendTo("#form").click().remove();
    }
}

function editGood(id) {
    var pk = id;
    units = {};
    $("#e_units").find(".unit").each(function (item) {
        id = $(this).prop('id');
        units[id] = {};
        units[id]['coeff'] = $(this).find(":input[type='number']").eq(0).prop("value");
        units[id]['isBase'] = $(this).find(":input[type='radio']").eq(0).prop("checked");
    });
    props = {};
    $("#e_props").find(".prop").each(function (item) {
        id = $(this).prop('id');
        props[id] = {};
        props[id]['value'] = $(this).find(".value").eq(0).val();
    });
    names = {};
    $("#e_names").find(".name").each(function (item) {
        names[item] = {};
        names[item]['name'] = $(this).find(":input[type='text']").eq(0).prop("value");
        names[item]['type'] = $(this).find(".type").eq(0).prop("value");
        names[item]['area'] = $(this).find(".area").eq(0).prop("value");
    });
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'edit_good/',
        data: {
            'id': pk,
            'name': $('#e_name').prop('value'),
            'counter': $("#e_counter option:selected").val(),
            'names': JSON.stringify(names),
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

function Tree(tree, t) {
    this.t = t;
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
        code = code + addBranch(code, this.tree[0]["nodes"][1], self.t);
        $(code).appendTo("#tree");
    };

    this.updEvent = function () {
        $("#tree li").unbind('mouseover');
        $("#tree li").unbind('mouseout');
        if (self.t != 'goods') {
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
        }
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
    $("#tree li").each(function (event) {
        id = $(this).prop("id");
        $("#a" + id).hide();
        $("#e" + id).hide();
        $("#d" + id).hide();
        //event.stopPropagation();
    });
    this.updEvent();
    $("#tree li").click(function (event) {
        id = $(this).prop("id");
        self.selected = id;
        $("#tree span").removeClass('active');
        obj = $(this).children("span");
        $(this).children("span").eq(0).addClass('active');
        $("#group option[value=" + id + "]").prop('selected', true);
        changeGroup(self.t);
        if (self.t == 'goods'){
            $("#model").find("option").show();
            $("#model").find("option").prop("selected", false);
            if (self.selected != 1) {
                $("#model").find("[name="+ self.selected + "]").prop('selected', true);
                $("#model").find("[name!="+ self.selected + "]").hide();
            }
        }
        //event.stopPropagation();
    });
}

function changeGroup(t) {
    if (t == "goods") {
        data = goods;
        gInf = function (id, isEdit = true) {
            getGoodInf(id, isEdit);
        };
        delObj = function (name, obj) {
            confirmDel(name, obj);
        }
    }
    else {
        data = models;
        gInf = function (id, isEdit = true) {
            getInf(id, isEdit);
        };
        delObj = function (name, obj) {
            confirmDel(name, obj);
        }
    }

    $("#goods-body").html("");
    for (m in data) {
        if (data[m].group == tr.selected || tr.selected == 1) {
            id = t == "goods" ? "<td>" + data[m].article + "</td>" : "";
            $("<tr id=" + data[m].id + ">" + id + "<td  onclick='gInf(" + data[m].id + ", false)'>" + data[m].name + "</td><td><span onclick='gInf(" + data[m].id + ")'><i title='Редактировать' class='fas fa-edit menu-btn'></i></span><span onclick='delObj(\"" + data[m].name + "\", this.parentElement)'><i title='Удалить' class='fas fa-trash-alt menu-btn'></i></span></td></tr>").appendTo("#goods-body");
        }
    }
    if ($("#goods-body tr").length == 0) $("#goods-body").html("<tr><td class='no-data' align='center' colspan='3'>Нет записей</td></tr>");
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
            $("#del_modal").modal('toggle');
        }
    });
};

function delCounter(obj) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'del_counter/',
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
            $("#del_modal").modal('toggle');
        }
    });
};

function delProp(obj) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'del_prop/',
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
            $("#del_modal").modal('toggle');
        }
    });
};

function delGood(obj) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'del_good/',
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
            $("#del_modal").modal('toggle');
        }
    });
};

function getDefault(sel) {
    t = $("option:selected", sel).prop("class");
    id = $("option:selected", sel).val();
    code = "<h6 class='addDefault'>Значение по умолчанию ";
    if (t == "0") {
        code = code + "<input type='number' class='form-control form-control-sm default' />";
    }
    else if (t == "1") {
        code = code + "<input type='text' class='form-control form-control-sm default' />";
    }
    else {
        code = code + "<select class='form-control form-control-sm default'>";
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
                "<button class='btn btn-success btn-sm' onclick='addEl();return false;' data-target='#newComp'>Добавить элемент множества</button>" +
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

function getModelInfo() {
    var code = "";
    id = $("#model").val();
    $("#units").html("");
    $("#props").html("");
    //получение единиц измерения
    for (u in models[id]['units']) {
        code = code + "<div class='unit'  id='" + u + "'><div class='form-inline'><div class='form-group col-md-6'><h6>- " + models[id]['units'][u].name + "</h6></div><div class='form-group inline-group col-md-6'>Коэффициент <input type='number' step='0.001' class='form-control form-control-sm inline-el' required/></div></div>";
        code = code + "<div class='form-inline'><div class='form-group col-md-6'><input type='checkbox' class='form-control' /> <span class='inline-el'>Неприменимая</span></div><div class='form-group col-md-6'><input type='radio' name='isBase' class='form-control'/><span class='inline-el'> Базовая</span></div></div></div>";
    }
    $(code).appendTo("#units");
    //получение свойств
    code = "";
    for (p in models[id]['props']) {
        if (!models[id]['props'][p]['visible']) checkedV = "checked";
        else checkedV = "";
        if (!models[id]['props'][p]['editable']) checkedE = "checked";
        else checkedE = "";
        code = code + "<div class='prop'  id='" + p + "'><div class='form-inline'><div class='form-group col-md-3'><h6>- " + models[id]['props'][p].name + "</h6></div><div class='form-group col-md-6'>" + getPropCode(models[id]['props'][p]['type'], models[id]['props'][p]['default'], models[id]['props'][p]['choises']) + "</div></div>";
        code = code + "<div class='form-inline inline-el'><input type='checkbox' " + checkedV + " class='form-control visible' /> <span class='inline-el'>Скрытое</span><input type='checkbox' " + checkedE + " class='form-control editable'/><span class='inline-el'> Неизменяемое</span><input type='checkbox'  class='form-control applicable'/><span class='inline-el'> Неприменимое</span></div></div>";
    }
    $(code).appendTo("#props");
}

function getPropCode(t, value = "", choises = null, editable = true) {
    var code = "";
    var disabled = editable ? "" : "disabled";
    switch (t) {
        case 0:
            code = "<input type='number' step='0.001' class='form-control form-control-sm inline-el value' value='" + value + "' required " + disabled + "/>";
            break;
        case 1:
            code = "<input type='text' class='form-control inline-el form-control-sm value' value='" + value + "' required " + disabled + "/>";
            break;
        case 2:
            code = "<select class='form-control form-control-sm inline-el value'" + disabled + ">";
            for (c in choises) {
                if (c == value) {
                    code = code + "<option value='" + c + "' selected>" + choises[c] + "</option>";
                }
                else code = code + "<option value='" + c + "'>" + choises[c] + "</option>";
            }
            code = code + "</select>";
            break;
    }
    return code;
}

function openClose(obj, arrow) {
    $("#" + obj).toggle();
    $(arrow).toggleClass("fa-angle-up fa-angle-down");
}

function GTree(tree, t) {
    this.t = t;
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
        $("#tree li").each(function(item){
            id = $(this).prop("id");
            if (id[0] == 'g') {
                $(this).addClass("good-li");
            }
        });
    };

    this.makeTree = function () {
        code = "";
        code = code + addGBranch(code, this.tree[0]["nodes"][1]);
        $(code).appendTo("#tree");
    };

    this.init();
    $("#tree li").click(function (event) {
        id = $(this).prop("id");
        self.selected = id;
        $("#tree span").removeClass('active');
        obj = $(this).children("span");
        $(this).children("span").eq(0).addClass('active');
        $("#group option[value=" + id + "]").prop('selected', true);
        if (id[0] == 'g') {
            $("#selectBtn").prop("disabled", false);
            self.selected = id.substring(2);
        }
        else {
            $("#selectBtn").prop("disabled", true);
        }
        //event.stopPropagation();
    });
    $("#tree li").dblclick(function (event) {
        $("#selectBtn").click();
    });
}

function STree(tree) {
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
        code = code + addGBranch(code, this.tree[0]["nodes"][1]);
        $(code).appendTo("#tree");
    };

    this.init();
    $("#tree li").click(function (event) {
        id = $(this).prop("id");
        self.selected = id;
        $("#tree span").removeClass('active');
        obj = $(this).children("span");
        $(this).children("span").eq(0).addClass('active');
        self.changeStockGroup();
        //event.stopPropagation();
    });

    this.changeStockGroup = function () {
        stock = $("#stock").val();
        code = "";
        for (r in goods[self.selected][stock]) {
            code = code + "<tr id='g-" + r + "'><td align=\"center\"><span style='font-size: 20px; color: green'\n" +
                "                          onclick=\"openGood(" + r + ", this)\"><i class='fas fa-caret-down'></i></span></td><td>" + goods[self.selected][stock][r].code + "</td><td>" + goods[self.selected][stock][r].name + "</td><td>" + goods[self.selected][stock][r].amount + "</td><td>" + goods[self.selected][stock][r].unit + "</td><td>" + goods[self.selected][stock][r].cost + "</td></tr>";
        }
        if (code == "") code = "<tr><td colspan=6 class='no-data' align='center'>Нет записей</td></tr>";
        $("#goods-body").html(code);
    }

    this.searchProd = function (text) {
        code = "";
        if (text == "") {
            self.changeStockGroup();
        }
        else {
            for (r in goods[self.selected][stock]) {
                if (goods[self.selected][stock][r].name.toUpperCase().indexOf(text.toUpperCase()) != -1 || goods[self.selected][stock][r].code.toUpperCase().indexOf(text.toUpperCase()) != -1) {
                    code = code + "<tr id='g-" + r + "'><td align=\"center\"><span style='font-size: 20px; color: green'\n" +
                        "                          onclick=\"openGood(" + r + ", this)\"><i class='fas fa-caret-down'></i></span></td><td>" + goods[self.selected][stock][r].code + "</td><td>" + goods[self.selected][stock][r].name + "</td><td>" + goods[self.selected][stock][r].amount + "</td><td>" + goods[self.selected][stock][r].unit + "</td><td>" + goods[self.selected][stock][r].cost + "</td></tr>";
                }
            }
            if (code == "") code = "<tr><td colspan=6 class='no-data' align='center'>Нет записей</td></tr>";
            $("#goods-body").html(code);
        }
    }
}

function addGBranch(code, branch) {
    code = code + "<li id=" + branch.id + "><span class='txt'>" + branch["name"] + "</span>";
    if (branch["nodes"] != undefined) {
        code = code + "<ul>";
        for (br in branch["nodes"]) {
            code = addGBranch(code, branch["nodes"][br]);
        }
        code = code + "</ul>";
    }
    code = code + "</li>";
    return code;
}

function openGood(id, obj) {
    $(obj.firstElementChild).toggleClass("fa-caret-down fa-caret-up");
    $("#product-info").remove();
    if ($(obj.firstElementChild).hasClass("fa-caret-up")) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: 'get_prod_info/',
            data: {
                'id': id,
                'stock': $("#stock").val()
            },
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function onAjaxSuccess(data) {
                data = JSON.parse(data);
                var period = $("#period").val();
                var code = "<div class='tab-pane fade show active' id='names' role='tabpanel' aria-labelledby='names-tab'><table class=\"table table-sm table-bordered\">\n" +
                    "                        <thead>\n" +
                    "                        <tr><th>Имя</th><th>Тип</th><th>Область</th></tr>\n" +
                    "                        </thead><tbody>";
                for (n in data.names) {
                    code = code + "<tr><td>" + data.names[n].name + "</td><td>" + data.names[n].type + "</td><td>" + data.names[n].area + "</td></tr>";
                }
                names = code + "</tbody></table></div>";
                units = " <div class='tab-pane fade' id='units' role='tabpanel' aria-labelledby='units-tab'>" +
                    "<table>\n" +
                    "<table class=\"table table-bordered\">\n" +
                    "                            <thead class=\"thead\">\n" +
                    "                            <tr>\n" +
                    "                                <th scope=\"col\">Количество</th>\n" +
                    "                                <th scope=\"col\">Ед. изм.</th>\n" +
                    "                            </thead>\n" +
                    "                            <tbody>\n";
                for (u in data['units']) {
                    units = units + "<tr><td>" + data['units'][u].amount + "</td><td>" + data['units'][u].unit + "</td></tr>"
                }
                units = units + "</tbody></table></div>";

                expNav = "<nav style=\"margin-top: 5px; margin-right: 0px\">\n" +
                    "                <ul class=\"pagination pagination-sm justify-content-end\" id=\"expectingNav\">\n" +
                    "                </ul>\n" +
                    "            </nav>";

                histNav = "<nav style=\"margin-top: 5px; margin-right: 0px\">\n" +
                    "                <ul class=\"pagination pagination-sm justify-content-end\" id=\"historyNav\">\n" +
                    "                </ul>\n" +
                    "            </nav>";


                expecting = " <div class='tab-pane fade' id='expecting' role='tabpanel' aria-labelledby='expecting-tab'>" +
                    "<table>\n" +
                    "<table class=\"table table-bordered\">\n" +
                    "                            <thead class=\"thead\">\n" +
                    "                            <tr>\n" +
                    "                                <th scope=\"col\">ВИН</th>\n" +
                    "                                <th scope=\"col\">Дата</th><th scope='col'>Операция</th><th scope='col'>Количество</th>\n" +
                    "                            </thead>\n" +
                    "                            <tbody id='expectingBody'>\n";
                for (u in data['expecting']) {
                    expecting = expecting + "<tr><td>" + data['expecting'][u].vin + "</td><td>" + data['expecting'][u].date + "</td><td>" + data['expecting'][u].operation + "</td><td>" + data['expecting'][u].amount + "</td></tr>";
                }
                if ($.isEmptyObject(data['expecting'])) expecting = expecting + "<tr><td colspan=5 align='center' class='no-data'>Нет записей</td></tr>";
                expecting = expecting + "</tbody></table>" + expNav + "</div>";

                prodHistory = " <div class='tab-pane fade' id='history' role='tabpanel' aria-labelledby='history-tab'>" +
                    "<table>\n" +
                    "<table class=\"table table-bordered\">\n" +
                    "                            <thead class=\"thead\">\n" +
                    "                            <tr>\n" +
                    "                                <th scope=\"col\">ВИН</th>\n" +
                    "                                <th scope=\"col\">Дата</th><th scope='col'>Операция</th><th scope='col'>Ед.изм.</th><th scope='col'>Количество</th>\n" +
                    "                            </thead>\n" +
                    "                            <tbody id='historyBody'>\n";
                for (u in data['history']) {
                    if (checkDatePeriod(data['history'][u].date, period)) prodHistory = prodHistory + "<tr><td>" + data['history'][u].vin + "</td><td>" + data['history'][u].date + "</td><td>" + data['history'][u].operation + "</td><td>" + data['history'][u].unit + "</td><td>" + data['history'][u].amount + "</td></tr>";
                }
                if ($.isEmptyObject(data['history'])) prodHistory = prodHistory + "<tr><td colspan=5 align='center' class='no-data'>Нет записей</td></tr>";
                prodHistory = prodHistory + "</tbody></table>" + histNav + "</div>";

                goodInfo = data['history'];

                code = "<tr id='product-info'><td colspan='6'><div class='add-info-good'>" +
                    "<ul class=\"nav nav-tabs\" id=\"myTab\" role=\"tablist\">\n" +
                    "  <li class=\"nav-item\">\n" +
                    "    <a class=\"nav-link active\" id=\"names-tab\" data-toggle=\"tab\" href=\"#names\" role=\"tab\" aria-controls=\"home\" aria-selected=\"true\">Имена</a>\n" +
                    "  </li>" +
                    "<li class=\"nav-item\">\n" +
                    "    <a class=\"nav-link\" id=\"units-tab\" data-toggle=\"tab\" href=\"#units\" role=\"tab\" aria-controls=\"units\" aria-selected=\"false\">Единицы измерения</a>\n" +
                    "  </li><li class=\"nav-item\">\n" +
                    "    <a class=\"nav-link\" id=\"expecting-tab\" data-toggle=\"tab\" href=\"#expecting\" role=\"tab\" aria-controls=\"expecting\" aria-selected=\"false\">Поступления/Отпуски</a>\n" +
                    "  </li><li class=\"nav-item\">\n" +
                    "    <a class=\"nav-link\" id=\"history-tab\" data-toggle=\"tab\" href=\"#history\" role=\"tab\" aria-controls=\"history\" aria-selected=\"false\">Приходы/Расходы</a>\n" +
                    "  </li></ul>\n" +
                    "<div class=\"tab-content\" id=\"myTabContent\">\n" + names + units + expecting + prodHistory +
                    "</div></div></tr>";
                $(obj.parentElement.parentElement).after(code);
                pag = new Pagination(3, "expectingBody", "expectingNav");
                pag2 = new Pagination(3, "historyBody", "historyNav");
            }
        });
    }
}

function saveInventory(stock) {
    $("#inventoryProds tr").each(function (item) {
        id = $(this).prop('id');
        if (inventoryGoods[id] == undefined) inventoryGoods[id] = {};
        inventoryGoods[id].amount = $("[name='amount']", this).val();
        inventoryGoods[id].cost = $("[name='cost']", this).val();
    });
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'save_inventory/',
        data: {
            'stock': stock,
            'inventory_goods': JSON.stringify(inventoryGoods),
            'date': $("#inventoryDate").prop('value'),
            'time': $("#inventoryTime").prop('value')
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

function getStockGoods(id) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'get_stock_goods/',
        data: {
            'id': id
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            inventoryGoods = {};
            var rows = JSON.parse(data);
            i = 0;
            code = "";
            for (r in rows) {
                code = code + "<tr id='" + r + "'><td>" + rows[r].article + "</td><td>" + rows[r].name + "</td><td>" + rows[r].unit + "</td><td><input class='form-control form-control-sm short-input' name='amount' type='number' value='" + rows[r].amount + "'/></td><td><input class='form-control form-control-sm short-input' name='cost' type='number' value='" + rows[r].cost.toFixed(1) + "'/></td><td></td>";
                inventoryGoods[r] = {
                    id: r,
                    amount: rows[r]['amount'],
                    cost: rows[r]['cost']
                }
            }
            $("#inventoryProds").html(code);
            $("#inventory").modal();
        }
    });
}

function getDemandGoods(id, t = "d") {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'get_demand_goods/',
        data: {
            'id': id,
            't': t
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            //$("#goods-body").html("");
            if (t == "d") addGoodsReq("goods-body", data);
            else addGoodsSh("goods-body", data);
            reqInfo[id] = {};
            var rows = JSON.parse(data);
            i = 0;
            for (r in rows) {
                if (rows[r]['article'] != undefined) {
                    reqInfo[id][i] = {
                        id: r,
                        article: rows[r]['article'],
                        name: rows[r]['name'],
                        amount: rows[r]['amount'],
                        balance: rows[r]['balance']
                    }
                    i++;
                }
            }
            curReq = id;
            $("#editReqBtn").prop('disabled', reqs[id].isEdited);
            $("#makeShipmentBtn").prop('disabled', false);
            $("#endShipmentBtn").prop('disabled', false);
            $("#makeSupplyBtn").prop('disabled', !rows['is_finished']);
            $(".table-selected").removeClass("table-selected");
            $("#l-" + id).addClass("table-selected");
            pag2 = new Pagination(10, "goods-body", "goodsNav");
        }
    });
}

function openSupply(isDonor) {
    id = curReq;
    code = "";
    for (r in reqInfo[id]) {
        code = code + "<tr id=" + reqInfo[id][r].id + "><td>" + reqInfo[id][r].article + "</td><td>" + reqInfo[id][r].name + "</td><td><input type='number' class='form-control form-control-sm' value=" + reqInfo[id][r].balance + " /></td></tr>";
    }
    $("#supply-body").html(code);
    $("#supply").modal();
    if (isDonor) operation = 1;
    else operation = 0;
    $("#supplyBtn").unbind('click');
    $("#supplyBtn").click(function () {
        var csrftoken = getCookie('csrftoken');
        goods = {};
        $("#supply-body").find("tr").each(function (item) {
            i = $(this).prop('id');
            if ($(this).find('input').eq(0).prop("value") != null) goods[i] = {
                "id": i,
                "amount": $(this).find('input').eq(0).prop("value")
            };
        });
        $.ajax({
            type: "POST",
            url: 'save_stock_operation/',
            data: {
                'id': id,
                'operation': operation,
                'cause': 1,
                'goods': JSON.stringify(goods),
                'isDonor': isDonor
            },
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function onAjaxSuccess() {
                window.location.reload();
            }
        });
    });
}

function endShipment() {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'finish_shipment/',
        data: {
            'id': curReq
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess() {
            document.location.reload();
        }
    });
}

function saveChangedStock(obj, isDonor) {
    stock = $("#editStock").val();
    id = obj.parentElement.parentElement.parentElement.id.substr(2);
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'save_changed_stock/',
        data: {
            'id': id,
            'stock': stock,
            'is_donor': isDonor
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            var code = "<span class='stock'>" + $("#editStock option:selected").text() + "</span><span class='inline-el' onclick='editStock(this)'><i class='fas fa-edit'></i></span>";
            $(obj.parentElement.parentElement).html(code);
        }
    });
}

function saveStatus(obj) {
    status = $("option:selected", obj).val();
    id = obj.parentElement.parentElement.parentElement.id.substr(2);
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: 'save_status/',
        data: {
            'id': id,
            'status': status
        },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data) {
            obj.parentElement.parentElement.innerHTML = $("option:selected", obj).text();

        }
    });
}

function getStocks(counter) {
    if (counter == 'donor') {
        select = $("#donor");
        id = $("#provider").val();
    }
    else {
        select = $("#acceptor");
        id = $("#consumer").val();
    }
    code = "<option value=''>-----</option>";
    for (s in stocks) {
        if (stocks[s].counter == id) {
            code = code + "<option value='" + stocks[s].pk + "'>" + stocks[s].stock + "</option>";
        }
    }
    $(select).html("");
    $(code).appendTo(select);
}

function addGoodField() {
    code = "<div class='form-row good-item'>\n" +
        "                        <div class='form-group col-md-6'>\n" +
        "                            <div class='form-inline'>\n" +
        "                        <div class='autocomplete' style='width:335px;'>\n" +
        "                            <input id='myInput' placeholder='Наименование товара' style='width:335px;' class='form-control form-control-sm  goodInp' type='text' name='myCountry' required>\n" +
        "                        </div>\n" +
        "                        <button class='btn btn-outline-info'\n" +
        "                                onclick='inp = this.previousSibling.previousSibling.firstChild.nextSibling;return false;'\n" +
        "                                data-toggle='modal' data-target='#tree-div'><span\n" +
        "                                style='font-size: 15px;' onclick=''><i class='fas fa-stream'></i></span></button></div></div>\n" +
        "                        <div class='form-group col-md-3'>\n" +
        "                           <select class='form-control form-control-sm' required><option value='' readonly>Ед.изм.</option>\n" +
        "                        </select></div><div class='form-group col-md-3'>\n" +
        "                            <div class='form-inline'><input placeholder='Кол-во' type='number' class='form-control form-control-sm' style='max-width: 145px' id='date' required/> <span onclick='this.parentElement.parentElement.parentElement.remove()' class='inline-el'><i title='Удалить' class='fas fa-trash-alt menu-btn'></i></span></div></div>\n" +
        "                    </div>";
    $(code).appendTo("#add_goods");
    autocomplete(document.getElementsByClassName("goodInp")[document.getElementsByClassName("goodInp").length - 1], goods);
}

function addDots() {
    code = "<span style='font-size: 17px; color: #CCCCCC' ><i class='fas fa-ellipsis-v'></i></span>";
    $(code).appendTo("#add_goods");
}

function getUnits(obj) {
    id = obj.name.substr(2);
    select = obj.parentElement.parentElement.parentElement.nextElementSibling.childNodes[1];
    code = "<select class='form-control form-control-sm unit'>";
    for (u in units) {
        if (units[u].product == id && units[u].applicable) {
            if (units[u].is_base) code = code + "<option value='" + units[u].pk + "' selected>" + units[u].unit + "</option>";
            else code = code + "<option value='" + units[u].pk + "'>" + units[u].unit + "</option>";
        }
    }
    code = code + "</select>";
    select.innerHTML = code;
}

function setNameId(id, obj) {
    obj.name = goods_inf[id];
    if (obj.parentElement.parentElement.parentElement.nextElementSibling != null) getUnits(obj);
}

function setGoodName(obj) {
    for (g in goods_inf) {
        if (goods_inf[g] == ("0_" + tr.selected)) {
            obj.value = goods[g];
            setNameId(g, obj);
        }
    }
}

function parseDate(string) {
    return new Date(string.substr(6, 4), string.substr(3, 2) - 1, string.substr(0, 2));
}

function checkDatePeriod(dateSring, period) {
    var date = parseDate(dateSring);
    var now = new Date();
    if (period == 0) return true;
    else if (period == 1) {
        return date.getFullYear() == now.getFullYear() && date.getMonth() == now.getMonth() && date.getDate() == now.getDate();
    }
    else if (period == 2) {
        startDate = new Date();
        startDate.setDate(startDate.getDate() - 7);
        return date > startDate;
    }
    else if (period == 3) {
        startDate = new Date();
        startDate.setDate(startDate.getDate() - 31);
        return date > startDate;
    }
    else {
        startDate = new Date();
        startDate.setDate(startDate.getDate() - 365);
        return date > startDate;
    }
}

function Pagination(max, table, nav) {
    this.maxRecs = max;
    this.tableBody = table;
    var self = this;
    this.trCount = 0;
    this.nav = nav;
    this.pageNum = 0;
    this.curPage = 1;

    this.initPagination = function () {
        self.trCount = $("#" + self.tableBody + " tr").length;
        if (self.trCount > self.maxRecs) {
            $("#" + self.tableBody + " tr:gt(" + (self.maxRecs - 1) + ")").hide();
        }
        self.pageNum = Math.ceil(self.trCount / self.maxRecs);
        var paginationCode = "<li class='page-item disabled'><span class='page-link'>Предыдущая</span></li>";
        for (i = 0; i < self.pageNum; i++) {
            if (i == 0) paginationCode = paginationCode + "<li class='page-item active'><a class='page-link' href='#'>1</a></li>";
            else paginationCode = paginationCode + "<li class='page-item'><a class='page-link' href='#'>" + (i + 1) + "</a></li>";
        }
        paginationCode = paginationCode + "<li class='page-item'><span class='page-link'>Следующая</span></li>";
        $("#" + self.nav).html(paginationCode);
        $("#" + self.nav + " li").each(function (item) {
            $(this).click({item: item}, function (eventObject) {
                self.goToPage(eventObject.data.item);
            });
        });
        self.goToPage(1);
    };

    this.goToPage = function (page) {
        if (page == 0) page = self.curPage - 1;
        if (page == (self.pageNum + 1)) page = self.curPage + 1;
        $("#" + self.nav + " li").removeClass("active");
        $("#" + self.nav).find('li').eq(page).addClass("active");
        $("#" + self.tableBody + " tr").hide();
        firstTr = (page - 1) * self.maxRecs;
        lastTr = (page * self.maxRecs) - 1;
        if (firstTr == 0) $("#" + self.tableBody + " tr:lt(" + (lastTr + 1) + ")").show();
        else {
            $("#" + self.tableBody + " tr:gt(" + (firstTr - 1) + ")").show();
            $("#" + self.tableBody + " tr:gt(" + lastTr + ")").hide();
        }
        self.curPage = page;
        if (self.curPage == self.pageNum) {
            $("#" + self.nav + " li").last().addClass("disabled");
            $("#" + self.nav + " li").last().off();
            $("#" + self.nav + " li").first().removeClass("disabled");
            $("#" + self.nav + " li").first().off();
            $("#" + self.nav + " li").first().on('click', function () {
                self.goToPage(0);
            });
        }
        if (self.curPage == 1) {
            $("#" + self.nav + " li").first().addClass("disabled");
            $("#" + self.nav + " li").first().off();
            if (self.curPage != self.pageNum) {
                $("#" + self.nav + " li").last().removeClass("disabled");
                $("#" + self.nav + " li").last().off();
                $("#" + self.nav + " li").last().on('click', function () {
                    self.goToPage(self.pageNum + 1);
                });
            }
        }
        else if (self.curPage != self.pageNum) {
            $("#" + self.nav + " li").first().removeClass("disabled");
            $("#" + self.nav + " li").last().removeClass("disabled");
            $("#" + self.nav + " li").first().off();
            $("#" + self.nav + " li").first().on('click', function () {
                self.goToPage(0);
            });
            $("#" + self.nav + " li").last().off();
            $("#" + self.nav + " li").last().on('click', function () {
                self.goToPage(self.pageNum + 1);
            });
        }
    };

    this.initPagination();

}

function openModalSupply() {
    if (isSupply) {
        $("#supplyTitle").text("Создание поставки");
        $("#counterLabel").text("Потребитель");
        $("#dateLabel").text("Дата поставки");
    }
    else {
        $("#supplyTitle").text("Выбытие");
        $("#counterLabel").text("Поставщик");
        $("#dateLabel").text("Дата выбытия");
    }
    $("#add_supply").modal();
}

function changePeriod(){
    var period = $("#period").val();
    var code = "";
    for (u in goodInfo) {
        if (checkDatePeriod(goodInfo[u].date, period)) code = code + "<tr><td>" + goodInfo[u].vin + "</td><td>" + goodInfo[u].date + "</td><td>" + goodInfo[u].operation + "</td><td>" + goodInfo[u].unit + "</td><td>" + goodInfo[u].amount + "</td></tr>";
    }
    if (code == "") code = "<tr><td colspan=5 align='center' class='no-data'>Нет записей</td></tr>";
    $("#historyBody").html(code);
    pag2 = new Pagination(3, "historyBody", "historyNav");
}

Date.prototype.toDateInputValue = (function() {
    var local = new Date(this);
    local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
    return local.toJSON().slice(0,10);
});



