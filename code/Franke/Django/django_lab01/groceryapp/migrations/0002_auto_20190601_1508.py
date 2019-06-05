# Generated by Django 2.2.1 on 2019-06-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]