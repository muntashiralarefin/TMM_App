# Generated by Django 3.2.13 on 2023-01-04 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20230104_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='c1',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='C1_Have you received service from tour operator?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='c2',
            field=models.CharField(blank=True, choices=[('Very satisfied', 'Very satisfied'), ('Satisfied', 'Satisfied'), ('Neutral', 'Neutral'), ('Dissatisfied', 'Dissatisfied'), ('Very dissatisfied', 'Very dissatisfied')], max_length=20, verbose_name='C2_(If c1 is yes) How you evaluate the professionalism of tour operators?'),
        ),
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
        migrations.AddField(
            model_name='survey',
            name='c4',
            field=models.ManyToManyField(blank=True, to='dash.Vacation_package', verbose_name='C4_As a tourist, what you want in a vacation package?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='c4_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='C4_1_Others (As a tourist, what you want in a vacation package?)'),
        ),
        migrations.AddField(
            model_name='survey',
            name='c5',
            field=models.ManyToManyField(blank=True, to='dash.Tour_operator_recommendation', verbose_name='C5_What are your recommendations for tour operators?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='c5_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='C5_1_ Others (What are your recommendations for tour operators?)'),
        ),
        migrations.AddField(
            model_name='survey',
            name='d1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dash.opinion', verbose_name='D1_What is your opinion on the cost of hotel in tourist spots?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='d2',
            field=models.CharField(blank=True, choices=[('Very satisfied', 'Very satisfied'), ('Satisfied', 'Satisfied'), ('Neutral', 'Neutral'), ('Dissatisfied', 'Dissatisfied'), ('Very dissatisfied', 'Very dissatisfied')], max_length=30, verbose_name='D2_Are you satisfied with hotel room service?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='d3',
            field=models.ManyToManyField(blank=True, to='dash.Room_service_dissatisfaction', verbose_name='D3_(If d2 is dissatisfaction) Reason behind dissatisfation'),
        ),
        migrations.AddField(
            model_name='survey',
            name='d3_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='D3_1_Others (What are your recommendations for tour operators?)'),
        ),
    ]
