# Generated by Django 3.2.13 on 2023-01-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_survey_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='c3',
            field=models.ManyToManyField(blank=True, to='dash.Tour_operator_dissatisfaction', verbose_name='C3_(If c2 is dissatisfaction) Reason behind dissatisfaction'),
        ),
        migrations.AddField(
            model_name='survey',
            name='c3_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='C3_1_(If c2 is dissatisfaction) Others (Reason behind dissatisfaction)'),
        ),
    ]