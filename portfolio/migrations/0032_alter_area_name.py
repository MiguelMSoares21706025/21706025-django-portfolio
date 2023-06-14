# Generated by Django 4.2.1 on 2023-06-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0031_alter_area_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(choices=[('Business', 'Business'), ('Technology', 'Technology'), ('Entertainment', 'Entertainment'), ('Lifestyle', 'Lifestyle'), ('Travel', 'Travel'), ('Sports', 'Sports'), ('Other', 'Other')], default='Business', max_length=15),
        ),
    ]
