# Generated by Django 5.0.4 on 2024-04-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='Seller Name', max_length=50),
        ),
    ]
