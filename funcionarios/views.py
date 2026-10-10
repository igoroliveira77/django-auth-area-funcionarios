from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'funcionarios/home.html'


class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionarios/painel.html'


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'funcionarios/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['funcionario'] = self.request.user
        return context
