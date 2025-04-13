from django.views.generic import ListView
from landing.forms import ConsultationForm
from django.shortcuts import render, redirect

class DirectionsPage(ListView):
    template_name = 'landing/pages/directions.html'
    form_class = ConsultationForm

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consult_form'] = self.form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            pass
            return redirect('directions')
        else:
            context = self.get_context_data()
            context['consult_form'] = form
            return render(request, self.template_name, context)
