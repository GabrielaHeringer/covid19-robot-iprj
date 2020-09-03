$.fn.parallax = function(resistance, mouse) {
    $el = $(this);
    TweenLite.to($el, 0.2, {
      x: -((mouse.clientX - window.innerWidth / 2) / resistance),
      y: -((mouse.clientY - window.innerHeight / 2) / resistance)
    });
  };
  
  $(document).mousemove(function(e) {
    $(".background").parallax(-30, e);
    $(".covid-big").parallax(30, e);
    $(".covid-banner").parallax(10, e);
    });



function format(d) {
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">' +
        '<tr>' +
        '<td>Resumo:</td>' +
        '<td>' + d.resumo + '</td>' +
        '</tr>' +
        '<tr>' +
        '</table>';
}

function formatar(mascara, documento){
    var i = documento.value.length;
    var saida = mascara.substring(0,1);
    var texto = mascara.substring(i);
    if (texto.substring(0,1) != saida){
        documento.value += texto.substring(0,1);
    }
}

function checkedOptions(option){
    for (var i = 0; i < option.length; i++){
        if (option[i].checked ) {
            var option_checked = option[i].value;
        }
    }
    if (option_checked == 'tt') {
        option_checked = 'Todos os termos';
    } else if (option_checked == 'qt') {
        option_checked = 'Qualquer termo';
    } else {
        option_checked = 'Nenhum termo';
    }
    return option_checked;
}

function stringDeBusca(palavras, option_checked){
    var string = "";
    if (option_checked == 'Nenhum termo'){
        string = 'NOT ';
    }
    string = string + '(';
    for (i in palavras){
        string = string + palavras[i]
        if (i < palavras.length-1) {
            if (option_checked == 'Qualquer termo') {
                string = string + ' OR '
            } else {
                string = string + ' AND '
            }
        }
    }
    string = string + ')'
    return string;
}

function limpaBusca(){
    $('#busca_global').val('');
    $('#titulo_resumo').val('');
    $('#idioma').val('');
    $('#autores').val('');
    $('#resumo').val('');
    $('#data_min').val('');
    $('#data_max').val('');
    $('#data_minA').val('');
    $('#data_maxA').val('');
}

function limpaMensagem(){
    document.getElementById('msg_titulo_resumo').innerHTML = "";
    document.getElementById('msg_search_value').innerHTML = "";
    document.getElementById('msg_idioma').innerHTML = "";
    document.getElementById('msg_autores').innerHTML = "";
    document.getElementById('msg_dataDoAcesso').innerHTML = "";
    document.getElementById('msg_dataDaPublicacao').innerHTML = "";
    document.getElementById('msg_filtrados').innerHTML = "";
}

function mostraBuscaAvançada() {
    if (document.getElementById("linha_TituloResumo").style.display == 'none'){
        document.getElementById("linha_TituloResumo").style.display = 'table-row';
        document.getElementById("linha_autores").style.display = 'table-row';
        document.getElementById("linha_idioma").style.display = 'table-row';
        document.getElementById("dataDoAcesso").style.display = 'table-row';
        document.getElementById("dataDaPublicacao").style.display = 'table-row';
        document.getElementById("buscaAvancada").style.display = 'block';
        document.getElementById("btnBuscaAvancada").style.display = 'none';
        document.getElementById("btnBuscaSimples").style.display = 'table-row';
        document.getElementById("linha_buscaGlobal").style.display = 'none';
    } else {
        document.getElementById("linha_TituloResumo").style.display = 'none';
        document.getElementById("linha_autores").style.display = 'none';
        document.getElementById("linha_idioma").style.display = 'none';
        document.getElementById("dataDoAcesso").style.display = 'none';
        document.getElementById("dataDaPublicacao").style.display = 'none';
        document.getElementById("buscaAvancada").style.display = 'none';
        document.getElementById("btnBuscaAvancada").style.display = 'table-row';
        document.getElementById("btnBuscaSimples").style.display = 'none';
        document.getElementById("linha_buscaGlobal").style.display = 'table-row';
    }  
    
}

