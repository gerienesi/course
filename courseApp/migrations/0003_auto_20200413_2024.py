# Generated by Django 3.0.5 on 2020-04-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0001_initial'),
        ('courseApp', '0002_remove_course_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseContent',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='studentApp.Student'),
        ),
    ]
