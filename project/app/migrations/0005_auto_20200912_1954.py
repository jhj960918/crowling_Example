# Generated by Django 3.1 on 2020-09-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200911_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musinsadata',
            name='musinsaImage',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]