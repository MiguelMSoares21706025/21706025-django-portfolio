# Generated by Django 4.2.1 on 2023-06-13 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0034_alter_article_description1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
