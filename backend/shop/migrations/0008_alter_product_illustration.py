# Generated by Django 3.2.6 on 2021-08-30 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210827_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='illustration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.illustration'),
        ),
    ]