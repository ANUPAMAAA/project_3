# Generated by Django 5.1.6 on 2025-05-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0021_oder_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='oder_notification',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
