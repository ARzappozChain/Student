# Generated by Django 4.2.11 on 2024-04-18 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0005_homeourservicesec_remove_homeourservice_service_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeourservice',
            name='ServicePlayImage',
        ),
    ]
