# Generated by Django 3.2.4 on 2021-06-30 15:07

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, help_text='Change product visibility', verbose_name='Product visibility')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('sex', models.CharField(choices=[('All', 'All'), ('Male', 'Male'), ('Female', 'Female')], default='All', max_length=50)),
                ('SizeOrModels', models.CharField(max_length=50)),
                ('regularPrice', models.CharField(max_length=50)),
                ('discountPrice', models.CharField(max_length=50)),
                ('image1', models.ImageField(upload_to=products.models.product_image, verbose_name='Image field1')),
                ('image2', models.ImageField(upload_to=products.models.product_image, verbose_name='Image field2')),
                ('stock', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, help_text='Change product visibility', verbose_name='Product visibility')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
        ),
    ]
