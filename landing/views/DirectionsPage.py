from django.views.generic import ListView

class DirectionsPage(ListView):
    template_name = 'landing/pages/directions.html'

    def get_queryset(self):
        pass
    
