# Generated by Django 4.2.11 on 2024-05-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0013_rename_month_seminer_time_month_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminer_time',
            name='seminer_image',
            field=models.ImageField(blank=True, default=' ', null=True, upload_to='HomePage/media/'),
        ),
    ]