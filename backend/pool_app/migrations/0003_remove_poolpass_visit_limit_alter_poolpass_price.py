# Generated by Django 5.0.2 on 2024-03-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool_app', '0002_poolpass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poolpass',
            name='visit_limit',
        ),
        migrations.AlterField(
            model_name='poolpass',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Стоимость'),
        ),
    ]
