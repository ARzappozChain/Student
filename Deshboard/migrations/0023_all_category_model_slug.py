# Generated by Django 4.2.11 on 2024-04-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0022_alter_all_category_card_data_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_category_model',
            name='slug',
            field=models.SlugField(blank=True, default=' ', max_length=150, null=True, unique=True),
        ),
    ]