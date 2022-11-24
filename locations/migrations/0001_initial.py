# Generated by Django 4.1.3 on 2022-11-24 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geography', '0004_city_deleted_at_country_deleted_at_state_deleted_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.city')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
