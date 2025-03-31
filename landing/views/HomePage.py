from django.views.generic import TemplateView
from landing.forms import ConsultationForm

class HomePage(TemplateView):
    template_name = 'landing/pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consult_form'] = ConsultationForm()
        return context