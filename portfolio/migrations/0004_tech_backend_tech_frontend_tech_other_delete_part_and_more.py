# Generated by Django 4.2.1 on 2023-06-10 10:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_academic_curricularunit_rename_technology_tech_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech_BackEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('release_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
                ('author', models.CharField(default='', max_length=30)),
                ('logo', models.ImageField(upload_to='portfolio/images/')),
                ('part', models.CharField(default='', max_length=10)),
                ('website_link', models.URLField()),
                ('description', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tech_FrontEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('release_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
                ('author', models.CharField(default='', max_length=30)),
                ('logo', models.ImageField(upload_to='portfolio/images/')),
                ('part', models.CharField(default='', max_length=10)),
                ('website_link', models.URLField()),
                ('description', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tech_Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('release_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
                ('author', models.CharField(default='', max_length=30)),
                ('logo', models.ImageField(upload_to='portfolio/images/')),
                ('part', models.CharField(default='', max_length=10)),
                ('website_link', models.URLField()),
                ('description', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.DeleteModel(
            name='Tech',
        ),
        migrations.DeleteModel(
            name='TechAuthor',
        ),
    ]
