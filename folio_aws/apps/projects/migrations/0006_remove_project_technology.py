# Generated by Django 3.2.10 on 2021-12-15 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_repo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
    ]
