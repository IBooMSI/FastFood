# Generated by Django 4.0.4 on 2022-06-03 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_order_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='labs',
        ),
    ]
