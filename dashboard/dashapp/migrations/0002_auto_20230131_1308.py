# Generated by Django 3.1.14 on 2023-01-31 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='e_ao',
            new_name='Email',
        ),
    ]