function mostrarMensagem() {
    limpaMensagem();
    var search = document.getElementById('busca_global').value;
    var titulo_resumo = document.getElementById('titulo_resumo').value;
    var idioma = document.getElementById('idioma').value;
    var autores = document.getElementById('autores').value;
    var dataDoAcessoMin = document.getElementById('data_minA').value;
    var dataDoAcessoMax = document.getElementById('data_maxA').value;
    var dataDaPublicacaoMin = document.getElementById('data_min').value;
    var dataDaPublicacaoMax = document.getElementById('data_max').value;
    var option_titulo_resumo = document.getElementById('TituloResumo').value;
    var radio_titulo_resumo = document.getElementsByName('tipoTituloResumo');
    var radio_autores = document.getElementsByName('tipoAutores');
    var filtrados = $("#example").dataTable().fnSettings().fnRecordsDisplay();
    var total = $("#example").dataTable().fnSettings().fnRecordsTotal();
    var radio_checked;
    var stringBusca = "";

    if ((search == "") & (titulo_resumo == "") & (idioma == "") & (autores == "") & (dataDoAcessoMin == "") & (dataDoAcessoMax == "") & (dataDaPublicacaoMin == "") & (dataDaPublicacaoMax == "")){
        document.getElementById("mensagem").style.display = 'none';
    } else{
        document.getElementById("mensagem").style.display = 'block';
    }

    if (search != "") {
        document.getElementById('msg_search_value').innerHTML = 'Qualquer campo contendo: ' + search;
	var palavras = search.match(/".*?"|\w+\S+/g);
	stringBusca = '(' + stringDeBusca(palavras, 'Todos os termos') + ' IN (_Título OR _Resumo OR _Autores OR _Idioma OR _Categoria OR _Assunto OR _Data-do-Acesso OR _Data-da-Publicação OR _Portal OR _Fonte))';
    }
    if (titulo_resumo != "") {
        radio_checked = checkedOptions(radio_titulo_resumo);
	var palavras = titulo_resumo.match(/".*?"|\w+\S+/g);
        if (option_titulo_resumo == 'titulo') {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + ' em título: ' + titulo_resumo;
	    var p = ' IN _Título)';
        }
        else if (option_titulo_resumo == 'resumo') {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + ' em resumo: ' + titulo_resumo;
	    var p = ' IN _Resumo)';
        }
        else if (option_titulo_resumo == 'tituloEresumo') {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + ' em título e resumo: ' + titulo_resumo;
	    var p = ' IN (_Título AND _Resumo))';
        }
        else {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + ' em título ou resumo: ' + titulo_resumo;
	    var p = ' IN (_Título OR _Resumo))';
        }
	if (stringBusca == "") {
            stringBusca = '(' + stringDeBusca(palavras, radio_checked) + p;
        } else {
            stringBusca = stringBusca + ' AND (' + stringDeBusca(palavras, radio_checked) + p;
        }
    }
    if (autores != "") {
        var palavras = autores.split(',')
        radio_checked = checkedOptions(radio_autores);
        document.getElementById('msg_autores').innerHTML = radio_checked + ' em autores: ' + autores;
        if (stringBusca == "") {
             stringBusca = '(' + stringDeBusca(palavras, radio_checked) + ' IN _Autores)';
        } else {
             stringBusca = stringBusca + ' AND (' + stringDeBusca(palavras, radio_checked) + ' IN _Autores)';
        }
    }
    if (idioma != "") {
        document.getElementById('msg_idioma').innerHTML = 'Idioma: ' + idioma;
	if (stringBusca == "") {
            stringBusca = '((' + idioma + ') IN _Idioma)';
        } else {
            stringBusca =  stringBusca + ' AND ((' + idioma + ') IN _Idioma)';
        }
    }
    if ((dataDoAcessoMin != "") & (dataDoAcessoMax != "")) {
        document.getElementById('msg_dataDoAcesso').innerHTML = 'Data do Acesso: ' + dataDoAcessoMin + ' a ' + dataDoAcessoMax;
	if (stringBusca == "") {
            if (dataDoAcessoMin != dataDoAcessoMin) {
                 stringBusca = '((BETWEEN ' + dataDoAcessoMin + ' AND ' + dataDoAcessoMax + ') IN _Data-do-Acesso)';
            } else {
                 stringBusca = '((' + dataDoAcessoMin + ') IN _Data-do-Acesso)';
	    }
        } else {
            if (dataDoAcessoMin != dataDoAcessoMin) {
           	 stringBusca =  stringBusca + ' AND ((BETWEEN ' + dataDoAcessoMin + ' AND ' + dataDoAcessoMax + ') IN _Data-do-Acesso)';
            } else {
                 stringBusca = stringBusca + ' AND ((' + dataDoAcessoMin + ') IN _Data-do-Acesso)';
	    }
        }
    }
    else if ((dataDoAcessoMin != "") & (dataDoAcessoMax == "")) {
        document.getElementById('msg_dataDoAcesso').innerHTML = 'Data do Acesso: maior ou igual a ' + dataDoAcessoMin;
	if (stringBusca == "") {
            stringBusca = '(( >= ' + dataDoAcessoMin + ') IN _Data-do-Acesso)';
        } else {
            stringBusca =  stringBusca + ' AND (( >= ' + dataDoAcessoMin + ') IN _Data-do-Acesso)';
        }
    }
    else if ((dataDoAcessoMin == "") & (dataDoAcessoMax != "")) {
        document.getElementById('msg_dataDoAcesso').innerHTML = 'Data do Acesso: menor ou igual a ' + dataDoAcessoMax;
	if (stringBusca == "") {
            stringBusca = '(( <= ' + dataDoAcessoMax + ') IN _Data-do-Acesso)';
        } else {
            stringBusca = stringBusca + ' AND (( <= ' + dataDoAcessoMax + ') IN _Data-do-Acesso)';
        }
    }
    if ((dataDaPublicacaoMin != "") & (dataDaPublicacaoMax != "")) {
        document.getElementById('msg_dataDaPublicacao').innerHTML = 'Data da Publicação: ' + dataDaPublicacaoMin + ' a ' + dataDaPublicacaoMax;
	if (stringBusca == "") {
	    if (dataDaPublicacao != dataDaPublicacao) {
                stringBusca = '((BETWEEN ' + dataDaPublicacaoMin + ' AND ' + dataDaPublicacaoMax + ') IN _Data-da-Publicação)';
            } else {
                stringBusca = '((' + dataDaPublicacaoMin + ') IN _Data-da-Publicação)';
            }
	} else {
	    if (dataDaPublicacao != dataDaPublicacao) {
            	stringBusca = stringBusca + ' AND ((BETWEEN ' + dataDaPublicacaoMin + ' AND ' + dataDaPublicacaoMax + ') IN _Data-da-Publicação)';
            } else {
		stringBusca = stringBusca + ' AND ((' + dataDaPublicacaoMin + ') IN _Data-da-Publicação)';
	    }
	}
    } 
    else if ((dataDaPublicacaoMin == "") & (dataDaPublicacaoMax != "")) {
        document.getElementById('msg_dataDaPublicacao').innerHTML = 'Data da Publicação: menor ou igual a ' + dataDaPublicacaoMax;
	if (stringBusca == "") {
           stringBusca = '(( >= ' + dataDaPublicacaoMin + ') IN _Data-da-Publicação)';
        } else {
           stringBusca =  stringBusca + ' AND (( <= ' + dataDaPublicacaoMax + ') IN _Data-da-Publicação)';
        }
    }
    else if ((dataDaPublicacaoMin != "") & (dataDaPublicacaoMax == "")) {
        document.getElementById('msg_dataDaPublicacao').innerHTML = 'Data da Publicação: maior ou igual a ' + dataDaPublicacaoMin;
	if (stringBusca == "") {
           stringBusca = '(( <= ' + dataDaPublicacaoMax + ') IN _Data-da-publicação)';
        } else {
           stringBusca = stringBusca + ' AND (( >= ' + dataDaPublicacaoMin + ') IN _Data-da-Publicação)';
        }
    }
    document.getElementById('msg_filtrados').innerHTML = '<br><b>String de busca: ' +  stringBusca + '</b><br><br>Foram filtrados: ' + filtrados + ' de um total de ' + total + ' registros.';
}

