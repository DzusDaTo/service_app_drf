# Generated by Django 3.2.16 on 2024-07-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20240702_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
