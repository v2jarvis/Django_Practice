# Generated by Django 4.2.7 on 2023-12-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_data', models.JSONField(blank=True, null=True)),
                ('csv_data', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
