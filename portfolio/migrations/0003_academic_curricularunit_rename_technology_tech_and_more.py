# Generated by Django 4.2.1 on 2023-06-10 10:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_academiccourse_article_author_certification_class_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CurricularUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curricular_unit', models.CharField(default='', max_length=50)),
                ('link', models.URLField()),
                ('year', models.IntegerField(default=1)),
                ('semester', models.CharField(default='1', max_length=5)),
                ('ects', models.IntegerField(default=1)),
                ('ranking', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curricular_units', to='portfolio.academic')),
                ('teachers', models.ManyToManyField(related_name='teachers', to='portfolio.teacher')),
            ],
        ),
        migrations.RenameModel(
            old_name='Technology',
            new_name='Tech',
        ),
        migrations.RemoveField(
            model_name='class',
            name='class_teachers',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='areas',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='course_class',
            new_name='curricular_unit',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='other_link',
            new_name='gitHub_link',
        ),
        migrations.RemoveField(
            model_name='techauthor',
            name='parts',
        ),
        migrations.DeleteModel(
            name='AcademicCourse',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
