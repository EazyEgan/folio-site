# Generated by Django 3.2.10 on 2021-12-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repo',
            field=models.URLField(blank=True),
        ),
    ]
