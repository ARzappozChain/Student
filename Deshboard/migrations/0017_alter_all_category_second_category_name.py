# Generated by Django 4.2.11 on 2024-04-19 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0016_all_category_second_cattegory_top_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_category_second',
            name='Category_Name',
            field=models.ForeignKey(blank=True, default=' ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_name', to='Deshboard.all_category_model'),
        ),
    ]