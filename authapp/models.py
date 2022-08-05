from django.db import models
from django.contrib.auth.models import AbstractUser


class PositionPionerUser(models.Model):
    name = models.CharField(verbose_name='Наименование должности', max_length=20, blank=False)
    description = models.TextField(verbose_name='Описание должности', blank=True)
    is_timetable_manager = models.BooleanField(verbose_name='Редактирование расписания', default=False)
    is_methodist = models.BooleanField(verbose_name='Редактирование программ', default=False)
    is_teacher = models.BooleanField(verbose_name='Редактирование журнала учёта занятий', default=False)

    def __str__(self):
        return f'{self.name}'


class PionerUser(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(verbose_name='Фамилия', max_length=20)
    patronymic = models.CharField(verbose_name='Отчество', max_length=20, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    position = models.ForeignKey(
        PositionPionerUser,
        verbose_name='Должность',
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
