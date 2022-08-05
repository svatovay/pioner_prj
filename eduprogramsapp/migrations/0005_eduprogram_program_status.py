# Generated by Django 4.0.3 on 2022-07-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprogramsapp', '0004_alter_eduprogram_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduprogram',
            name='program_status',
            field=models.CharField(choices=[('A', 'Реализуется'), ('NA', 'Не реализуется'), ('D', 'Удалена')], default='NA', max_length=20, verbose_name='Статус программы'),
        ),
    ]
