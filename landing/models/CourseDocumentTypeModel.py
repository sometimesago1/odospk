from django.db import models

class CourseDocumentTypeModel(models.Model):
    name = models.CharField(max_length=9, unique=True, verbose_name='Выдаваемый документ')

    def __str__(self):
        return self.name