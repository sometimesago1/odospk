from django.db import models
from django.core.validators import MinLengthValidator
from landing.models import CourseModel

class FeedbackModel(models.Model):
    customer = models.CharField(max_length=50, blank=False, null=False, verbose_name='Слушатель')
    course_complited_at = models.CharField(max_length=125, blank=False, null=False, verbose_name='Курс пройден')
    content = models.TextField(blank=False, null=False, validators=[
        MinLengthValidator(125, message='Отзыв должен быть не менее 125 символов')
    ])
    photo = models.ImageField(upload_to='static/img/feedbacks/', default=None, blank=True, null=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    #Foreign key
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='feedbacks')
    