# Generated by Django 3.2.13 on 2023-01-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_auto_20230101_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='c2',
            field=models.CharField(blank=True, choices=[('Very satisfied', 'Very satisfied'), ('Satisfied', 'Satisfied'), ('Neutral', 'Neutral'), ('Dissatisfied', 'Dissatisfied'), ('Very dissatisfied', 'Very dissatisfied')], max_length=20, verbose_name='C2_(If c1 is yes) How you evaluate the professionalism of tour operators?'),
        ),
    ]
