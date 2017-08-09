function addRow(id){
    var comp_id = document.getElementById("material").selectedOptions[0].value;
    var comp_name = document.getElementById("material").selectedOptions[0].textContent;
    var min = document.getElementById("min").value;
    var max = document.getElementById("max").value;
    var tbody = document.getElementById(id).getElementsByTagName("TBODY")[0];
    var row = document.createElement("TR");
    var td1 = document.createElement("TD");
    td1.appendChild(document.createTextNode(comp_id));
    var td2 = document.createElement("TD");
    td2.appendChild (document.createTextNode(comp_name.substring(5)));
    var td3 = document.createElement("TD");
    td3.appendChild (document.createTextNode(min));
    var td4 = document.createElement("TD");
    td4.appendChild (document.createTextNode(max));
    var td5 = document.createElement("TD");
    var t6 = document.createElement("button");
    t6.setAttribute('onclick', 'deleteRow(this)');
    t6.setAttribute('class', "btn btn-default");
    var d = document.createElement("i");
    d.setAttribute('class', "glyphicon glyphicon-trash");
    t6.appendChild(d);
    td5.appendChild (t6);
    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);
    row.appendChild(td5);
    tbody.appendChild(row);
    saveTable2();
  }



  function deleteRow(r)
  {
    var i=r.parentNode.parentNode.rowIndex;
    document.getElementById('components').deleteRow(i);
    saveTable2();
  }

  function deleteRow2(r, amm)
  {
    var i=r.parentNode.parentNode.rowIndex;
    document.getElementById('materials').deleteRow(i);
    var waterAmm = parseInt($("#ВД01").val()) + parseInt(amm);
    $("#ВД01").attr("value", waterAmm);
    saveTable3();
  }

function saveTable2(){
  var table = $('#components').tableToJSON({ignoreColumns: [4]}); // Convert the table into a javascript object
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
}

function saveTable3(){
  var table = $('#materials').tableToJSON({ignoreColumns: [4]}); // Convert the table into a javascript object
  var field = document.getElementById('json');
  field.value = JSON.stringify(table);
}

function checkBounds(){
  var min = document.getElementById("min");
  var max = document.getElementById("max");
  return min.valueAsNumber <= max.valueAsNumber;
}

function saveRow(){
  var err = document.getElementById("error-message");
  if (err) err.remove();
  if (checkBounds()) {
    addRow('components');
    $("#newComp").modal("hide");
  }
  else{
    var max = document.getElementById('max').parentElement;
    max.insertAdjacentHTML('afterend', '<p class="error-message" id="error-message" style="color: red">' + "Минимальное значение должно быть не больше максимального." + '</p>');
  }
}

  function addMat(){
    var code = document.getElementById("material").selectedOptions[0].value;
    var name = document.getElementById("material").selectedOptions[0].textContent.substring(5);
    var amm = $("#percent").val();
    var waterAmm = $("#ВД01").val() - amm;
    $("#ВД01").attr("value", waterAmm);
    $("#materials tbody").append("<tr><td>" + code + "</td>" + "<td>" + name + "</td>" + "<td>" + amm + "</td>" + "<td><button class='btn btn-default' onclick='deleteRow2(this," + amm + ")'><i class='glyphicon glyphicon-trash'></i></button></td>" + "</tr>");
    $("#newComp").modal("hide");
    saveTable3();
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

  function getName(m_id, m) {
    var i = 0;
    var name = "0";
    while (i < m.length && name == "0"){
      if (m[i].pk == m_id) name = m[i].fields.name;
      i++;
    }
    return name;
  };

  function changeWater() {
    var ammount = document.getElementById("ammount").value;
    var water1 = document.getElementById("water");
    var water2 = document.getElementById("water2");
    var w_a = document.getElementById("water_amm");
    var tbody = document.getElementById("materials");
    var mat_ammount = 0;
    for (i=2; i<tbody.rows.length; i++){
      var m = tbody.rows[i].children[2].children[0].valueAsNumber;
      var temp = $("#materials tr").eq(i).find("td").eq(3);
      temp.css("visibility", "collapse");
      temp.text(m);
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

  function getComponents(c, m) {
    var table = document.getElementById("materials");
    var length = table.rows.length;
    for (i = 2; i < length; i++) table.deleteRow(2);
    var sel = document.getElementById("composition");
    var sel_id = sel.value;
    var components = JSON.parse(c);
    var materials = JSON.parse(m);
    var amm = $("#ammount").val();
    var tbody = document.getElementById("materials").getElementsByTagName("TBODY")[0];
    for (i = 0; i < components.length; i++){
      if (components[i].fields.formula == sel_id){
        var row = document.createElement("TR");
        row.setAttribute('id', components[i].fields.mat);
        var td1 = document.createElement("TD");
        var td2 = document.createElement("TD");
        var td5 = document.createElement("TD");
        var td6 = document.createElement("TD");
        var input = document.createElement("input");
        input.type = "number";
        input.name = getCode(components[i].fields.mat, materials);
        input.setAttribute('onchange', "changeWater();return false;");
        input.setAttribute('step', "0.01");
        input.setAttribute('value', ((components[i].fields.ammount/1020)*amm).toFixed(2));
        td1.appendChild(document.createTextNode(getCode(components[i].fields.mat, materials)));
        td2.appendChild(document.createTextNode(getName(components[i].fields.mat, materials)));
        td5.appendChild(input);
        row.appendChild(td1);
        row.appendChild(td2);
        row.appendChild(td5);
        row.appendChild(td6);
        tbody.appendChild(row);
      }
    }
    var code = document.getElementById("composition").selectedOptions[0].textContent.substring(0, 5);
    var name = document.getElementById("composition").selectedOptions[0].textContent.substring(5);
    $("#code").attr("value", code);
    $("#name1").attr("value", name);
  };

//функция получения состава технологической композиции
  function getComponents2(c, m) {
    var table = document.getElementById("materials");
    var length = table.rows.length;
    for (i = 2; i < length; i++) table.deleteRow(2);
    var sel = document.getElementById("formula");
    var sel_id = sel.value;
    var components = JSON.parse(c);
    var materials = JSON.parse(m);
    var amm = $("#ammount").val();
    var tbody = document.getElementById("materials").getElementsByTagName("TBODY")[0];
    for (i = 0; i < components.length; i++){
      if (components[i].fields.formula == sel_id){
        var row = document.createElement("TR");
        row.setAttribute('id', components[i].fields.mat);
        var td1 = document.createElement("TD");
        var td2 = document.createElement("TD");
        var td5 = document.createElement("TD");
        var td6 = document.createElement("TD");
        var input = document.createElement("input");
        input.type = "number";
        input.name = getCode(components[i].fields.mat, materials);
        input.setAttribute('onchange', "changeWater();return false;");
        input.setAttribute('step', "0.01");
        input.setAttribute('value', ((components[i].fields.ammount/1020)*amm).toFixed(2));
        td1.appendChild(document.createTextNode(getCode(components[i].fields.mat, materials)));
        td2.appendChild(document.createTextNode(getName(components[i].fields.mat, materials)));
        td5.appendChild(input);
        row.appendChild(td1);
        row.appendChild(td2);
        row.appendChild(td5);
        row.appendChild(td6);
        tbody.appendChild(row);
      }
    }
    var code = document.getElementById("composition").selectedOptions[0].textContent.substring(0, 5);
    var name = document.getElementById("composition").selectedOptions[0].textContent.substring(5);
    $("#code").attr("value", code);
    $("#name1").attr("value", name);
  };
