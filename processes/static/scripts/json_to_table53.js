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
    var m = tbody.rows[i].children[5].children[0].valueAsNumber;
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
    if (m[i].pk == m_id) {
      if (m[i].fields.mark == "-") mark = "";
      else mark = m[i].fields.mark;
      name = m[i].fields.name + " " + mark;
    }
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


//Заполнение полей данными по выбранной партии
function getKneading(){
  kneadingId = document.getElementById("kneading").value;
  var processes = JSON.parse($("#processes").attr("value"));
  for (p in processes){
    if (p == kneadingId){
      $("#ammount").attr("value", processes[p].amount);
      start = processes[p].start_date.substr(8) + '/' + processes[p].start_date.substr(5,2) + '/' + processes[p].start_date.substr(0, 4);
      end = processes[p].finish_date.substr(8) + '/' + processes[p].finish_date.substr(5,2) + '/' + processes[p].finish_date.substr(0, 4);
      $("#start").attr("value", start);
      $("#end").attr("value", end);
      $("#reactor").find('option').attr("selected", false);
      $("#formula").find('option').attr("selected", false);
      $("#reactor [value = " + processes[p].reactor + "]").attr("selected", "selected");
      $("#formula [value = " + processes[p].formula + "]").attr("selected", "selected");
    }
  }
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
      if (loadList[i].min!='-' && loadList[i].max!=0){
        var min = ((loadList[i].min/100)*amm).toFixed(2);
        var max = ((loadList[i].max/100)*amm).toFixed(2);
      }
      else{
        var min = "-";
        var max = "-";
      }
      if (t_name=='materials'){
        if (loadList[i].type != "5") $('<tr id='+ loadList[i].type + '_' + loadList[i].cont_id + '><td>' + loadList[i].mat_code + '</td><td>' + loadList[i].mat_name + '</td><td>' + "<input type='number' class='min' name=" + loadList[i].mat_code + "_min" + " style='width: 7em'" + " value=" + min + '>' + '</td><td>' + "<input type='number' class='max' name=" + loadList[i].mat_code + "_max"  + " style='width: 7em'" +  " value=" + max + '>' + "</td><td></td><td><input type='number' class='term' name=" + loadList[i].mat_code + "  min=" + min + " max=" + max + " step='0.01' value=" + loadList[i].amount + '>'+ '</td>' + '<td style="visibility:collapse;width:1px">' + loadList[i].type + '_' + loadList[i].cont_id + '_' + loadList[i].amount + '</td></tr>').appendTo(tbody);
        else {
          $('<tr id='+ loadList[i].type + '_' + loadList[i].cont_id + '><td>' + loadList[i].mat_code + '</td><td>' + loadList[i].mat_name + '</td><td>' + "<input type='number' class='min' name=" + loadList[i].mat_code + "_min"  + " style='width: 7em'" +  " value=" + min + '>' + '</td><td>' + "<input type='number' class='max' name=" + loadList[i].mat_code + "_max"  + " style='width: 7em'" +  " value=" + max + '>' + "</td><td>" + getSelectOfComp(loadList[i].cont_id)  + "</td><td><input type='number' class='term' name=" + loadList[i].mat_code + "  min=" + min + " max=" + max + " step='0.01' value=" + loadList[i].amount + '>'+ '</td>' + '<td style="visibility:collapse;width:1px">' + loadList[i].type + '_' + loadList[i].cont_id + '_' + loadList[i].amount + '</td></tr>').appendTo(tbody);
        }
      }
      else{
        $('<tr id='+ loadList[i].type + '_' + loadList[i].cont_id + '><td>' + loadList[i].mat_code + '</td><td>' + loadList[i].mat_name + '</td><td>' + min + '</td><td>' + max + "</td><td>" + loadList[i].amount + '</td>').appendTo(tbody);
      }
  }
};

