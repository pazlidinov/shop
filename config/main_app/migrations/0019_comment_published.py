# Generated by Django 4.1.7 on 2023-05-10 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 5, 10, 6, 24, 6, 453846, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
