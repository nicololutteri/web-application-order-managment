SITE = "https://webappapi.nicololutteri.com"

$.ajax({
    url: SITE + "/orders/all/",
    type: 'GET',
    headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'token': Cookies.get('token') }
}).done(function (data) {
    $("#btn-sort-ord_num").click(function () {
        data.sort(function (a, b) {
            return parseInt(a['pk']) < parseInt(b['pk']) ? -1 : 1;
        });

        reload();
    });
    $("#btn-sort-ord_numI").click(function () {
        data.sort(function (a, b) {
            return parseInt(a['pk']) < parseInt(b['pk']) ? 1 : -1;
        });

        reload();
    });

    $("#btn-sort-ord_amount").click(function () {
        data.sort(function (a, b) {
            return parseInt(a["fields"]["ord_amount"]) < parseInt(b["fields"]["ord_amount"]) ? -1 : 1;
        });

        reload();
    });
    $("#btn-sort-ord_amountI").click(function () {
        data.sort(function (a, b) {
            return parseInt(a["fields"]["ord_amount"]) < parseInt(b["fields"]["ord_amount"]) ? 1 : -1;
        });

        reload();
    });

    $("#btn-sort-advance_amount").click(function () {
        data.sort(function (a, b) {
            return parseInt(a["fields"]["advance_amount"]) < parseInt(b["fields"]["advance_amount"]) ? -1 : 1;
        });

        reload();
    });
    $("#btn-sort-advance_amountI").click(function () {
        data.sort(function (a, b) {
            return parseInt(a["fields"]["advance_amount"]) < parseInt(b["fields"]["advance_amount"]) ? 1 : -1;
        });

        reload();
    });

    $("#btn-sort-ord_date").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["ord_date"] < b["fields"]["ord_date"] ? -1 : 1;
        });

        reload();
    });
    $("#btn-sort-ord_dateI").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["ord_date"] < b["fields"]["ord_date"] ? 1 : -1;
        });

        reload();
    });

    $("#btn-sort-cust_code").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["cust_code"] < b["fields"]["cust_code"] ? -1 : 1;
        });

        reload();
    });
    $("#btn-sort-cust_codeI").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["cust_code"] < b["fields"]["cust_code"] ? 1 : -1;
        });

        reload();
    });

    $("#btn-sort-agent_code").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["agent_code"] < b["fields"]["agent_code"] ? -1 : 1;
        });

        reload();
    });
    $("#btn-sort-agent_codeI").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["agent_code"] < b["fields"]["agent_code"] ? 1 : -1;
        });

        reload();
    });

    $("#btn-sort-ord_description").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["ord_description"] < b["fields"]["ord_description"] ? -1 : 1;
        });

        reload();
    });
    $("#btn-sort-ord_descriptionI").click(function () {
        data.sort(function (a, b) {
            return a["fields"]["ord_description"] < b["fields"]["ord_description"] ? 1 : -1;
        });

        reload();
    });

    function reload() {
        $('#ordersTable tbody').empty();
        reloadTable();
    }

    function reloadTable() {
        for (i = 0; i < data.length; i++) {
            addEntry(data[i]["pk"], data[i]["fields"]["ord_amount"], data[i]["fields"]["advance_amount"], data[i]["fields"]["ord_date"] + '</td>', data[i]["fields"]["cust_code"], data[i]["fields"]["agent_code"], data[i]["fields"]["ord_description"]);
        }
    }

    data = JSON.parse(data);
    reloadTable();
});

$('#btn-add').click(function () {
    var tmp = '<p id="dataInfoShow">In this demo version is not permitted</p>';

    $('#dataInfo').empty();
    $('#dataInfo').append(tmp);

    $('#modalInfo').modal('show');
})

