# Generated by Django 3.2.13 on 2023-01-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_auto_20230101_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='b8',
            field=models.ManyToManyField(blank=True, to='dash.Cbt_Recommendation', verbose_name='(If b3 is yes) What are your recommendations to improve community based tourism?'),
        ),
        migrations.AddField(
            model_name='survey',
            name='b8_1',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='(If b3 is yes) Others (What are your recommendations to improve community based tourism?)'),
        ),
    ]
