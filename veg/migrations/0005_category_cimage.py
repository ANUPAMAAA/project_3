# Generated by Django 5.1.6 on 2025-03-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0004_brand_bimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cimage',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
