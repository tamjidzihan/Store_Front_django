# Generated by Django 4.2.5 on 2023-09-19 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_like_date_alter_like_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.customer'),
        ),
    ]
