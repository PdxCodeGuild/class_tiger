# Generated by Django 2.2.1 on 2019-06-12 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Short',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_url', models.CharField(max_length=500)),
                ('short', models.CharField(default='', max_length=10)),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='ShortUrl',
        ),
    ]
