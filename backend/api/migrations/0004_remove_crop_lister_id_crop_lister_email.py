# Generated by Django 4.0.4 on 2024-12-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_crop_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='lister_id',
        ),
        migrations.AddField(
            model_name='crop',
            name='lister_email',
            field=models.CharField(default='admin@gmail.com', max_length=200),
        ),
    ]