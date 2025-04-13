from django.views.generic import TemplateView
from landing.forms import ConsultationFormDark
from django.shortcuts import render, redirect

class HomePage(TemplateView):
    template_name = 'landing/pages/index.html'
    form_class = ConsultationFormDark

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consult_form'] = self.form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            pass
            return redirect('home')
        else:
            context = self.get_context_data()
            context['consult_form'] = form
            return render(request, self.template_name, context)