# Generated by Django 3.0.8 on 2020-07-30 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='nickname',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_number',
            new_name='major',
        ),
    ]
