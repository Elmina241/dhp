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
            $("#stock-tbody tr").each(function(){
                $(this).click(function() {
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

function initTree(){
        makeTree($("#tree_data").prop("value"));
        $('#tree').treed({openedClass:'fa-folder-open', closedClass:'fa-folder'});
        $("#tree li").click(function(event){
            /*id = $(this).prop("id");
            addGoods("goods-body", goods[id]);*/
            event.stopPropagation();
        });
       // document.getElementById("1").click();
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

function addGoods(table, rows) {
    row = "";
    for (r in rows) {
        row = row + "<tr id=id-" + r + ">";
        for (d in rows[r]){
            if (rows[r][d] == null){
                row = row + "<td>--</td>";
            }
            else row = row + "<td>" + rows[r][d] + "</td>";
        }
        row = row + "</tr>";
    }
    var tableBody = $("#" + table);
    //var rowCount = $("#" + table + " tr").length;
    $(tableBody).html("");
    if (row == ""){
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
        for (d in rows[r]){
            if (rows[r][d] == null){
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

function makeTree(data){
    var tree = JSON.parse(data);
    code = "";
    code = code + addBranch(code, tree[0]["nodes"][1]);
    $(code).appendTo("#tree");
}

function addBranch(code, branch){
    menu = "<span style='font-size: 20px; color: yellowgreen;'><i class='fas fa-plus-circle'></i></span>";
    code = code + "<li id="+ branch.id +">" + branch["name"] + " " + menu;
    if (branch["nodes"] != undefined){
        code = code + "<ul>";
        for (br in branch["nodes"]){
            code = addBranch(code, branch["nodes"][br]);
        }
        code = code + "</ul>";
    }
    code = code  + "</li>";
    return code;
}