# Generated by Django 4.1.3 on 2022-11-24 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='state',
            new_name='country',
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together={('name', 'country')},
        ),
    ]
