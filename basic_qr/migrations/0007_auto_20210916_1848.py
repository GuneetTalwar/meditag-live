# Generated by Django 3.2.7 on 2021-09-16 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_qr', '0006_alter_userprofile_blood_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name_in_case_of_emergency',
            new_name='contact_name_in_case_of_emergency',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='emergency_no',
            new_name='contact_number_in_case_of_emergency',
        ),
    ]