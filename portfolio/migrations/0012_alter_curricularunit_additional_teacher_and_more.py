# Generated by Django 4.2.1 on 2023-06-10 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_curricularunit_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curricularunit',
            name='additional_teacher',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_teachers', to='portfolio.teacher'),
        ),
        migrations.AlterField(
            model_name='curricularunit',
            name='responsible_teacher',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsible_teachers', to='portfolio.teacher'),
        ),
    ]
