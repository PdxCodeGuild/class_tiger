# Generated by Django 2.2.1 on 2019-06-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0002_auto_20190611_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=500)),
                ('short_url', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Short',
        ),
    ]
