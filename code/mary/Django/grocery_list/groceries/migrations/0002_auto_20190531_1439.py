# Generated by Django 2.2.1 on 2019-05-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date completed'),
        ),
    ]