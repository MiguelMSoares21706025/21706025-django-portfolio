# Generated by Django 4.2.1 on 2023-06-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_remove_tech_backend_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
    ]
