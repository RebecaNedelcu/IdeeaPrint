# Generated by Django 3.2.6 on 2021-08-31 09:43

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_contactmessage_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='illustration',
        ),
        migrations.RemoveField(
            model_name='productdetails',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productdetails',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='sarmale', max_length=125),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='shop.product'),
        ),
        migrations.CreateModel(
            name='ProductIllustration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('illustration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.illustration')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
