from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# from musics import views
from app2.views import NovidadeViewSet, WebPostList2, subjects2, database2, help2, about2, submit_login, register, logout_user, perfil, meus_alertas, editar_alerta, delete_alerta, criar_alerta

app_name = 'app2'

router = DefaultRouter()
router.register(r'novidade', NovidadeViewSet)

urlpatterns = [
    url(r'^$', WebPostList2, name='WebPostList2'),
    url(r'^subjects/', subjects2, name='subjects2'),
    url(r'^database/', database2, name='database2'),
    url(r'^help/', help2, name='help2'),
    url(r'^about/', about2, name='about2'),
    url(r'^register/', register, name='register'),
    url(r'^login/', submit_login, name='submit_login'),
    url(r'^logout/', logout_user, name='logout'),
    url(r'^perfil/', perfil, name='perfil'),
    url(r'^criar-alerta/', criar_alerta, name='criar_alerta'),
    url(r'^meus-alertas/', meus_alertas, name='meus_alertas'),
    path('editar-alerta/<slug:id>/', editar_alerta, name='editar_alerta'),
    path('excluir/<slug:id>/', delete_alerta, name='delete_alerta'),
    url(r'^password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='app2/registration/password_change_done.html'), 
        name='password_change_done'),

    url(r'^password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('app2:password_change_done'), template_name='app2/registration/password_change.html'), 
        name='password_change'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
