
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='usuarios/login.html',
            next_page='painel_funcionarios'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),
]
