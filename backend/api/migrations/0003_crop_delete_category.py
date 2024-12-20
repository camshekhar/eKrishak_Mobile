# Generated by Django 4.0.4 on 2024-12-16 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_cart_cust_remove_feedback_cust_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(default='no_img.jpg', upload_to='images/crops')),
                ('price', models.CharField(default='0', max_length=100)),
                ('quantity', models.IntegerField(default='0')),
                ('lister_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]