# Generated by Django 2.2.2 on 2019-06-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirp',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
