# Generated by Django 4.2.11 on 2024-04-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0009_alter_homeourservice_sercicebannerimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeseminermodel',
            name='day',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='homeseminermodel',
            name='month',
            field=models.CharField(blank=True, default='0', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='homeseminermodel',
            name='seminer_image',
            field=models.ImageField(blank=True, default='0', null=True, upload_to='Deshboard/media/'),
        ),
        migrations.AlterField(
            model_name='homeseminermodel',
            name='year',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
