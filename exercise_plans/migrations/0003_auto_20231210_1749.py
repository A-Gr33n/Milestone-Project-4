# Generated by Django 3.2.3 on 2023-12-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_plans', '0002_auto_20231210_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='reps',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
