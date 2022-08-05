# Generated by Django 4.0.3 on 2022-06-12 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eduprogramsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthLimitations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование ОВЗ')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='SocialStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование статуса')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('disability', models.BooleanField(default=False, verbose_name='Инвалидность')),
                ('edu_program', models.ManyToManyField(to='eduprogramsapp.eduprogram')),
                ('health_limitations', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='studentsapp.healthlimitations')),
                ('social_status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='studentsapp.socialstatus')),
            ],
        ),
    ]
