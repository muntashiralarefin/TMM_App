# Generated by Django 3.2.13 on 2023-01-04 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0006_auto_20230104_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='g1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dash.opinion_hawker', verbose_name='G1_What is your opinion on presence of hawker in tourist spot?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='g2',
            field=models.ManyToManyField(blank=True, to='dash.Negative_reason_hawker', verbose_name='G2_(If g1 is negative) Reasons behind negative opinion'),
        ),
        migrations.AddField(
            model_name='survey',
            name='g2_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='G2_1_ Other (Reasons behind negative opinion)'),
        ),
        migrations.AddField(
            model_name='survey',
            name='g3',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='G3_ Do you think rehabilitation of hawkers is necessary?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='g4',
            field=models.ManyToManyField(blank=True, to='dash.Hawker_suggest', verbose_name='G4_ What are your recommendations to increase the skill of hawkers?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='g4_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='G4_1_ Others ( What are your recommendations to increase the skill of hawkers?)'),
        ),
        migrations.AddField(
            model_name='survey',
            name='i1',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='I1_Do you think this tourist spot is cleaned enough?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='i2',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='I2_Do you think you are cooperating to clean this area?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='i3',
            field=models.ManyToManyField(blank=True, to='dash.Clean_suggestion', verbose_name='I3_ What is your recemmendation to clean this area?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='i3_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='I3_1_ Others'),
        ),
        migrations.AddField(
            model_name='survey',
            name='k1',
            field=models.ManyToManyField(blank=True, to='dash.Spot_expectation', verbose_name='K1_What you expect from tourist spot?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='k1_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='K1_1_ Others ( What you expect from tourist spot?)'),
        ),
        migrations.AddField(
            model_name='survey',
            name='k2',
            field=models.ManyToManyField(blank=True, to='dash.Recommendation_improve', verbose_name='K2_How tourism sector can be developed according to you?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='k2_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='K2_1_ Other ( How tourism sector can be developed according to you?)'),
        ),
    ]
