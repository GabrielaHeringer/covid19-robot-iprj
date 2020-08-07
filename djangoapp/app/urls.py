from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# from musics import views
from app.views import NovidadeViewSet, WebPostList, subjects, database, help, about

app_name = 'app'

router = DefaultRouter()
router.register(r'novidade', NovidadeViewSet)

urlpatterns = [
    url(r'^$', WebPostList, name='WebPostList'),
    url(r'^subjects/', subjects, name='subjects'),
    url(r'^database/', database, name='database'),
    url(r'^help/', help, name='help'),
    url(r'^about/', about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
