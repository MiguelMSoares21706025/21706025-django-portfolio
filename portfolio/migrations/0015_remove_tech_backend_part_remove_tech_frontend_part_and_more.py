# Generated by Django 4.2.1 on 2023-06-10 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tech_backend',
            name='part',
        ),
        migrations.RemoveField(
            model_name='tech_frontend',
            name='part',
        ),
        migrations.RemoveField(
            model_name='tech_other',
            name='part',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio/static/portfolio/images/'),
        ),
    ]
