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
    t6.setAttribute('onclick', 'deleteRow(this)')
    t6.appendChild(document.createTextNode("Удалить"))
    td5.appendChild (t6);
    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);
    row.appendChild(td5);
    tbody.appendChild(row);
    var table = $('#components').tableToJSON({ignoreColumns: [4]}); // Convert the table into a javascript object
    var field = document.getElementById('json');
    field.value = JSON.stringify(table);
  }

  function deleteRow(r)
  {
    var i=r.parentNode.parentNode.rowIndex;
    document.getElementById('components').deleteRow(i);
    var table = $('#components').tableToJSON({ignoreColumns: [4]}); // Convert the table into a javascript object
    var field = document.getElementById('json');
    field.value = JSON.stringify(table);
  }

  