//Функция для передачи изменений в загрузочном листе в таблицу materials2
function changeMatTable(){
    var rowCount = $('#materials tr').length;
    for (i = 2; i < rowCount; i++) {
      var tr = $('#materials tr').eq(i);
      var valEl = document.getElementsByClassName('term')[i-2];
      var val = valEl.value;
      valEl = document.getElementsByClassName('min')[i-2];
      var min = valEl.value;
      valEl = document.getElementsByClassName('max')[i-2];
      var max = valEl.value;
      if (tr.attr('id')[0] == "5"){
        id = tr.attr('id').substr(2);
        var batch = $("#b"+id + " :selected").val();
        var t = "";
        var bId = "";
        if (batch != undefined) {
          t = batch[0];
          bId = batch.substr(2);
        }
        else{
          t = "5";
          bId = id;
        }
        $('#materials tr').eq(i).find('td').eq(6).text(t + '_' + bId + '_' + val + "_" + min + "_" + max);
      }
      else {
        $('#materials tr').eq(i).find('td').eq(6).text(tr.attr('id') + '_' + val + "_" + min + "_" + max);
      }

    }
    table = $('#materials').tableToJSON();
    var field = document.getElementById('json');
    field.value = JSON.stringify(table);
}

//Функция проверки незаполненных композиций
function checkReady(){
    var rowCount = $('#materials tr').length;
    var res = false;
    for (i = 2; i < rowCount; i++) {
      var tr = $('#materials tr').eq(i);
      if (tr.attr('id')[0] == "5"){
        document.getElementById('startMix').setAttribute('disabled', 'disabled');
      }
    }
    return res;
}

//Функция для проверки, все ли компоненты загружены
function checkLoadedComponents(){
  var rowCount = $('#materials2 tr').length;
  document.getElementById('endMix').removeAttribute('disabled');
  var res = false;
  for (i = 1; i < rowCount; i++) {
    var tr = $('#materials2 tr').eq(i);
    temp = tr.attr('class');
    if (tr.attr('class') != "success"){
      document.getElementById('endMix').setAttribute('disabled', 'disabled');
    }
  }
  return res;
}


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
      if (m_comp[i].fields.formula == null){
        $("<tr id=" + m_comp[i].fields.mat + "><td>" + getCode(m_comp[i].fields.mat, materials) + "</td><td>" + getName(m_comp[i].fields.mat, materials) + "</td><td></td><td><input type='number' class='form-control' value=" + matAm + " name=" + getCode(m_comp[i].fields.mat, materials) + " onchange='changeMatAmP();changeWaterL();changeWaterT();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'>" + matAm + "</td>" + "</tr>").appendTo(table);
      }
      else{
        $("<tr id=" + m_comp[i].fields.formula + " name='compl'><td>" + getCode(m_comp[i].fields.formula, complComp) + "</td><td>" + getFormulaName(m_comp[i].fields.formula) + "</td><td>" + getSelectOfComp(m_comp[i].fields.formula) + "</td><td><input type='number' class='form-control' value=" + matAm + " name=" + getCode(m_comp[i].fields.formula, complComp) + " onchange='changeMatAmP();changeWaterL();changeWaterT();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'>" + matAm + "</td>" + "</tr>").appendTo(table);
      }
      }
    }
    changeMatAmP();
    changeWaterL();
    changeWaterT();
};

function getBatchList(m, m_c, compl) {
  var table = $("#loadList tbody");
  var rowCount = $('#loadList tr').length;
  for (i = 2; i < rowCount; i++) $('#loadList tr').eq(2).remove();
  var sel = document.getElementById("kneading");
  var sel_id = sel.value;
  var processes = JSON.parse($("#processes").attr("value"));
  for (p in processes){
    if (p == sel_id){
      b_amm = processes[p].amount;
      list_id = processes[p].list;
    }
  }
  var materials = JSON.parse(m);
  var m_comp = m_c;
  var complComp = JSON.parse(compl);
  var amm = $("#ammount").val();
  for (i in m_comp){
    if (m_comp[i].list == list_id){
      var row = document.createElement("TR");
      var matAm = (m_comp[i].ammount/b_amm*amm).toFixed(2) ;
      if (m_comp[i].mat != null){
        $("<tr id=" + m_comp[i].mat + "><td>" + getCode(m_comp[i].mat, materials) + "</td><td>" + getName(m_comp[i].mat, materials) + "</td><td></td><td><input type='number' class='form-control' value=" + matAm + " name=" + getCode(m_comp[i].mat, materials) + " onchange='changeMatAmP();changeWaterL();changeWaterT();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'>" + matAm + "</td>" + "</tr>").appendTo(table);
      }
      else{
          $("<tr id=" + m_comp[i].formula + " name='compl'><td>" + getCode(m_comp[i].formula, complComp) + "</td><td>" + getFormulaName(m_comp[i].formula) + "</td><td>" + getSelectOfComp(m_comp[i].formula) + "</td><td><input type='number' class='form-control' value=" + matAm + " name=" + getCode(m_comp[i].formula, complComp) + " onchange='changeMatAmP();changeWaterL();changeWaterT();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'>" + matAm + "</td>" + "</tr>").appendTo(table);
      }
    }
  }
  changeMatAmP();
  changeWaterL();
  changeWaterT();
};

