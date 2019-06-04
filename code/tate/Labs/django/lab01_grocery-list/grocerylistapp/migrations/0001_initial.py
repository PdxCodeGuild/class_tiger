# Generated by Django 2.2.1 on 2019-05-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=200)),
                ('item_quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
    ]
