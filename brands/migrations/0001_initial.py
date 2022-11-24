# Generated by Django 4.1.3 on 2022-11-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
