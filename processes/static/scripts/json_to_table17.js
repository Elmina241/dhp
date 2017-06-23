function getComponents(c, m, f_c, f) {
  var table = document.getElementById("materials");
  var length = table.rows.length;
  for (i = 2; i < length; i++) table.deleteRow(2);
  var sel = document.getElementById("formula");
  var sel_id = sel.value;
  var components = JSON.parse(c);
  var materials = JSON.parse(m);
  var formulas = JSON.parse(f);
  var f_comp = JSON.parse(f_c);
  var amm = $("#ammount").val();
  var tbody = document.getElementById("materials").getElementsByTagName("TBODY")[0];
  for (i = 0; i < f_comp.length; i++){
    if (f_comp[i].fields.formula == sel_id){
      var row = document.createElement("TR");
      row.setAttribute('id', f_comp[i].fields.mat);
      var td1 = document.createElement("TD");
      var td2 = document.createElement("TD");
      var td3 = document.createElement("TD");
      var td4 = document.createElement("TD");
      var td5 = document.createElement("TD");
      var input = document.createElement("input");
      input.type = "number";
      input.name = getCode(f_comp[i].fields.mat, materials);
      input.setAttribute('onchange', "changeWater();return false;");
      input.setAttribute('step', "0.01");
      input.value = (f_comp[i].fields.ammount/1020*amm).toFixed(2);
      var bounds = getMinMax(components, getComp(formulas, f_comp[i].fields.formula), f_comp[i].fields.mat);
      td1.appendChild(document.createTextNode(getCode(f_comp[i].fields.mat, materials)));
      td2.appendChild(document.createTextNode(getName(f_comp[i].fields.mat, materials)));
      td3.appendChild(document.createTextNode(((bounds.min/100)*amm).toFixed(2)));
      td4.appendChild(document.createTextNode(((bounds.max/100)*amm).toFixed(2)));
      input.setAttribute('min', ((bounds.min/100)*amm).toFixed(2));
      input.setAttribute('max', ((bounds.max/100)*amm).toFixed(2));
      td5.appendChild(input);
      row.appendChild(td1);
      row.appendChild(td2);
      row.appendChild(td3);
      row.appendChild(td4);
      row.appendChild(td5);
      tbody.appendChild(row);
    }
  }
};




//получить номер состава
function getComp(f, f_id){
  var i = 0;
  var id = "0";
  while (i < f.length && id == "0"){
    if (f[i].pk == f_id) id = f[i].fields.composition;
    i++;
  }
  return id;
}

function getCode(m_id, m) {
  var i = 0;
  var id = "0";
  while (i < m.length && id == "0"){
    if (m[i].pk == m_id) id = m[i].fields.code;
    i++;
  }
  return id;
};

function changeWater() {
  var ammount = document.getElementById("ammount").value;
  var water1 = document.getElementById("water");
  var water2 = document.getElementById("water2");
  var w_a = document.getElementById("water_amm");
  var tbody = document.getElementById("materials");
  var mat_ammount = 0;
  for (i=2; i<tbody.rows.length; i++){
    var m = tbody.rows[i].children[4].children[0].valueAsNumber;
    if (isNaN(m)) m = 0;
    mat_ammount = mat_ammount + m;
  }
  water1.textContent = (ammount - mat_ammount).toFixed(2);
  if (w_a != null) w_a.value = (ammount - mat_ammount).toFixed(2);
  if (water2 != null) water2.textContent = (ammount - mat_ammount).toFixed(2);
  if ($('#materials2').length == 0) var table = $('#materials').tableToJSON();
  else var table = $('#materials2').tableToJSON();
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
};

function getAmmount() {
  var ammount = document.getElementById("textAmm");
  var tbody = document.getElementById("materials2");
  var mat_ammount = 0;
  for (i=1; i<tbody.rows.length; i++){
    var m = parseFloat(tbody.rows[i].children[4].textContent);
    if (isNaN(m)) m = 0;
    mat_ammount = mat_ammount + m;
  }
  ammount.textContent = mat_ammount.toFixed(2) + " кг";
  $("#list_amm").attr('value', mat_ammount.toFixed(2));
};

function getName(m_id, m) {
  var i = 0;
  var name = "0";
  while (i < m.length && name == "0"){
    if (m[i].pk == m_id) name = m[i].fields.name;
    i++;
  }
  return name;
};

