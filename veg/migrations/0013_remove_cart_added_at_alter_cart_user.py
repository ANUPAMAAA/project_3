# Generated by Django 5.1.6 on 2025-04-07 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0012_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='added_at',
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veg.signup'),
        ),
    ]
