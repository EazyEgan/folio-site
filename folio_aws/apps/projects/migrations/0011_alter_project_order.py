# Generated by Django 4.0 on 2022-02-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_order_alter_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='order',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
