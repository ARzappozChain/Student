# Generated by Django 4.2.11 on 2024-04-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0017_alter_all_category_second_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_category_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cattegory_top_text', models.TextField(blank=True, default=' ', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='all_category_second',
            name='Cattegory_top_text',
        ),
    ]