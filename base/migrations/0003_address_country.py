# Generated by Django 4.2.5 on 2023-09-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