function getMinMax(c, comp, mat, fComp, formula){
  var i=0;
  var bounds = {
    min: 0,
    max: 0,
    amm: 0
  };
  var flag = false;
  while (i < c.length && !flag){
    if (c[i].fields.mat == mat && c[i].fields.comp == comp){
      bounds.min = c[i].fields.min;
      bounds.max = c[i].fields.max;
      flag = true;
    }
    i++;
  }
  i=0;
  if (fComp!=undefined){
    var flag = false;
    while (i < fComp.length && !flag){
      if (fComp[i].fields.mat == mat && fComp[i].fields.formula == formula){
        bounds.amm = fComp[i].fields.ammount;
        flag = true;
      }
      i++;
    }
  }
  return bounds;
}


//Изменяет не только минимум и максимум, но и количество компонента в составе
function changeMinMax(c, f, f_c){
  var components = JSON.parse(c);
  var form = JSON.parse(f);
  var fComp = JSON.parse(f_c);
  var amm = $("#ammount").val();
  var comp = getComp(form, $("#formula").val());
  var size = $("#materials tr").size();
  for (var i = 2; i < size; i++){
    var row = $("#materials tr").eq(i);
    var code = row.attr("id");
    var bounds = getMinMax(components, comp, code, fComp, $("#formula").val());
    $("#materials tr").eq(i).find('td').eq(2).text(((bounds.min/100)*amm).toFixed(2));
    $("#materials tr").eq(i).find('td').eq(3).text(((bounds.max/100)*amm).toFixed(2));
    $("#materials tr").eq(i).find('td').eq(4).text(((bounds.amm/1020)*amm).toFixed(2));
    $("#materials tr").eq(i).find('input').attr('min', ((bounds.min/100)*amm).toFixed(2));
    $("#materials tr").eq(i).find('input').attr('max', ((bounds.max/100)*amm).toFixed(2));
  }
}

function changeMinMax2(c, c_id){
  var components = JSON.parse(c);
  //var form = JSON.parse(f);
  var amm = $("#ammount").val();
  //var comp = getComp(form, $("#formula").val());
  var size = $("#materials tr").size();
  for (var i = 2; i < size; i++){
    var row = $("#materials tr").eq(i);
    var code = row.attr("id");
    var bounds = getMinMax(components, c_id, code);
    $("#materials tr").eq(i).find('td').eq(2).text(((bounds.min/100)*amm).toFixed(2));
    $("#materials tr").eq(i).find('td').eq(3).text(((bounds.max/100)*amm).toFixed(2));
  }
}

//функция для получения загрузочного листа
function getComponents2(c, m, l_c, l_id, t_name) {
  var tbody = $("#"+t_name+" tbody")[0];
  var materials = JSON.parse(m);
  var components = JSON.parse(c);
  var l_comp = JSON.parse(l_c);
  var amm = $("#ammount").val();
  for (i = 0; i < l_comp.length; i++){
      var mat_code = getCode(l_comp[i].fields.mat, materials);
      var mat_amm = l_comp[i].fields.ammount;
      var bounds = getMinMax(components, l_id, l_comp[i].fields.mat);
      var mat_name = getName(l_comp[i].fields.mat, materials);
      var min = ((bounds.min/100)*amm).toFixed(2);
      var max = ((bounds.max/100)*amm).toFixed(2);
      if (t_name=='materials'){
        $('<tr id='+ l_comp[i].fields.mat + '><td>' + mat_code + '</td><td>' + mat_name + '</td><td>' + min + '</td><td>' + max + "</td><td><input type='number' name=" + mat_code + " onchange='changeWater();return false;' min=" + min + " max=" + max + " step='0.01' value=" + mat_amm + '>').appendTo(tbody);
      }
      else{
        $('<tr id='+ l_comp[i].fields.mat + '><td>' + mat_code + '</td><td>' + mat_name + '</td><td>' + min + '</td><td>' + max + "</td><td>" + mat_amm + '</td>').appendTo(tbody);
      }
  }
};

