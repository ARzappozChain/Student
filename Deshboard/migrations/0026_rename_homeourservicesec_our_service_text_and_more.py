# Generated by Django 4.2.11 on 2024-05-03 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0025_delete_cattegorymodel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeOurServicesec',
            new_name='Our_Service_Text',
        ),
        migrations.DeleteModel(
            name='HomeSeminerModel',
        ),
    ]