function getFormulaName(id){
  var names = JSON.parse($("#formula_names").attr("value"));
  for (n in names){
    if (n == id){
      return names[n];
    }
  }
}

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
    else  m2 = parseFloat(m.textContent);
    mat_ammount = mat_ammount + m2;
    var m1 = tbody.rows[i].children[5];
    if (m1 == undefined) m2 = 0;
    else  m2 = parseFloat(m1.textContent);
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
  var err = document.getElementById("error-message");
  if (err) err.remove();
  var id = document.getElementById("material").selectedOptions[0].value
  var code = document.getElementById("material").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("material").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  if (!checkExisting(false)){
    $("#loadList tbody").append("<tr id=" + id + "><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td></td><td><input type='number' class='form-control' name=" + code + " onchange='changeMatAmP();changeWaterL();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");
    $("#newComp").modal("hide");
  }
  else {
    var material = document.getElementById('material').parentElement;
    material.insertAdjacentHTML('afterend', '<p class="error-message" id="error-message" style="color: red">' + "Компонент уже есть в листе." + '</p>');
  }
}

//Получение списка технологических композиций
function getSelectOfComp(id){
  var batches = JSON.parse($("#batches").attr("value"));
  res = "<select class='form-control' id='b"+id+"' name='b'"+id+">";
  for (b in batches){
    if (batches[b].formula == id){
      res = res + "<option value="+batches[b].type+"t"+batches[b].id+">"+ batches[b].name + "</option>";
    }
  }
  res = res + "</select>";
  return res;
}

function addComplComp(){
  var err = document.getElementById("error-message");
  if (err) err.remove();
  var id = document.getElementById("complComp").selectedOptions[0].value
  var code = document.getElementById("complComp").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("complComp").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  if (!checkExisting(true)){
    $("#loadList tbody").append("<tr id=" + id + " name='compl'><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td>" + getSelectOfComp(id) + "</td><td><input type='number' class='form-control' name=" + code + " onchange='changeMatAmP();changeWaterL();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRow(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");
    $("#newComplComp").modal("hide");
  }
  else{
    var material = document.getElementById('complComp').parentElement;
    material.insertAdjacentHTML('afterend', '<p class="error-message" id="error-message" style="color: red">' + "Компонент уже есть в листе." + '</p>');
  }
}