//Функция для отображения загрузочного листа с составными компонентами
function getLoadList(loadList, t_name) {
  var tbody = $("#"+t_name+" tbody")[0];
  //var list = JSON.parse(loadList);
  var amm = $("#ammount").val();
  for (i in loadList){
      if (loadList[i].min!='-'){
        var min = ((loadList[i].min/100)*amm).toFixed(2);
        var max = ((loadList[i].min/100)*amm).toFixed(2);
      }
      else{
        var min = "-";
        var max = "-";
      }
      if (t_name=='materials'){
        $('<tr id='+ i + '><td>' + loadList[i].mat_code + '</td><td>' + loadList[i].mat_name + '</td><td>' + min + '</td><td>' + max + "</td><td><input type='number' name=" + loadList[i].mat_code + " onchange='changeWater();return false;' min=" + min + " max=" + max + " step='0.01' value=" + loadList[i].amount + '>').appendTo(tbody);
      }
      else{
        $('<tr id='+ i + '><td>' + loadList[i].mat_code + '</td><td>' + loadList[i].mat_name + '</td><td>' + min + '</td><td>' + max + "</td><td>" + loadList[i].amount + '</td>').appendTo(tbody);
      }
  }
};

/** Скрипты для страницы планирование **/
//Формирование таблицы состава в планировании
function getCompositionT(c, m, f_c, f) {
  var table = $("#materials tbody");
  var rowCount = $('#materials tr').length;
  for (i = 2; i < rowCount; i++) $('#materials tr').eq(2).remove();
  var sel = document.getElementById("formula");
  var sel_id = sel.value;
  var components = JSON.parse(c);
  var materials = JSON.parse(m);
  var formulas = JSON.parse(f);
  var f_comp = JSON.parse(f_c);
  var amm = $("#ammount").val();
  for (i = 0; i < f_comp.length; i++){
    if (f_comp[i].fields.formula == sel_id){
      var row = document.createElement("TR");
      var bounds = getMinMax(components, getComp(formulas, f_comp[i].fields.formula), f_comp[i].fields.mat);
      $("<tr id=" + f_comp[i].fields.mat + "><td>" + getCode(f_comp[i].fields.mat, materials) + "</td><td>" + getName(f_comp[i].fields.mat, materials) + "</td><td>" + ((bounds.min/100)*amm).toFixed(2) + "</td><td>" +
      + ((bounds.max/100)*amm).toFixed(2) + "</td><td name=" + getCode(f_comp[i].fields.mat, materials) + ">" + (f_comp[i].fields.ammount/1020*amm).toFixed(2) + "</td><td></td><tr>").appendTo(table);
    }
  }
};

//Получение списка загрузочных листов
function getListOfModels(lists) {
  var rowCount = $('#list option').length;
  for (i = 1; i < rowCount; i++) $('#list option:last').remove();
  var sel = document.getElementById("formula");
  var sel_id = sel.value;
  var modelLists = JSON.parse(lists);
  for (i = 0; i < modelLists.length; i++){
    if (modelLists[i].fields.formula == sel_id){
      $('#list').append("<option value=" + modelLists[i].pk + ">" + modelLists[i].pk + " " + $("#formula :selected").text() + "</option>");
    }
  }
};

//Получение макета загрузочного листа
function getModelList(m, m_c, compl) {
  var table = $("#loadList tbody");
  var rowCount = $('#loadList tr').length;
  for (i = 2; i < rowCount; i++) $('#loadList tr').eq(2).remove();
  var sel = document.getElementById("list");
  var sel_id = sel.value;
  var materials = JSON.parse(m);
  var m_comp = JSON.parse(m_c);
  var complComp = JSON.parse(compl);
  var amm = $("#ammount").val();
  for (i = 0; i < m_comp.length; i++){
    if (m_comp[i].fields.list == sel_id){
      var row = document.createElement("TR");
      var matAm = (m_comp[i].fields.ammount/100*amm).toFixed(2) ;
      if (m_comp[i].fields.compl == null){
        $("<tr id=" + m_comp[i].fields.mat + "><td>" + getCode(m_comp[i].fields.mat, materials) + "</td><td>" + getName(m_comp[i].fields.mat, materials) + "</td><td><input type='number' class='form-control' value=" + matAm + " name=" + getCode(m_comp[i].fields.mat, materials) + " onchange='changeMatAm();changeWaterP();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'>" + matAm + "</td>" + "</tr>").appendTo(table);
      }
      else{
        $("<tr id=" + m_comp[i].fields.compl + " name='compl'><td>" + getCode(m_comp[i].fields.compl, complComp) + "</td><td>" + getName(m_comp[i].fields.compl, complComp) + "</td><td><input type='number' class='form-control' value=" + matAm + " name=" + getCode(m_comp[i].fields.compl, complComp) + " onchange='changeMatAm();changeWaterL();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'>" + matAm + "</td>" + "</tr>").appendTo(table);
      }
      }
    }
    changeMatAm();
    changeWaterL();
    changeWaterT();
};

