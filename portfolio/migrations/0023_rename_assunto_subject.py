# Generated by Django 4.2.1 on 2023-06-12 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_rename_subject_assunto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assunto',
            new_name='Subject',
        ),
    ]