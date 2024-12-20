# Generated by Django 4.0.4 on 2024-12-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_crop_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farmer_email', models.CharField(max_length=100)),
                ('vendor_email', models.CharField(max_length=100)),
                ('crop', models.JSONField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('aproved', models.BooleanField(default=False)),
                ('subTotal', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('paymentMode', models.CharField(max_length=20)),
                ('paymentStatus', models.CharField(choices=[('pending', 'pending'), ('success', 'success'), ('failed', 'failed'), ('Refund Initiated', 'Refund Initiated'), ('Refunded', 'Refunded')], default='pending', max_length=100)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('transit_status', models.CharField(choices=[('Ordered', 'Ordered'), ('Shipped', 'Shipped'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Ordered', max_length=20)),
            ],
        ),
    ]