function changeWaterT() {
  var ammount = document.getElementById("ammount").value;
  var water1 = document.getElementById("water");
  var w_a = document.getElementById("water_amm");
  var tbody = document.getElementById("materials");
  var mat_ammount = 0;
  var mat_ammount2 = 0;
  for (i=2; i<tbody.rows.length; i++){
    var m = tbody.rows[i].children[4];
    if (m==undefined) m2 = 0;
    else  m2 = parseInt(m.textContent);
    mat_ammount = mat_ammount + m2;
    var m1 = tbody.rows[i].children[5];
    if (m1 == undefined) m2 = 0;
    else  m2 = parseInt(m1.textContent);
    if (isNaN(m2)) m2=0;
    mat_ammount2 = mat_ammount2 + m2;
  }
  document.getElementById("water2").textContent = (ammount - mat_ammount2).toFixed(2);
  water1.textContent = (ammount - mat_ammount).toFixed(2);
  if (w_a != null) w_a.value = (ammount - mat_ammount).toFixed(2);
  if ($('#materials2').length == 0) var table = $('#loadList').tableToJSON();
  else var table = $('#materials2').tableToJSON();
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
};

//Добавление реактива в загрузочный лист
function addMaterial(){
  var id = document.getElementById("material").selectedOptions[0].value
  var code = document.getElementById("material").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("material").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  $("#loadList tbody").append("<tr id=" + id + "><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td><input type='number' class='form-control' name=" + code + " onchange='changeMatAm();changeWaterL();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");
  $("#newComp").modal("hide");
}

function addComplComp(){
  var id = document.getElementById("complComp").selectedOptions[0].value
  var code = document.getElementById("complComp").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("complComp").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  $("#loadList tbody").append("<tr id=" + id + " name='compl'><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td><input type='number' class='form-control' name=" + code + " onchange='changeMatAm();changeWaterL();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");

  $("#newComp").modal("hide");
}

function deleteRow(r)
{
  var i=r.parentNode.parentNode.rowIndex;
  document.getElementById('loadList').deleteRow(i);
  changeMatAm();
  changeWaterL();
}

//Расчёт количества реактивов в загрузочном листе
function changeMatAm(){
  var tbody = document.getElementById("loadList");
  var mats = document.getElementById("materials");
  compl_comp_comps = $("#compl_comp_comps").attr("value");
  var comps = JSON.parse(JSON.parse(compl_comp_comps));
  for (j=2; j < mats.rows.length; j++){
    td = $("#materials tr").eq(j).find("td").eq(5).text("0");
  }
  for (i=2; i<tbody.rows.length; i++){
    var tr = $("#loadList tr").eq(i);
    tr.find("td").eq(4).text(tr.find("input").val());
    var code = tr.find("td").eq(0).text();
    var id = tr.attr("id");
    if (tr.attr("name") == "compl"){
      var newAm = tr.find("input").val();
      if (newAm=="") newAm = 0;
      for (j=0; j < comps.length; j++){
        if (comps[j].fields.compl == id){
          matId = comps[j].fields.mat;
          var amm = $("#materials tr#" + matId).find("td").eq(5).text();
          matAm = (newAm/100)*comps[j].fields.ammount;
          $("#materials tr#" + matId).find("td").eq(5).text((parseFloat(amm) + parseFloat(matAm)).toFixed(2));
        }
      }
    }
    else{
      var amm = $("#materials tr#" + id).find("td").eq(5).text();
      var newAm = tr.find("input").val();
      if (newAm == "") newAm = 0;
      $("#materials tr#" + id).find("td").eq(5).text((parseFloat(amm) + parseFloat(newAm)).toFixed(2));
    }
  }
}

