# Generated by Django 4.2.6 on 2023-11-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='course',
            field=models.CharField(default='', max_length=10),
        ),
    ]