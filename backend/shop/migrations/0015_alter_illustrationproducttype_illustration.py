# Generated by Django 3.2.6 on 2021-08-31 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20210831_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illustrationproducttype',
            name='illustration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_type', to='shop.illustration'),
        ),
    ]
