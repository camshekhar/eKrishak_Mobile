# Generated by Django 4.0.4 on 2024-12-17 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_crop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]