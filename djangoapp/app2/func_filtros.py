from django.db.models import Q
import re

def func_idioma(idioma, queryset):
    if idioma == 'en_es':
        queryset = queryset.filter(Q(idioma__icontains='en') | Q(idioma__icontains='es'))
    elif idioma == 'en_pt':
        queryset = queryset.filter(Q(idioma__icontains='en') | Q(idioma__icontains='pt'))
    elif idioma == 'es_pt':
        queryset = queryset.filter(Q(idioma__icontains='es') | Q(idioma__icontains='pt'))
    else:
        queryset = queryset.filter(Q(idioma__icontains=idioma))
    return queryset

def func_autores(autores, queryset, queryset1, option_autores):
    """pattern = r"\"([^\"]*)\""
    palavras = re.findall(pattern, autores)

    for i in range(len(palavras)):
        if option_autores == 'and':
            autores = autores.replace('"', '')
            autores = autores.replace(palavras[i], '')
        else:
            autores = autores.replace('"' + palavras[i] + '"', '')"""
    autores = autores.split(',')
    print(autores)

    if option_autores == 'and':
        if len(autores) > 0:
            for i in range(len(autores)):
                queryset = queryset.filter(Q(autores__icontains=autores[i]))
        """if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset = queryset.filter(Q(autores__icontains=palavras[i]))"""

    elif option_autores == 'or':
        if len(autores) > 0:
            for i in range(len(autores)):
                queryset1 = queryset1 | queryset.filter(Q(autores__icontains=autores[i]))
        """if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset1 = queryset1 | queryset.filter(Q(autores__icontains=palavras[i]))"""    
        queryset = queryset1

    else:
        if len(autores) > 0:
            for i in range(len(autores)):
                queryset = queryset.exclude(Q(autores__icontains=autores[i]))
        """if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset = queryset.exclude(Q(autores__icontains=palavras[i]))"""
    return queryset

def func_titulo(titulo, queryset, queryset1, option_titulo):
    pattern = r"\"([^\"]*)\""
    palavras = re.findall(pattern, titulo)
            
    for i in range(len(palavras)):
        if option_titulo == 'and':
            titulo = titulo.replace('"', '')
            titulo = titulo.replace(palavras[i], '')
        else:
            titulo = titulo.replace('"' + palavras[i] + '"', '')
    titulo = titulo.split()

    if option_titulo == 'and':
        if len(titulo) > 0:
            for i in range(len(titulo)):
                queryset = queryset.filter(Q(titulo__icontains=titulo[i]))
        if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset = queryset.filter(Q(titulo__icontains=palavras[i]))

    elif option_titulo == 'or':
        if len(titulo) > 0:
            for i in range(len(titulo)):
                queryset1 = queryset1 | queryset.filter(Q(titulo__icontains=titulo[i]))
        if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset1 = queryset1 | queryset.filter(Q(titulo__icontains=palavras[i]))    
        queryset = queryset1

    else:
        if len(titulo) > 0:
            for i in range(len(titulo)):
                queryset = queryset.exclude(Q(titulo__icontains=titulo[i]))
        if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset = queryset.exclude(Q(titulo__icontains=palavras[i]))
    return queryset

def func_resumo(resumo, queryset, queryset1, option_resumo):
    pattern = r"\"([^\"]*)\""
    palavras = re.findall(pattern, resumo)
    
    for i in range(len(palavras)):
        if option_resumo == 'and':
            resumo = resumo.replace('"', '')
            resumo = resumo.replace(palavras[i], '')
        else:
            resumo = resumo.replace('"' + palavras[i] + '"', '')
    resumo = resumo.split()

    if option_resumo == 'and':
        if len(resumo) > 0:
            for i in range(len(resumo)):
                queryset = queryset.filter(Q(resumo__icontains=resumo[i]))
        if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset = queryset.filter(Q(resumo__icontains=palavras[i]))

    elif option_resumo == 'or':
        if len(resumo) > 0:
            for i in range(len(resumo)):
                queryset1 = queryset1 | queryset.filter(Q(resumo__icontains=resumo[i]))
        if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset1 = queryset1 | queryset.filter(Q(resumo__icontains=palavras[i]))    
        queryset = queryset1

    else:
        if len(resumo) > 0:
            for i in range(len(resumo)):
                queryset = queryset.exclude(Q(resumo__icontains=resumo[i]))
        if len(palavras) > 0:
            for i in range(len(palavras)):
                queryset = queryset.exclude(Q(resumo__icontains=palavras[i]))
    return queryset

def func_data_publi(dataMin, dataMax, queryset):
    if dataMin and not dataMax:
        queryset = queryset.filter(Q(data_publicacao__gte=dataMin))

    if not dataMin and dataMax:
        queryset = queryset.filter(Q(data_publicacao__lte=dataMax))

    if dataMin and dataMax:
        queryset = queryset.filter(Q(data_publicacao__gte=dataMin), Q(data_publicacao__lte=dataMax))
    return queryset

def func_data_acesso(dataMinAcesso, dataMaxAcesso, queryset):
    dataMinAcesso = dataMinAcesso.replace("/", "-")
    dataMaxAcesso = dataMaxAcesso.replace("/","-")
    if dataMinAcesso and not dataMaxAcesso:
        queryset = queryset.filter(Q(dataPrimeiroAcesso__gte=dataMinAcesso))

    if not dataMinAcesso and dataMaxAcesso:
        queryset = queryset.filter(Q(dataPrimeiroAcesso__lte=dataMaxAcesso))
        
    if dataMinAcesso and dataMaxAcesso:
        queryset = queryset.filter(Q(dataPrimeiroAcesso__gte=dataMinAcesso), Q(dataPrimeiroAcesso__lte=dataMaxAcesso))
    return queryset
