# Generated by Django 4.2.1 on 2023-06-15 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0035_remove_comment_comment_delete_news_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='url("../images/backiee-5769412.jpg")', upload_to='portfolio/static/portfolio/images/'),
        ),
    ]
