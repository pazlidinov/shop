# Generated by Django 4.1.7 on 2023-04-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_remove_product_img_name_product_img_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='colors', to='main_app.color'),
        ),
    ]