# Generated by Django 2.2.5 on 2021-03-31 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, upload_to='reports'),
        ),
    ]