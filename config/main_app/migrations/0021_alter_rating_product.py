# Generated by Django 4.1.7 on 2023-05-12 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='main_app.product'),
        ),
    ]