//Проверка соответствия реактивов загрузочного листа реактивам состава
function checkList(){
  var tbody = document.getElementById("loadList");
  var mats = document.getElementById("materials");
  compl_comp_comps = $("#compl_comp_comps").attr("value");
  var comps = JSON.parse(JSON.parse(compl_comp_comps));
  var error = false;
  var composition = {}
  for (i=2; i<mats.rows.length; i++){
    if ($("#materials tr").eq(i).find('td').eq(0).length != 0){
      composition[$("#materials tr").eq(i).find('td').eq(0).text()] = false;
    }
  }
  for (i=2; i<tbody.rows.length; i++){
    var tr = $("#loadList tr").eq(i);
    var code = tr.find("td").eq(0).text();
    var id = tr.attr("id");
    if (tr.attr("name") == "compl"){
      for (j=0; j < comps.length; j++){
        if (comps[j].fields.compl == id){
          matId = comps[j].fields.mat;
          if ($("#materials tr#" + matId).length == 0){
            error = true;
          }
          else {
            composition[$("#materials tr#" + matId).find('td').eq(0).text()] = true;
          }
        }
      }
    }
    else{
      error = error || ($("#materials tr#" + id).length == 0);
      composition[code] = true;
    }
  }
  for (c in composition){
    if (composition[c] == false){
      error = true;
    }
  }
  if (error) $("#error").show();
  else $("#error").hide();
}

//Проверка соответствия границам рецепта
function checkBounds(){
  var mats = document.getElementById("materials");
  var errors = {'length': 0};
  for (i=2; i<mats.rows.length; i++){
    var val = parseFloat($("#materials tr").eq(i).find('td').eq(5).text());
    var min = parseFloat($("#materials tr").eq(i).find('td').eq(2).text());
    var max = parseFloat($("#materials tr").eq(i).find('td').eq(3).text());
    if (val > max || val < min){
      errors[$("#materials tr").eq(i).find('td').eq(0).text()] = $("#materials tr").eq(i).find('td').eq(1).text();
      errors.length ++;
    }
  }
  if (errors.length!=0) {
    delete errors.length;
    message = "Количество реактивов не соответсвует допустимым границам";
    for (e in errors){
      message = message + "; " + e + " " + errors[e];
    }
    $("#errors").text(message);
    $("#errors").show();
  }
  else $("#errors").hide();
}

//Проверка соответствия границам рецепта в планировании
function checkBoundsP(){
  var mats = document.getElementById("materials");
  var errors = {'length': 0};
  for (i=2; i<mats.rows.length; i++){
    var val = parseFloat($("#materials tr").eq(i).find('td').eq(5).text());
    var min = parseFloat($("#materials tr").eq(i).find('td').eq(2).text());
    var max = parseFloat($("#materials tr").eq(i).find('td').eq(3).text());
    if (val > max || val < min){
      errors[$("#materials tr").eq(i).find('td').eq(0).text()] = $("#materials tr").eq(i).find('td').eq(1).text();
      errors.length ++;
    }
  }
  if (errors.length!=0) {
    delete errors.length;
    message = "Количество реактивов не соответсвует допустимым границам";
    for (e in errors){
      message = message + "; " + e + " " + errors[e];
    }
    message = message + " <a href='#' class='alert-link' id='errorLink'>(Всё равно создать процесс)</a>";
    $("#errors").html(message);
    $('#errorLink').on('click', function() {
      $("#form").submit();
    });
    $("#errors").show();
  }
  else $("#errors").hide();
}

//Проверка на ошибки
function submitList(){
  checkList();
  checkBounds();
  if ($("#errors").css('display')=='none' && $("#error").css('display')=='none'){
    $("#form").submit();
  }
}

//Проверка на ошибки
function submitPlan(){
  $("#dateError").hide();
  checkList();
  if ($("#error").css('display')=='none'){
    var temp = document.getElementsByName('start')[0];
    if (document.getElementsByName('start')[0].value == "" || document.getElementsByName('end')[0].value == ""){
      $("#dateError").show();
    }
    else{
      checkBoundsP();
      if ($("#errors").css('display')=='none'){
        $("#form").submit();
      }
    }
  }
}

//Подсчёт воды в загрузочном листе
function changeWaterL() {
  var ammount = document.getElementById("ammount").value;
  var water1 = document.getElementById("water1");
  var water2 = document.getElementById("water2");
  var w_a = document.getElementById("water_amm");
  var tbody = document.getElementById("loadList");
  var mat_ammount = 0;
  for (i=2; i<tbody.rows.length; i++){
    var m = tbody.rows[i].children[2].children[0].valueAsNumber;
    if (isNaN(m)) m = 0;
    mat_ammount = mat_ammount + m;
  }
  water1.textContent = (ammount - mat_ammount).toFixed(2);
  if (w_a != null) w_a.value = (ammount - mat_ammount).toFixed(2);
  if (water2 != null) water2.textContent = (ammount - mat_ammount).toFixed(2);
  /*if ($('#materials2').length == 0) var table = $('#materials').tableToJSON();*/
  var table = $('#loadList').tableToJSON();
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
};

