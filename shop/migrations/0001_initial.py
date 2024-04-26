# Generated by Django 5.0.4 on 2024-04-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobno', models.IntegerField()),
                ('email', models.EmailField(default='@gmail.com', max_length=100)),
                ('curr_year', models.IntegerField()),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('category', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
