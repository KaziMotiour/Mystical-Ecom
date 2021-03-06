# Generated by Django 3.2.4 on 2021-06-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210630_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discountPrice',
            field=models.DecimalField(decimal_places=2, default=0, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Discount price'),
        ),
    ]
