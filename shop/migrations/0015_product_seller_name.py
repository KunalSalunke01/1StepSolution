# Generated by Django 5.0.4 on 2024-04-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_condn_product_curr_year_product_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