function addEntry(pk, ord_amount, advance_amount, ord_date, cust_code, agent_code, ord_descriptor) {
    var tmp = ''
    tmp += '<tr id="' + pk + '">';

    tmp += '<td scope="row" aria-describedby="table_ord_num">' + pk + '</td>';
    tmp += '<td aria-describedby="table_ord_amount">' + ord_amount + '</td>';
    tmp += '<td aria-describedby="table_advance_amount">' + advance_amount + '</td>';
    tmp += '<td aria-describedby="table_ord_date">' + ord_date + '</td>';
    tmp += '<td aria-describedby="table_cust_code">' + cust_code + '</td>';
    tmp += '<td aria-describedby="table_agent_code">' + agent_code + '</td>';
    tmp += '<td aria-describedby="table_ord_description">' + ord_descriptor + '</td>';

    if (ROLE === "Role.Manager" || ROLE === "Role.Agent") {
        tmp += '<td aria-labelledby="table_mod"><button id="mod" ' + 'onclick=' + 'modify("' + pk + '") class="btn">&#10000;</button></td>';
        tmp += '<td aria-labelledby="table_del"><button id="del" ' + 'onclick=' + 'deleteOrder("' + pk + '") class="btn">&#9851;</button></td>';
    }
    else {
        tmp += '<td aria-labelledby="table_mod"></td>';
        tmp += '<td aria-labelledby="table_del"></td>';
    }

    if (ROLE === "Role.Manager" || ROLE === "Role.Agent") {
        tmp += '<td aria-labelledby="table_info-customer"><button id="info" ' + 'onclick=' + 'infoCustomer("' + cust_code + '") class="btn">?</button></td>';
    }
    else {
        tmp += '<td aria-labelledby="table_info-customer"></td>';
    }

    if (ROLE === "Role.Manager" || ROLE === "Role.Customer") {
        tmp += '<td aria-labelledby="table_info-agent"><button id="info" ' + 'onclick=' + 'infoAgent("' + agent_code + '") class="btn">?</button></td>';
    }
    else {
        tmp += '<td aria-labelledby="table_info-agent"></td>';
    }

    tmp += '</tr>';

    $('#ordersTable tbody').append(tmp);
}

function modify(code) {
    var tmp = '<p id="dataInfoShow">In this demo version is not permitted</p>';

    $('#dataInfo').empty();
    $('#dataInfo').append(tmp);

    $('#modalInfo').modal('show');
}

if (ROLE === "Role.Customer") {
    $('#newTable').empty();
}

function deleteOrder(code) {
    var tmp = '<p id="dataInfoShow">In this demo version is not permitted</p>';

    $('#dataInfo').empty();
    $('#dataInfo').append(tmp);

    $('#modalInfo').modal('show');
};

function infoCustomer(code) {
    $.ajax({
        url: SITE + "/clients/" + code + "/",
        type: 'GET',
        headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'token': Cookies.get('token') }
    }).done(function (data) {
        data = JSON.parse(data);

        var tmp = '<p id="dataInfoShow">';

        tmp += 'Codice cliente: ' + data[0]['pk'] + '</br>'
        tmp += 'Nome cliente: ' + data[0]['fields']['cust_name'] + '<br />'
        tmp += 'Citta: ' + data[0]['fields']['cust_city'] + '<br />'
        tmp += 'Luogo di lavoro: ' + data[0]['fields']['working_area'] + '<br />'
        tmp += 'Stato: ' + data[0]['fields']['cust_country'] + '<br />'
        tmp += 'Grado: ' + data[0]['fields']['grade'] + '<br />'
        tmp += 'Prezzo di apertura: ' + data[0]['fields']['opening_amt'] + '<br />'
        tmp += 'Prezzo ricevuto: ' + data[0]['fields']['receive_amt'] + '<br />'
        tmp += 'Pagamento: ' + data[0]['fields']['payment_amt'] + '<br />'
        tmp += 'Debito: ' + data[0]['fields']['outstanding_amt'] + '<br />'
        tmp += 'Numero di telefono: ' + data[0]['fields']['phone_no'] + '<br />'
        tmp += 'Codice agente: ' + data[0]['fields']['agent_code']

        tmp += '</p>'

        $('#dataInfo').empty();
        $('#dataInfo').append(tmp);

        $('#modalInfo').modal('show');
    }).fail(function (data) {
        alert('Operazione fallita');
    });
};

function infoAgent(code) {
    $.ajax({
        url: SITE + "/agents/" + code + "/",
        type: 'GET',
        headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'token': Cookies.get('token') }
    }).done(function (data) {
        data = JSON.parse(data);

        var tmp = '<p id="dataInfoShow">';

        tmp += 'Codice agente:' + data[0]['pk'] + '<br />'
        tmp += 'Nome agente:' + data[0]['fields']['agent_name'] + '<br />'
        tmp += 'Area di lavoro:' + data[0]['fields']['working_area'] + '<br />'
        tmp += 'Commissioni: ' + data[0]['fields']['commission'] + '<br />'
        tmp += 'Numero di telefono: ' + data[0]['fields']['phone_no'] + '<br />'
        tmp += 'Stato: ' + data[0]['fields']['country']

        tmp += '</p>'

        $('#dataInfo').empty();
        $('#dataInfo').append(tmp);

        $('#modalInfo').modal('show');
    }).fail(function (data) {
        alert('Operazione fallita');
    });
};
