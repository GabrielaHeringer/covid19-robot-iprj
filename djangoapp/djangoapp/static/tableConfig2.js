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

function checkedOptions(option){
    for (var i = 0; i < option.length; i++){
        if (option[i].checked ) {
            var option_checked = option[i].value;
        }
    }
    return option_checked;
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
    document.getElementById("mensagem").style.display = 'none';
    limpaBusca();
    if (document.getElementById("linha_TituloResumo").style.display == 'none'){
        document.getElementById("linha_TituloResumo").style.display = 'table-row';
        document.getElementById("linha_autores").style.display = 'table-row';
        document.getElementById("linha_idioma").style.display = 'table-row';
        document.getElementById("tipo_autores").style.display = 'table-row';
        document.getElementById("tipo_TituloResumo").style.display = 'table-row';
        document.getElementById("dataDoAcesso").style.display = 'table-row';
        document.getElementById("dataDaPublicacao").style.display = 'table-row';
    } else {
        document.getElementById("linha_TituloResumo").style.display = 'none';
        document.getElementById("linha_autores").style.display = 'none';
        document.getElementById("linha_idioma").style.display = 'none';
        document.getElementById("tipo_TituloResumo").style.display = 'none';
        document.getElementById("tipo_autores").style.display = 'none';
        document.getElementById("dataDoAcesso").style.display = 'none';
        document.getElementById("dataDaPublicacao").style.display = 'none';
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

    if ((search == "") & (titulo_resumo == "") & (idioma == "") & (autores == "") & (dataDoAcessoMin == "") & (dataDoAcessoMax == "") & (dataDaPublicacaoMin == "") & (dataDaPublicacaoMax == "")){
        document.getElementById("mensagem").style.display = 'none';
    } else{
        document.getElementById("mensagem").style.display = 'block';
    }

    if (search != "") {
        document.getElementById('msg_search_value').innerHTML = 'Busca global: ' + search;
    }
    if (titulo_resumo != "") {
        radio_checked = checkedOptions(radio_titulo_resumo);
        if (option_titulo_resumo == 'titulo') {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + ' em título: ' + titulo_resumo;
        }
        else if (option_titulo_resumo == 'resumo') {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + ' em resumo: ' + titulo_resumo;
        }
        else if (option_titulo_resumo == 'titulo&resumo') {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + 'em título e resumo: ' + titulo_resumo;
        }
        else {
            document.getElementById('msg_titulo_resumo').innerHTML = radio_checked + ' em título ou resumo: ' + titulo_resumo;
        }
    }
    if (idioma != "") {
        document.getElementById('msg_idioma').innerHTML = 'Idioma: ' + idioma;
    }
    if (autores != "") {
        radio_checked = checkedOptions(radio_autores);
        document.getElementById('msg_autores').innerHTML = radio_checked + ' em autores: ' + autores;
    }
    if ((dataDoAcessoMin != "") & (dataDoAcessoMax != "")) {
        document.getElementById('msg_dataDoAcesso').innerHTML = 'Data do Acesso: ' + dataDoAcessoMin + ' a ' + dataDoAcessoMax;
    }
    else if ((dataDoAcessoMin != "") & (dataDoAcessoMax == "")) {
        document.getElementById('msg_dataDoAcesso').innerHTML = 'Data do Acesso: maior ou igual a ' + dataDoAcessoMin;
    }
    else if ((dataDoAcessoMin == "") & (dataDoAcessoMax != "")) {
        document.getElementById('msg_dataDoAcesso').innerHTML = 'Data do Acesso: menor ou igual a ' + dataDoAcessoMax;
    }
    if ((dataDaPublicacaoMin != "") & (dataDaPublicacaoMax != "")) {
        document.getElementById('msg_dataDaPublicacao').innerHTML = 'Data da Publicação: ' + dataDaPublicacaoMin + ' a ' + dataDaPublicacaoMax;
    } 
    else if ((dataDaPublicacaoMin == "") & (dataDaPublicacaoMax != "")) {
        document.getElementById('msg_dataDaPublicacao').innerHTML = 'Data da Publicação: menor ou igual a ' + dataDaPublicacaoMax;
    }
    else if ((dataDaPublicacaoMin != "") & (dataDaPublicacaoMax == "")) {
        document.getElementById('msg_dataDaPublicacao').innerHTML = 'Data da Publicação: maior ou igual a ' + dataDaPublicacaoMin;
    }
    document.getElementById('msg_filtrados').innerHTML = 'Foram filtrados: ' + filtrados + ' de um total de ' + total + ' registros. Você pode refinar o resultado.';
}

$(document).ready(function() {
    var table = $('#example').DataTable({
        "deferRender": true,
	"paging": true,
	"sort": true,
	"paginationType": "simple_numbers",
	"iDisplayLenght": 10,
	"scrollCollapse": false,
	"scrollX": true,
	"scrollY": false,
	"processing": true,
        "language": {
     	    "processing": "Loading. Please Wait..."
  	},
        "serverSide": true,
        "ajax": {
            "url": "/api/novidade/",
            "type": "GET",
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
        "autoWidth": false,
        "columnDefs": [
                { "width": "2%", "targets": 0 },
                { "width": "6%", "targets": 6 },
        ],
	"drawCallback" : function() {
            console.log(this.api().page.info());
        }
    });

    $('#btnSubmit').on('click', function(event){
        $('#example').DataTable().ajax.reload();
	mostrarMensagem();
    });

    $('#btnClear').on('click', function(event){
        limpaBusca();
    });

    $('#btnAvancada').on('click', function(event){
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

