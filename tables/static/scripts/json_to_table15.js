//для состава
function getComponentsF(c, m, f='') {
  var table = document.getElementById("materials");
  var length = table.rows.length;
  for (i = 2; i < length; i++) table.deleteRow(2);
  var sel = document.getElementById("composition");
  var sel_id = sel.value;
  var components = JSON.parse(c);
  var materials = JSON.parse(m);
  if (f!="0"){
    var f_comp = JSON.parse(f);
  }
  var tbody = document.getElementById("materials").getElementsByTagName("TBODY")[0];
  for (i = 0; i < components.length; i++){
    if (components[i].fields.comp == sel_id){
      var row = document.createElement("TR");
      var td1 = document.createElement("TD");
      var td2 = document.createElement("TD");
      var td3 = document.createElement("TD");
      var td4 = document.createElement("TD");
      var td5 = document.createElement("TD");
      var input = document.createElement("input");
      input.type = "number";
      input.name = getCode(components[i].fields.mat, materials);
      if (f!="0") input.value = ((getAmmount(components[i].fields.mat, f_comp)/1020)*100).toFixed(2);
      input.setAttribute('onchange', "saveTable();return false;");
      input.setAttribute('step', "0.01");
      td1.appendChild(document.createTextNode(getCode(components[i].fields.mat, materials)));
      td2.appendChild(document.createTextNode(getName(components[i].fields.mat, materials)));
      //td3.appendChild(document.createTextNode(components[i].fields.min));
      //td4.appendChild(document.createTextNode(components[i].fields.max));
      td5.appendChild(input);
      row.appendChild(td1);
      row.appendChild(td2);
      //row.appendChild(td3);
      //row.appendChild(td4);
      row.appendChild(td5);
      tbody.appendChild(row);
    }
  }
};

function getCode(m_id, m) {
  var i = 0;
  var id = "0";
  while (i < m.length && id == "0"){
    if (m[i].pk == m_id) id = m[i].fields.code;
    i++;
  }
  return id;
};

//Получение списка составов
function getListOfFormulas(lists) {
  var rowCount = $('#formula option').length;
  for (i = 0; i < rowCount; i++) $('#formula option:last').remove();
  var sel = document.getElementById("composition");
  var sel_id = sel.value;
  var modelLists = JSON.parse(lists);
  for (i = 0; i < modelLists.length; i++){
    if (modelLists[i].fields.composition == sel_id){
      shortName = "";
      if (modelLists[i].fields.name != null){
        shortName = modelLists[i].fields.name;
      }
      $('#formula').append("<option value=" + modelLists[i].pk + ">" + modelLists[i].fields.code + " " + $("#composition :selected").text().substring(5) + ' ' +  shortName + "</option>");
    }
  }
};

function saveTable() {
  var ammount = 100;
  var water = document.getElementById("ВД01");
  var tbody = document.getElementById("materials");
  var mat_ammount = 0;
  for (i=2; i<tbody.rows.length; i++){
    var m = tbody.rows[i].children[2].children[0].valueAsNumber;
    //$("#materials tr").eq(i).find("td").eq(3).text();
    if (isNaN(m)) m = 0;
    mat_ammount = mat_ammount + m;
  }
  water.value = ammount - mat_ammount;
  var table = $('#materials').tableToJSON(); // Convert the table into a javascript object
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

function getAmmount(m_id, f) {
  var i = 0;
  var amm = "0";
  while (i < f.length && amm == "0"){
    if (f[i].fields.mat == m_id) amm = f[i].fields.ammount;
    i++;
  }
  return amm;
};
