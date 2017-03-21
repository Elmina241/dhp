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
  var tbody = document.getElementById("materials");
  var mat_ammount = 0;
  for (i=2; i<tbody.rows.length; i++){
    var m = tbody.rows[i].children[4].children[0].valueAsNumber;
    if (isNaN(m)) m = 0;
    mat_ammount = mat_ammount + m;
  }
  water1.textContent = (ammount - mat_ammount).toFixed(2);
  if (water2 != null) water2.textContent = (ammount - mat_ammount).toFixed(2);
  var table = $('#materials2').tableToJSON(); // Convert the table into a javascript object
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
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

function getMinMax(c, comp, mat){
  var i=0;
  var bounds = {
    min: 0,
    max: 0
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
  return bounds;
}

function changeMinMax(c, f){
  var components = JSON.parse(c);
  var form = JSON.parse(f);
  var amm = $("#ammount").val();
  var comp = getComp(form, $("#formula").val());
  var size = $("#materials tr").size();
  for (var i = 2; i < size; i++){
    var row = $("#materials tr").eq(i);
    var code = row.attr("id");
    var bounds = getMinMax(components, comp, code);
    $("#materials tr").eq(i).find('td').eq(2).text(((bounds.min/100)*amm).toFixed(2));
    $("#materials tr").eq(i).find('td').eq(3).text(((bounds.max/100)*amm).toFixed(2));
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
        $('<tr id='+ l_comp[i].fields.mat + '><td>' + mat_code + '</td><td>' + mat_name + '</td><td>' + min + '</td><td>' + max + "</td><td><input type='number' name=" + mat_code + " onchange='changeWater();return false;' step='0.01' value=" + mat_amm + '>').appendTo(tbody);
      }
      else{
        $('<tr id='+ l_comp[i].fields.mat + '><td>' + mat_code + '</td><td>' + mat_name + '</td><td>' + min + '</td><td>' + max + "</td><td>" + mat_amm + '</td>').appendTo(tbody);
      }
  }
};

//Функция для передачи изменений в таблицу
function saveChanges(){
  $("#textAmm").text($("#ammount").val());
  var table = $("#materials");
  var size = $("#materials tr").size();
  for (var i = 2; i < size; i++){
    $("#materials2 tr").eq(i).find('td').eq(4).text($("#materials tr").eq(i).find('input').val());
  }
  var table = $('#materials2').tableToJSON(); // Convert the table into a javascript object
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
  var form = document.getElementById("form");
  form.submit();
}
