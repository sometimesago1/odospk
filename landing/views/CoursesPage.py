from django.views.generic import ListView

class CoursesPage(ListView):
    template_name = 'landing/pages/courses.html'

    def get_queryset(self):
        pass