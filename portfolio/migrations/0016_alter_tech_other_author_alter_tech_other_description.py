# Generated by Django 4.2.1 on 2023-06-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_remove_tech_backend_part_remove_tech_frontend_part_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech_other',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tech_other',
            name='description',
            field=models.CharField(default='', max_length=600),
        ),
    ]