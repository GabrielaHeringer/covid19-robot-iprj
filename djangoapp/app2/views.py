from app2.serializers import NovidadeSerializer
from app2.models import query_posts_by_args, Novidade2, Profile, AvisoPorEmail
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from app2.forms import UserModelForm, ProfileForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, send_mass_mail

def WebPostList2(request):
	html = TemplateResponse(request, 'app2/web_post_list2.html')
	return HttpResponse(html.render())
	
def subjects2(request):
	html = TemplateResponse(request, 'app2/subjects2.html')
	return HttpResponse(html.render())

def database2(request):
	html = TemplateResponse(request, 'app2/database2.html')
	return HttpResponse(html.render())

def help2(request):
        html = TemplateResponse(request, 'app2/help2.html')
        return HttpResponse(html.render())

def about2(request):
        html = TemplateResponse(request, 'app2/about2.html')
        return HttpResponse(html.render())

@login_required(login_url='/login/')
def criar_alerta(request):
        alertas = AvisoPorEmail.objects.filter(user_alerta=request.user.id)
        igual = False
        if request.method == 'POST':
            nome = request.POST.get('nome_alerta')
            frequencia = request.POST.get('frequencia')
            busca_global = request.POST.get('busca_global')
            idiomas = request.POST.get('idiomas')
            autor = request.POST.get('autor')
            titulo_e_resumo = request.POST.get('titulo_e_resumo')
            opcao_titulo_resumo = request.POST.get('titulo_resumo')
            button_autores = request.POST.get('tipoAutores')
            button_titulo_e_resumo = request.POST.get('tipoTituloResumo')
            if busca_global or idiomas or autor or titulo_e_resumo:
                for alerta in alertas:
                    if alerta.busca_global == busca_global and alerta.idiomas == idiomas and alerta.titulo_e_resumo == titulo_e_resumo and alerta.autor == autor and alerta.opcao_titulo_resumo == opcao_titulo_resumo and alerta.button_titulo_e_resumo == button_titulo_e_resumo and alerta.button_autores == button_autores:
                        igual = True

                if not igual:
                    aviso = AvisoPorEmail.objects.create(nome=nome, frequencia=frequencia, busca_global=busca_global, titulo_e_resumo=titulo_e_resumo,
                                        idiomas=idiomas, autor=autor, button_titulo_e_resumo=button_titulo_e_resumo, button_autores=button_autores, opcao_titulo_resumo=opcao_titulo_resumo, user_alerta_id=request.user.id)
                    return redirect('/cadastro/meus-alertas/')
                else:
                    messages.error(request, 'Esse alerta já foi criado. Verifique seus alertas.')
            else:
                messages.error(request, 'Alerta vazio. Preencha pelo menos um campo.')

        html = TemplateResponse(request, 'app2/criar_alerta.html')
        return HttpResponse(html.render())

@login_required(login_url='/login/')
def meus_alertas(request):
        profile = Profile.objects.get(user_id=request.user.id)
        alertas = AvisoPorEmail.objects.filter(user_alerta=request.user.id)
        dic = {'profile':profile, 'alertas': alertas}
        html = TemplateResponse(request, 'app2/meus_alertas.html', dic)
        return HttpResponse(html.render())

@login_required(login_url='/login/')
def delete_alerta(request, id):
    alerta = AvisoPorEmail.objects.get(id=id)
    if alerta:
        alerta.delete()
    return redirect('/cadastro/meus-alertas/')