$(document).ready(function() {
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    var table = $('#example').DataTable({
        "deferRender": true,
	"paging": true,
	"sort": true,
	"responsive": true,
	"paginationType": "simple_numbers",
	"iDisplayLenght": 10,
	"scrollCollapse": false,
	"scrollX": true,
	"scrollY": false,
	"processing": true,
        "language": {
     	    "processing": "Carregando. Por favor, aguarde...",
            "lengthMenu": "Mostrar _MENU_ registros",
            "zeroRecords": "Não foram encontrados artigos para a string de busca.",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            "infoFiltered": "(filtrado do total de _MAX_ registros)",
            "paginate": {
                "previous": "Anterior",
                "next": "Próximo"
            }
  	},
        "serverSide": true,
        "ajax": {
            "url": "/api/novidade/",
            "type": "GET",
	    "cache": true,
	    "headers":{"X-CSRFToken": $crf_token},
            "data": function ( d ) {
                d.search.value = $('#busca_global').val();
                d.columns[1].search.value = $('#titulo_resumo').val();
                d.radio_TituloResumo = $('input[name="tipoTituloResumo"]:checked').val();
                d.opcTituloResumo = $('#TituloResumo').val();
                d.columns[2].search.value = $('#idioma').val();
		d.columns[3].search.value = $('#autores').val();
		d.columns[7].search.value = $('#data_min').val();
                d.extra_value = $('#data_max').val();
		d.columns[6].search.value = $('#data_minA').val();
                d.extra_value2 = $('#data_maxA').val();
                d.radio_autores = $("input[name='tipoAutores']:checked").val();
            }
        },
        "columns": [{
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
            {"data": "titulo"},
            {"data": "idioma"},
            {"data": "autores"},
            {"data": "categoria"},
	    {"data": "subject"},
            {"data": "dataPrimeiroAcesso"},
            {"data": "data_publicacao"},
	    {"data": "portal"},
            /*{
                "data": "fonte",
                "render": function(data, type, row, meta) {
                    return '<a target="_blank" href="'+data+'">Acessar</a>';
		}
            },*/
            {
                "data": "link_externo",
                "render": function (data, type, row, meta) {
                    if(data === ''){
                      	var title_encode = encodeURI(row['titulo']);
                   	return '<a target= "_blank" href="https://www.google.com/#q='+title_encode+'">Pesquisar</a>';
                  }else{
                    	return '<a target="_blank" href="'+data+'">Acessar</a>';
                  }
                }
            },
	    { "data": "resumo", "visible": false},
        ],
        "order": [[6, "desc"]],
        "autoWidth": true,
	"drawCallback" : function() {
            mostrarMensagem();
        }
    });

    $('#btnSubmit').on('click', function(event){
        $('#example').DataTable().ajax.reload();
    });

    $('#btnClear').on('click', function(event){
        limpaBusca();
    });

    $('#btnBuscaAvancada, #btnBuscaSimples').on('click', function(event){
        mostraBuscaAvançada();
    });

    $('#dataDaPublicacao').datepicker({
        todayBtn: 'linked',
        format: 'yyyy/mm/dd',
        autoclose: true,
        todayHighlight: 'linked',
	clearBtn: true
    });

    $('#dataDoAcesso').datepicker({
        todayBtn: 'linked',
        format: 'yyyy/mm/dd',
        autoclose: true,
        todayHighlight: 'linked',
        clearBtn: true
    });

    // Add event listener for opening and closing details
    $('#example tbody').on('click', 'td.details-control', function() {
        var tr = $(this).closest('tr');
        var row = table.row(tr);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        } else {
            // Open this row
            row.child(format(row.data())).show();
            tr.addClass('shown');
        }
    });
    
});

