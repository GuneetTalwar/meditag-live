# Generated by Django 3.2.7 on 2021-09-15 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_qr', '0004_userprofile_name_in_case_of_emergency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='disabilities',
            new_name='existing_med_conditions',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='ongoing_meds',
            new_name='ongoing_medication',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='spl_med_conditions',
            new_name='others',
        ),
    ]
