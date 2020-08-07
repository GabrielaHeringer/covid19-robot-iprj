from app.serializers import NovidadeSerializer
from app.models import query_posts_by_args, Novidade
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.template.response import TemplateResponse
from django.http.response import HttpResponse

def WebPostList(request):
	html = TemplateResponse(request, 'app/web_post_list.html')
	return HttpResponse(html.render())
	
def subjects(request):
	html = TemplateResponse(request, 'app/subjects.html')
	return HttpResponse(html.render())

def database(request):
	html = TemplateResponse(request, 'app/database.html')
	return HttpResponse(html.render())

def help(request):
        html = TemplateResponse(request, 'app/help.html')
        return HttpResponse(html.render())

def about(request):
        html = TemplateResponse(request, 'app/about.html')
        return HttpResponse(html.render())

class NovidadeViewSet(viewsets.ModelViewSet):
	queryset = Novidade.objects.all()
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
