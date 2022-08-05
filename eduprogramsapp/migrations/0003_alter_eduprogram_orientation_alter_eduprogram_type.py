# Generated by Django 4.0.3 on 2022-07-03 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduprogramsapp', '0002_rename_adapted_eduprogram_is_adapted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduprogram',
            name='orientation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='eduprogramsapp.orientationprogram', verbose_name='Направленность программы'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='eduprogramsapp.typeprogram', verbose_name='Тип программы'),
        ),
    ]
