from django.db import models

class CourseTypeModel(models.Model):
    name = models.CharField(max_length=9, unique=True, verbose_name='Тип курса')

    def __str__(self):
        return self.name