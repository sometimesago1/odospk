from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse

class AvailableToEnrollManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available_slots__bt = CourseModel.available_slots)

class CourseModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=False, null=False, verbose_name='Слаг', validators=[
        MinLengthValidator(25, message='Название курса должно быть от 25 символов'),
        MaxLengthValidator(255, message='Название курса не может быть больше 255 символов')
    ])
    description = models.TextField(blank=False, verbose_name='Описание курса')
    course_duration = models.IntegerField(blank=False, null=False, verbose_name='Длительность обучения')
    available_slots = models.IntegerField(blank=True, null=True)
    graduates = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    photo = models.ImageField(upload_to='static/img/courses/', blank=True, default=None, null=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    #Foreing keys
    document_type = models.ForeignKey('CourseDocumentTypeModel', on_delete=models.CASCADE, related_name='document', verbose_name='Выдаваемый документ')
    course_type = models.ForeignKey('CourseTypeModel', on_delete=models.CASCADE, related_name='Type', verbose_name='Тип курса')

    #Managers
    objects = models.Manager()
    available_to_enroll = AvailableToEnrollManager()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-title']
        indexes = [
            models.Index(fields=['-title'])
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course', kwargs={'course_slug': self.slug})

