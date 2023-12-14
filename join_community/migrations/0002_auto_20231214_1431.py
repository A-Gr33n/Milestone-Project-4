# Generated by Django 3.2.3 on 2023-12-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscription',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]