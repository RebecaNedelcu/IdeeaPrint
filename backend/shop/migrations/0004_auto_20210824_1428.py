# Generated by Django 3.2.6 on 2021-08-24 11:28

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210817_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Illustration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='productdetails',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='product',
        ),
        migrations.AddField(
            model_name='productdetails',
            name='cantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdetails',
            name='sex',
            field=models.CharField(choices=[('M', 'Man'), ('F', 'Woman'), ('U', 'Unisex')], default='M', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimages',
            name='product_details',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='shop.productdetails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('1', 'T-Shirts'), ('2', 'Hoodies'), ('3', 'Mugs'), ('4', 'Totebags')], max_length=4),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=6),
        ),
        migrations.AddField(
            model_name='product',
            name='illustration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.illustration'),
            preserve_default=False,
        ),
    ]
