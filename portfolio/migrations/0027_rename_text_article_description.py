# Generated by Django 4.2.1 on 2023-06-12 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_alter_article_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='description',
        ),
    ]