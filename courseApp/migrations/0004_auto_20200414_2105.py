# Generated by Django 3.0.5 on 2020-04-14 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0001_initial'),
        ('courseApp', '0003_auto_20200413_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='studentApp.Student'),
        ),
    ]