@login_required(login_url='/login/')
def editar_alerta(request, id):
        editar = AvisoPorEmail.objects.get(id=id)
        alertas = AvisoPorEmail.objects.filter(user_alerta=request.user.id)
        igual = False
        if request.method == 'POST':
            nome = request.POST.get('nome_alerta')
            frequencia = request.POST.get('frequencia')
            busca_global = request.POST.get('busca_global')
            idiomas = request.POST.get('idiomas')
            autor = request.POST.get('autor')
            titulo_e_resumo = request.POST.get('titulo_e_resumo')
            opcao_titulo_resumo = request.POST.get('titulo_resumo')
            button_autores = request.POST.get('tipoAutores')
            button_titulo_e_resumo = request.POST.get('tipoTituloResumo')
            if busca_global or idiomas or autor or titulo_e_resumo:
                for alerta in alertas:
                    if alerta.busca_global == busca_global and alerta.idiomas == idiomas and alerta.titulo_e_resumo == titulo_e_resumo and alerta.autor == autor:
                        if alerta.opcao_titulo_resumo == opcao_titulo_resumo or (alerta.opcao_titulo_resumo != opcao_titulo_resumo and alerta.titulo_e_resumo == "" and titulo_e_resumo == ""):
                            if alerta.button_titulo_e_resumo == button_titulo_e_resumo or (alerta.button_titulo_e_resumo != button_titulo_e_resumo and alerta.titulo_e_resumo == "" and titulo_e_resumo == ""):
                                if alerta.button_autores == button_autores or (alerta.button_autores != button_autores and alerta.autor == "" and autor == ""):
                                    if alerta.id != editar.id:
                                        igual = True
                                    else:
                                        if nome == alerta.nome and frequencia == alerta.frequencia:
                                            igual = True

                if not igual:
                    editar.nome = nome
                    editar.frequencia = frequencia
                    editar.busca_global = busca_global
                    editar.idiomas = idiomas
                    editar.autor = autor
                    editar.titulo_e_resumo = titulo_e_resumo
                    editar.opcao_titulo_resumo = opcao_titulo_resumo
                    editar.button_autores = button_autores
                    editar.button_titulo_e_resumo = button_titulo_e_resumo
                    editar.save()
                    return redirect('/cadastro/meus-alertas')
                else:
                    messages.error(request, 'Esse alerta já foi criado. Verifique seus alertas.')
            else:
                messages.error(request, 'Alerta vazio. Preencha pelo menos um campo.')

        html = TemplateResponse(request, 'app2/meus_alertas.html', {'alerta': editar})
        return HttpResponse(html.render())

@login_required(login_url='/login/')
def perfil(request):
        profile = Profile.objects.get(user_id=request.user.id)
        alertas = AvisoPorEmail.objects.filter(user_alerta=request.user.id)
        if request.method == 'POST':
            pais = request.POST.get('pais')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            profissao = request.POST.get('profissao')
            organizacao = request.POST.get('organizacao')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user = request.user
            if User.objects.filter(email=email).exists():
                    messages.error(request, 'E-mail já cadastrado.')
            else:
                    user.email = email
            user.first_name = first_name
            user.last_name = last_name
            profile.telefone = telefone
            profile.organizacao = organizacao
            profile.pais = pais
            user.save()
            profile.save()

        html = TemplateResponse(request, 'app2/perfil.html', {'profile':profile, 'alertas':alertas})
        return HttpResponse(html.render())

def register(request):
	user_form = UserModelForm(request.POST or None)
	profile_form = ProfileForm(request.POST or None)
	context = {'user_form': user_form, 'profile_form': profile_form}
	if request.method == 'POST':
		if user_form.is_valid() and profile_form.is_valid():
                        email = request.POST['email']
                        if User.objects.filter(email=email).exists():
                            messages.error(request, 'E-mail já cadastrado.')
                        else:
                            user = user_form.save()
                            profile = profile_form.save(commit=False)
                            profile.user = user
                            profile.save()
                            return redirect('/cadastro/login')
		#else:
                        #messages.error(request, 'Favor tentar novamente.')

	html = TemplateResponse(request, 'app2/register.html', context)
	return HttpResponse(html.render())

@csrf_protect
def submit_login(request):
        if request.method == "POST":   
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
       
                if user is not None:
                        login(request, user)
                        return redirect('/cadastro/')
                else:
                        messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    
        html = TemplateResponse(request, 'app2/login.html')
        return HttpResponse(html.render())

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/cadastro/')

def error_404_view(request, exception):
    html = TemplateResponse(request, 'app2/404.html')
    return HttpResponse(html.render())

def error_500_view(request):
    html = TemplateResponse(request, 'app2/500.html')
    return HttpResponse(html.render()) 

class NovidadeViewSet(viewsets.ModelViewSet):
	queryset = Novidade2.objects.using('replica1').all()
	serializer_class = NovidadeSerializer

	def list(self, request, **kwargs):
		try:
			novidades = query_posts_by_args(**request.query_params)
			serializer = NovidadeSerializer(novidades['items'], many=True)
			result = dict()
			result['data'] = serializer.data
			result['draw'] = novidades['draw']
			result['recordsTotal'] = novidades['total']
			result['recordsFiltered'] = novidades['count']

			return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

		except Exception as e:
			return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

def email():
	avisos = AvisoPorEmail.objects.filter(frequencia='Semanal')
	for aviso in avisos:
        	user = aviso.user_alerta.id
        	usuario = User.objects.get(id=user)
       		send_mail(
                	'Assunto - test',
                	'<h1>Infos dos Alertas</h1> <br> Nome: {} <br> Frequencia: {} <br>'.format(aviso.nome, aviso.frequencia),
                	'projetorococovid@gmail.com',
                	[usuario.email, 'lucas-de-paula@hotmail.com', 'meohisse@gmail.com'],
                	fail_silently=False,
        	)
