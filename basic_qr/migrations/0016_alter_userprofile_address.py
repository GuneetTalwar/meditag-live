# Generated by Django 3.2.7 on 2021-09-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_qr', '0015_auto_20210923_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, help_text='(Fill in to claim your free stickers)(Enter Pin Code)', null=True),
        ),
    ]
