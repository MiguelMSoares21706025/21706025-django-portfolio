# Generated by Django 4.2.1 on 2023-06-12 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0032_alter_area_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='area',
        ),
        migrations.RemoveField(
            model_name='author',
            name='area',
        ),
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(choices=[('Business', 'Business'), ('Technology', 'Technology'), ('Entertainment', 'Entertainment'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Sports', 'Sports'), ('Other', 'Other')], default='Business', max_length=15),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
    ]
