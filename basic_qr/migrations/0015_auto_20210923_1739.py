# Generated by Django 3.2.7 on 2021-09-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_qr', '0014_auto_20210921_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, help_text='(Fill in to claim your free stickers)', null=True),
        ),
    ]