/** Скрипты для страницы загрузочных листов **/
//Формирование таблицы состава в процентах
function getCompositionP(c, m, f_c, f) {
  var table = $("#materials tbody");
  var rowCount = $('#materials tr').length;
  for (i = 2; i < rowCount; i++) $('#materials tr').eq(2).remove();
  var sel = document.getElementById("formula");
  var sel_id = sel.value;
  var components = JSON.parse(c);
  var materials = JSON.parse(m);
  var formulas = JSON.parse(f);
  var f_comp = JSON.parse(f_c);
  for (i = 0; i < f_comp.length; i++){
    if (f_comp[i].fields.formula == sel_id){
      var row = document.createElement("TR");
      var bounds = getMinMax(components, getComp(formulas, f_comp[i].fields.formula), f_comp[i].fields.mat);
      $("<tr id=" + f_comp[i].fields.mat + "><td>" + getCode(f_comp[i].fields.mat, materials) + "</td><td>" + getName(f_comp[i].fields.mat, materials) + "</td><td>" + bounds.min.toFixed(2) + "</td><td>" +
      + bounds.max.toFixed(2) + "</td><td name=" + getCode(f_comp[i].fields.mat, materials) + ">" + (f_comp[i].fields.ammount/1020*100).toFixed(2) + "</td><td></td><tr>").appendTo(table);
    }
  }
};


//Подсчёт воды в загрузочном листе
function changeWaterP() {
  var water1 = document.getElementById("water1");
  var water2 = document.getElementById("water2");
  var w_a = document.getElementById("water_amm");
  var tbody = document.getElementById("loadList");
  var mat_ammount = 0;
  for (i=2; i<tbody.rows.length; i++){
    var m = tbody.rows[i].children[2].children[0].valueAsNumber;
    if (isNaN(m)) m = 0;
    mat_ammount = mat_ammount + m;
  }
  water1.textContent = (100 - mat_ammount).toFixed(2);
  if (w_a != null) w_a.value = (100 - mat_ammount).toFixed(2);
  //if (water2 != null) water2.textContent = (100 - mat_ammount).toFixed(2);
  /*if ($('#materials2').length == 0) var table = $('#materials').tableToJSON();*/
  var table = $('#loadList').tableToJSON();
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
};

function changeWaterTP() {
  var water1 = document.getElementById("water");
  var w_a = document.getElementById("water_amm");
  var tbody = document.getElementById("materials");
  var mat_ammount = 0;
  var mat_ammount2 = 0;
  for (i=2; i<tbody.rows.length; i++){
    var m = tbody.rows[i].children[4];
    if (m==undefined) m2 = 0;
    else  m2 = parseInt(m.textContent);
    mat_ammount = mat_ammount + m2;
    var m1 = tbody.rows[i].children[5];
    if (m1 == undefined) m2 = 0;
    else  m2 = parseInt(m1.textContent);
    if (isNaN(m2)) m2=0;
    mat_ammount2 = mat_ammount2 + m2;
  }
  document.getElementById("water2").textContent = (100 - mat_ammount2).toFixed(2);
  water1.textContent = (100 - mat_ammount).toFixed(2);
  if (w_a != null) w_a.value = (100 - mat_ammount).toFixed(2);
  if ($('#materials2').length == 0) var table = $('#loadList').tableToJSON();
  else var table = $('#materials2').tableToJSON();
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
};

//Добавление реактива в макет
function addMaterialP(){
  var id = document.getElementById("material").selectedOptions[0].value
  var code = document.getElementById("material").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("material").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  $("#loadList tbody").append("<tr id=" + id + "><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td><input type='number' class='form-control' name=" + code + " onchange='changeMatAm();changeWaterP();changeWaterTP();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRowP(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");
  $("#newComp").modal("hide");
}

function addComplCompP(){
  var id = document.getElementById("complComp").selectedOptions[0].value
  var code = document.getElementById("complComp").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("complComp").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  $("#loadList tbody").append("<tr id=" + id + " name='compl'><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td><input type='number' class='form-control' name=" + code + " onchange='changeMatAm();changeWaterP();changeWaterTP();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRowP(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");
  $("#newComp").modal("hide");
}

function deleteRowP(r)
{
  var i=r.parentNode.parentNode.rowIndex;
  document.getElementById('loadList').deleteRow(i);
  changeMatAm();
  changeWaterP();
  changeWaterTP()
}
