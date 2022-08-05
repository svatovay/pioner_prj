from django.db import models
from eduprogramsapp.models import EduProgram


class SocialStatus(models.Model):
    name = models.CharField(verbose_name='Наименование статуса', max_length=30, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.name}'


class HealthLimitations(models.Model):
    name = models.CharField(verbose_name='Наименование ОВЗ', max_length=50, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=20)
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    patronymic = models.CharField(verbose_name='Отчество', max_length=20)
    birth_date = models.DateField(verbose_name='Дата рождения')
    social_status = models.ForeignKey(SocialStatus, on_delete=models.SET_DEFAULT, default=None)
    health_limitations = models.ForeignKey(HealthLimitations, on_delete=models.SET_DEFAULT, default=None)
    disability = models.BooleanField(verbose_name='Инвалидность', default=False)
    edu_program = models.ManyToManyField(EduProgram)  # ДОП
