# Generated by Django 4.2.3 on 2023-08-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(null=2, upload_to=''),
            preserve_default=2,
        ),
    ]