function deleteRow(r)
{
  var i=r.parentNode.parentNode.rowIndex;
  document.getElementById('loadList').deleteRow(i);
  changeMatAmP();
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
    var code = tr.find("td").eq(0).text();
    var id = tr.attr("id");
    tr.find("td").eq(4).text(id + '_' + tr.find("input").val());
    if (tr.attr("name") == "compl"){
      var newAm = tr.find("input").val();
      if (newAm=="") newAm = 0;
      for (j=0; j < comps.length; j++){
        if (comps[j].fields.formula == id){
          matId = comps[j].fields.mat;
          var amm = $("#materials tr#" + matId).find("td").eq(5).text();
          matAm = (newAm/100)*(comps[j].fields.ammount/1020)*100;
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

//Расчёт количества реактивов в загрузочном листе
function changeMatAmP(){
  var tbody = document.getElementById("loadList");
  var mats = document.getElementById("materials");
  compl_comp_comps = $("#compl_comp_comps").attr("value");
  var batches = JSON.parse($("#batches").attr("value"));
  var comps = JSON.parse(JSON.parse(compl_comp_comps));
  var batch_comps = JSON.parse(JSON.parse($("#batch_comps").attr("value")));
  for (j=2; j < mats.rows.length; j++){
    td = $("#materials tr").eq(j).find("td").eq(5).text("0");
  }
  for (i=2; i<tbody.rows.length; i++){
    var tr = $("#loadList tr").eq(i);
    tr.find("td").eq(5).text(tr.find("input").val());
    var code = tr.find("td").eq(0).text();
    var id = tr.attr("id");
    if (tr.attr("name") == "compl"){
      var batch = $("#b"+id + " :selected").val();
      var t = "";
      var bId = "";
      if (batch != undefined) {
        t = batch[0];
        bId = batch.substr(2);
      }
      else{
        t = "4";
        bId = tr.attr("id");
      }
      var newAm = tr.find("input").val();
      if (newAm=="") newAm = 0;
      if (t!="3" && t!= "4"){
        batchId = 0;
        for (b in batches){
          if (batches[b].id == bId && t == batches[b].type) batchId = batches[b].batch;
        }
        for (j=0; j < batch_comps.length; j++){
          if (batch_comps[j].fields.batch == batchId){
            matId = batch_comps[j].fields.mat;
            var amm = $("#materials tr#" + matId).find("td").eq(5).text();
            matAm = (newAm/100)*batch_comps[j].fields.ammount;
            $("#materials tr#" + matId).find("td").eq(5).text((parseFloat(amm) + parseFloat(matAm)).toFixed(2));
          }
        }
      }
      else{
        if (t == "3"){
          comps = JSON.parse(JSON.parse(compl_comp_comps));
          for (j=0; j < comps.length; j++){
            if (comps[j].fields.compl == bId){
              matId = comps[j].fields.mat;
              var amm = $("#materials tr#" + matId).find("td").eq(5).text();
              matAm = (newAm/100)*comps[j].fields.ammount;
              $("#materials tr#" + matId).find("td").eq(5).text((parseFloat(amm) + parseFloat(matAm)).toFixed(2));
            }
          }
        }
        else {
          comps = JSON.parse(JSON.parse($("#f_c").attr("value")));
          for (j=0; j < comps.length; j++){
            if (comps[j].fields.formula == bId){
              matId = comps[j].fields.mat;
              var amm = $("#materials tr#" + matId).find("td").eq(5).text();
              matAm = (newAm/1020)*comps[j].fields.ammount;
              $("#materials tr#" + matId).find("td").eq(5).text((parseFloat(amm) + parseFloat(matAm)).toFixed(2));
            }
          }
        }
      }
      //Формат ячейики сложного компонента: тип(1(реактор),2(танк),3(приобретённая),4(не выбрана))_ключ композиции_количество
      tr.find("td").eq(5).text(t+"_"+bId+"_"+tr.find("input").val());
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
  $("#error").hide();
  var tbody = document.getElementById("loadList");
  var mats = document.getElementById("materials");
  compl_comp_comps = $("#f_c").attr("value");
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
        if (comps[j].fields.formula == id){
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
  $("#errors").hide();
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
    message = message + " <a href='#' class='alert-link' id='errorLink'>(Всё равно создать загрузочный лист)</a>";
    $("#errors").html(message);
    $('#errorLink').on('click', function() {
      $("#form").submit();
    });
    $("#errors").show();
  }
  else $("#errors").hide();
}

//Проверка на вмещаемость реактора
function checkRector(){
  $("#reactorError").hide();
  rId = $("#reactor :selected").val();
  var am = $("#ammount").val();
  var reactors = JSON.parse(JSON.parse($("#reactors").attr("value")));
  for (i=0; i < reactors.length; i++){
    if (reactors[i].pk == rId){
      if (am > reactors[i].fields.max || am < reactors[i].fields.min) $("#reactorError").show();
    }
  }
}

//Проверка соответствия границам рецепта в планировании
function checkBoundsP(){
  var mats = document.getElementById("materials");
  $("#errors").hide();
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
      $("#errors").hide();
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

//Проверка на ошибки в плане
function submitPlan(){
  $("#dateError").hide();
  checkList();
  if ($("#error").css('display')=='none'){
    var temp = document.getElementsByName('start')[0];
    if (document.getElementsByName('start')[0].value == "" || document.getElementsByName('end')[0].value == ""){
      $("#dateError").show();
    }
    else{
      checkRector();
      if ($("#reactorError").css('display')=='none'){
        checkMatAm();
        if ($("#amountError").css('display')=='none'){
          checkBoundsP();
          if ($("#errors").css('display')=='none'){
            $("#form").submit();
          }
        }
      }
    }
  }
}

//Проверка на ошибки в формировании технологической композиции
function submitTechComp(){
  $("#dateError").hide();
  checkList();
  if ($("#error").css('display')=='none'){
      checkRector();
      if ($("#reactorError").css('display')=='none'){
        checkBoundsP();
        if ($("#errors").css('display')=='none'){
          checkMatAm();
          if ($("#amountError").css('display')=='none'){
              checkIsEmpty($("#reactor").val());
          }
        }
      }
  }
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

//Проверка на содержимое реактора
function checkIsEmpty(id){
  $("#reactorIsNotEmpty").hide();
  var csrftoken = getCookie('csrftoken');
  $.ajax({
        type: "POST",
        url: 'check_is_empty/',
        data: {
          'id': id
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data)
        {
          if (data!="empty") {
            $("#reactorIsNotEmpty").show();
            $("#startMix").prop('disabled', true);
          }
          else {
            $("#startMix").prop('disabled', false);
            $("#form").submit();
          }
        }
      });
}

//проверка наличия формулы в компонентах загрузочного листа
function checkFormula(id){
  var loadList = $("#load_list").attr("value");
  loadList = JSON.parse(loadList);
  var res = false;
  for (c in loadList){
    if (loadList[c].cont_id == id && loadList[c].type == 5){
      return true;
    }
  }
  return false;
}

function checkIsEmpty2(id){
  $("#reactorIsNotEmpty").hide();
  var csrftoken = getCookie('csrftoken');
  $.ajax({
        type: "POST",
        url: 'check_is_empty2/',
        data: {
          'id': id
        },
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function onAjaxSuccess(data)
        {
          if (data!="empty") {
            if (checkFormula(data)) {
              $("#reactorIsNotEmpty").text("Реактор не пуст. Необходимо пересчитать загрузочный лист.");
              $("#reactorIsNotEmpty").show();
              $("#startMix").prop('disabled', true);
            }
            else {
              $("#reactorIsNotEmpty").text("Реактор занят");
              $("#reactorIsNotEmpty").show();
              $("#startMix").prop('disabled', true);
            }
          }
          else {
            $("#startMix").prop('disabled', false);
            checkReady();
          }
        }
      });
}

//Проверка наличия реактивов
function checkMatAm(){
  $("#amountError").hide();
  var length = $("#loadList").find('tr').length;
  compl_comp = JSON.parse(JSON.parse($("#compl_comp").attr("value")));
  materials = JSON.parse(JSON.parse($("#reagents").attr("value")));
  batches = JSON.parse($("#batches").attr("value"));
  var errors = {'length': 0};
  for (i=2; i < length; i++){
    var tr = $("#loadList tr").eq(i);
    var code = tr.find("td").eq(0).text();
    var id = tr.attr("id");
    if (tr.attr("name") == "compl"){
      var batch = $("#b"+id + " :selected").val();
      var t = "";
      var bId = "";
      if (batch != undefined) {
        t = batch[0];
        bId = batch.substr(2);
      }
      var am = tr.find("input").val();
      if (am=="") am = 0;
      for (j in batches){
        if (batches[j].id == bId && t == batches[j].type){
          curAm = parseFloat(batches[j].amount);
          if (am > curAm){
            errors[batches[j].name] = curAm;
            errors['length'] = errors['length'] +1;
          }
        }
      }
    }
    else{
      var am = tr.find("input").val();
      if (am == "") am = 0;
      for (j=0; j < materials.length; j++){
        if (materials[j].pk == id){
          curAm = parseFloat(materials[j].fields.ammount);
          if (am > curAm){
            errors[materials[j].fields.code] = curAm;
            errors['length'] = errors['length'] +1;
          }
        }
      }
    }
  }

  if (errors.length!=0) {
    delete errors.length;
    message = "Недостаточно реактивов";
    for (e in errors){
      message = message + "; " + e + "- доступное количество: " + errors[e];
    }
    $("#amountError").html(message);
    $("#amountError").show();
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
    var m = tbody.rows[i].children[3].children[0].valueAsNumber;
    if (isNaN(m)) m = 0;
    mat_ammount = mat_ammount + m;
  }
  water1.textContent = (ammount - mat_ammount).toFixed(2);
  if (w_a != null) w_a.value = (ammount - mat_ammount).toFixed(2);
  if (water2 != null) water2.textContent = (ammount - mat_ammount).toFixed(2);
  /*if ($('#materials2').length == 0) var table = $('#materials').tableToJSON();*/
  isWaterValid("water1", "send");
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
  isWaterValid("water1", "send");
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
    else  m2 = parseFloat(m.textContent);
    mat_ammount = mat_ammount + m2;
    var m1 = tbody.rows[i].children[5];
    if (m1 == undefined) m2 = 0;
    else  m2 = parseFloat(m1.textContent);
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

function checkExisting(isCompl){
  res = false;
  var size = $("#loadList tr").length;
  for (var i = 1; i < size; i++){
    var row = $("#loadList tr").eq(i);
    if (!isCompl) id = $("#material").prop("value");
    else id = $("#complComp").prop("value");
    temp = row.attr('name');
    temp2 =  row.attr('name') == "compl" ^ isCompl;
    if (row.prop("id") == id && !(row.attr('name') == "compl" ^ isCompl)) res = true;
  }
  return res;
}

//Добавление реактива в макет
function addMaterialP(){
  var err = document.getElementById("error-message");
  if (err) err.remove();
  var id = document.getElementById("material").selectedOptions[0].value
  var code = document.getElementById("material").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("material").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  if (!checkExisting(false)){
    $("#loadList tbody").append("<tr id=" + id + "><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td><input type='number' class='form-control' name=" + code + " onchange='changeMatAm();changeWaterP();changeWaterTP();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRowP(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");
    $("#newComp").modal("hide");
  }
  else{
    var material = document.getElementById('material').parentElement;
    material.insertAdjacentHTML('afterend', '<p class="error-message" id="error-message" style="color: red">' + "Компонент уже есть в листе." + '</p>');
  }
}

function addComplCompP(){
  var err = document.getElementById("error-message");
  if (err) err.remove();
  var id = document.getElementById("complComp").selectedOptions[0].value
  var code = document.getElementById("complComp").selectedOptions[0].textContent.substring(0,4);
  var name = document.getElementById("complComp").selectedOptions[0].textContent.substring(5);
  /*var amm = $("#percent").val();
  var waterAmm = $("#ВД01").val() - amm;
  $("#ВД01").attr("value", waterAmm);*/
  if (!checkExisting(true)){
    $("#loadList tbody").append("<tr id=" + id + " name='compl'><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td><input type='number' class='form-control' name=" + code + " onchange='changeMatAm();changeWaterP();changeWaterTP();return false;'></td>" + "<td><button class='btn btn-default' onclick='deleteRowP(this)'><i class='glyphicon glyphicon-trash'></i></button></td><td style='visibility:collapse;'></td>" + "</tr>");
    $("#newComplComp").modal("hide");
  }
  else{
    var material = document.getElementById('complComp').parentElement;
    material.insertAdjacentHTML('afterend', '<p class="error-message" id="error-message" style="color: red">' + "Компонент уже есть в листе." + '</p>');
  }
}

function deleteRowP(r)
{
  var i=r.parentNode.parentNode.rowIndex;
  document.getElementById('loadList').deleteRow(i);
  changeMatAm();
  changeWaterP();
  changeWaterTP();
}

//Функция проверки воды
function isWaterValid(water, btn){
  if ($("#"+water).text() < 0){
    $("#"+water).attr("bgcolor", "#ffa6a6");
    $("#"+btn).attr("disabled", true);
    return false;
  }
  else{
    $("#"+water).attr("bgcolor", "#ffffff");
    $("#"+btn).attr("disabled", false);
    return true;
  }
}
