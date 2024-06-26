# Generated by Django 5.0.4 on 2024-04-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condn',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='curr_year',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default='@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='mobno',
            field=models.IntegerField(default='00000000'),
        ),
    ]
