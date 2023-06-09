# Generated by Django 4.2.1 on 2023-06-12 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_rename_assunto_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='tech_backend',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='be_techs', to='portfolio.subject'),
        ),
        migrations.AddField(
            model_name='tech_frontend',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fe_techs', to='portfolio.subject'),
        ),
        migrations.AddField(
            model_name='tech_other',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_techs', to='portfolio.subject'),
        ),
    ]
