from django.urls import path
from .views import HomeView, PainelView, PerfilView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('painel/', PainelView.as_view(), name='painel_funcionarios'),
    path('perfil/', PerfilView.as_view(), name='perfil_funcionario'),
]
