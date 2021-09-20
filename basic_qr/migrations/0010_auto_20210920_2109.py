# Generated by Django 3.2.7 on 2021-09-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_qr', '0009_alter_deliversticker_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliversticker',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deliversticker',
            name='complete_address',
            field=models.TextField(help_text='Do not forget to add the pin code', max_length=200, null=True),
        ),
    ]