# Generated by Django 3.2.7 on 2021-09-24 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_qr', '0017_userprofile_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['created_at']},
        ),
    ]
