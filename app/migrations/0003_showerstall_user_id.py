# Generated by Django 3.1 on 2020-08-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_showerqueue'),
    ]

    operations = [
        migrations.AddField(
            model_name='showerstall',
            name='user_id',
            field=models.IntegerField(default=None),
        ),
    ]
