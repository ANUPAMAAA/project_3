# Generated by Django 5.1.6 on 2025-04-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0013_remove_cart_added_at_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_tax',
            field=models.IntegerField(null=True),
        ),
    ]
