from django.db import models
from django.db.models import Q
from model_utils import Choices
from app.filters import FiltroTituloResumo, FiltroAutores, FiltroDatas, FiltroBuscaGlobal
import ipdb


ORDER_COLUMN_CHOICES = Choices(
	('0', 'resumo'),
	('1', 'titulo'),
	('2', 'idioma'),
	('3', 'autores'),
	('4', 'categoria'),
	('5', 'subject'),
	('6', 'dataPrimeiroAcesso'),
	('7', 'data_publicacao'),
	('8', 'portal'),
	('9', 'fonte'),
	('10', 'link_externo'),
)

class PortalBusca(models.Model):
    nome = models.TextField()
    dataInclusao = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    link = models.URLField()

class Novidade(models.Model):

    dataPrimeiroAcesso = models.DateField(auto_now_add=True)
    idioma = models.TextField()
    resumo = models.TextField(blank=True)
    subject = models.TextField(blank=True, null=True)
    portal = models.CharField(blank=True, max_length=255)
    autores = models.TextField(blank=True)
    fonte = models.URLField()
    link_externo = models.URLField(blank=True)
    jornal = models.TextField(blank=True)
    titulo = models.TextField(unique=True)
    categoria = models.TextField(blank=True)
    data_publicacao = models.TextField(blank=True)
    portalBusca = models.ForeignKey("PortalBusca", on_delete=models.CASCADE, null=True)
    credibilidade = models.ForeignKey("Credibilidade", on_delete=models.CASCADE, null=True)
    especialista = models.ForeignKey("Especialista", on_delete=models.CASCADE, null=True)

    class Meta:
      db_table = "app_novidade"

def query_posts_by_args(**kwargs):
  draw = int(kwargs.get('draw', None)[0])
  length = int(kwargs.get('length', None)[0])
  start = int(kwargs.get('start', None)[0])
  search_value = kwargs.get('search[value]', None)[0]
  order_column = kwargs.get('order[0][column]', None)[0]
  order = kwargs.get('order[0][dir]', None)[0]
  titulo_resumo = kwargs.get('columns[1][search][value]', None)[0]
  autores = kwargs.get('columns[3][search][value]', None)[0]
  idioma = kwargs.get('columns[2][search][value]', None)[0]
  dataMinA = kwargs.get('columns[6][search][value]', None)[0]
  dataMaxA = kwargs.get('extra_value2', None)[0]
  dataMin = kwargs.get('columns[7][search][value]', None)[0]
  dataMax = kwargs.get('extra_value', None)[0]


  #opcões
  opcTituloResumo = kwargs.get('opcTituloResumo', None)[0]
  radio_TituloResumo = kwargs.get('radio_TituloResumo', None)[0]
  radio_autores = kwargs.get('radio_autores', None)[0]

  order_column = ORDER_COLUMN_CHOICES[order_column]

  # django orm '-' -> desc
  if order == 'desc':
    order_column = '-' + order_column

  queryset = Novidade.objects.all()
  total = queryset.count()

  if search_value:
      filtroBuscaGlobal = FiltroBuscaGlobal(search_value, queryset)
      queryset = filtroBuscaGlobal.filtrar()
  
  if titulo_resumo:

    if opcTituloResumo != 'resumo':
      querysetTitulo = queryset
      filtroTitulo = FiltroTituloResumo(titulo_resumo, querysetTitulo, "titulo")

      if radio_TituloResumo == "tt":
        querysetTitulo = filtroTitulo.TodosTermos()     

      elif radio_TituloResumo == "qt":
        queryset_vazia = Novidade.objects.none()
        querysetTitulo = filtroTitulo.QualquerTermo(queryset_vazia)

      elif radio_TituloResumo == "nt":
        querysetTitulo = filtroTitulo.NenhumTermo()

    if opcTituloResumo != 'titulo':
      querysetResumo = queryset
      filtroResumo = FiltroTituloResumo(titulo_resumo, querysetResumo, "resumo")
    
      if radio_TituloResumo == "tt":
        querysetResumo= filtroResumo.TodosTermos()  

      elif radio_TituloResumo == "qt":
        queryset_vazia = Novidade.objects.none()
        querysetResumo = filtroResumo.QualquerTermo(queryset_vazia)

      elif radio_TituloResumo == "nt":
        querysetResumo = filtroResumo.NenhumTermo()

    if opcTituloResumo == 'tituloEresumo':
      queryset = querysetResumo & querysetTitulo

    elif opcTituloResumo == 'tituloOUresumo':
      queryset = querysetResumo | querysetTitulo

    elif opcTituloResumo == 'titulo':
      queryset = querysetTitulo

    else:
      queryset = querysetResumo

  if idioma:
    queryset = queryset.filter(Q(idioma__icontains=idioma))

  if autores:
     filtroAutores = FiltroAutores(autores, queryset)

     if radio_autores == "tt":
      queryset = filtroAutores.TodosAutores()

     elif radio_autores == "qt":
      queryset_vazia = Novidade.objects.none()
      queryset = filtroAutores.QualquerAutor(queryset_vazia)

     elif radio_autores == "nt":
      queryset = filtroAutores.NenhumAutor()

  if dataMinA or dataMaxA:
    filtroDataAcesso = FiltroDatas(dataMinA, dataMaxA, queryset, "acesso")
    queryset = filtroDataAcesso.FiltrarData()

  if dataMin or dataMax:
    filtroDataPublicacao = FiltroDatas(dataMin, dataMax, queryset, "publicacao")
    queryset = filtroDataPublicacao.FiltrarData()

  count = queryset.count()
  if length == -1:
      queryset = queryset.order_by(order_column)
  else:
      queryset = queryset.order_by(order_column)[start:start + length]

  return{
  			'items': queryset,
  			'count': count,
  			'total': total,
  			'draw': draw
  		}

class Especialista(models.Model):
	nome = models.TextField()
	especialidade = models.TextField()

class Assunto(models.Model):
	descricao = models.TextField()
	palavrasChaves = models.TextField()
	dataInclusao = models.DateField()
	stringBusca = models.TextField()
	novidade = models.ManyToManyField("Novidade")

class AvisoPorEmail(models.Model):
	dataInicialRecebim = models.DateField()
	dataFinalRecebim = models.DateField()
	poisNovidade = models.TextField()
	credibilidadeAviso = models.ForeignKey("Credibilidade", on_delete=models.CASCADE)
	assuntoAviso = models.ForeignKey("Assunto", on_delete=models.CASCADE)
	pesquisador = models.ForeignKey("Pesquisador", on_delete=models.CASCADE)

class Credibilidade(models.Model):
	descricao = models.TextField()

class Pesquisador(models.Model):
	nome = models.TextField()


