# Generated by Django 3.2.6 on 2021-08-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_illustrationproducttype_illustration'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='price',
            field=models.DecimalField(decimal_places=2, default=30, max_digits=8),
            preserve_default=False,
        ),
    ]