# Generated by Django 4.2.7 on 2023-12-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='csv_file',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='json_file',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
