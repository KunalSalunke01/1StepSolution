# Generated by Django 5.0.4 on 2024-04-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/shop/images/'),
        ),
    ]
