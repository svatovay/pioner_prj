from django.db import models


class TypeProgram(models.Model):
    name = models.CharField(verbose_name='Тип', max_length=30, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        _ = self.name.split()
        return f'ДО{self.name[0].upper()}П' if len(_) == 1 else f'ДОП{_[0][0].upper()}{_[0][1].upper()}'


class OrientationProgram(models.Model):
    name = models.CharField(verbose_name='Направленность', max_length=30, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.name}'


class EduProgram(models.Model):
    class StatusChoice(models.TextChoices):
        ACTIVE_PROGRAM = 'A', 'Реализуется'
        NOT_ACTIVE_PROGRAM = 'NA', 'Не реализуется'
        DELETED_PROGRAM = 'D', 'Удалена'

    type = models.ForeignKey(
        TypeProgram,
        verbose_name='Тип программы',
        on_delete=models.SET_DEFAULT,
        default=None
    )

    orientation = models.ForeignKey(
        OrientationProgram,
        verbose_name='Направленность программы',
        on_delete=models.SET_DEFAULT,
        default=None
    )

    is_adapted = models.BooleanField(verbose_name='Адаптированность', default=False)
    duration = models.IntegerField(verbose_name='Продолжительность, ч', default=8)
    name = models.CharField(verbose_name='Наименование', max_length=250, blank=False, unique=True)
    description = models.TextField(verbose_name='Описание', blank=False)
    program_status = models.CharField(
        verbose_name='Статус программы',
        max_length=20,
        choices=StatusChoice.choices,
        blank=False,
        default=StatusChoice.NOT_ACTIVE_PROGRAM,
    )

    def __str__(self):
        return f'{self.type} "{self.name}"'


class WorkProgram(models.Model):
    edu_program = models.ForeignKey(
        EduProgram,
        verbose_name='Основная программа',
        on_delete=models.CASCADE,
        blank=False
    )
    duration = models.IntegerField(verbose_name='Продолжительность, ч')
    name = models.CharField(verbose_name='Наименование', max_length=250, blank=False)
    description = models.TextField(verbose_name='Описание', blank=False)
