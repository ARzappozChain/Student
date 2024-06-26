# Generated by Django 4.2.11 on 2024-04-19 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0018_all_category_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Cattegory_Wise_Show_Card_Detial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cattegoryWiseImage', models.ImageField(blank=True, null=True, upload_to='Deshboard/media/')),
                ('Course_name', models.CharField(blank=True, max_length=150, null=True)),
                ('student_reviews', models.CharField(blank=True, default='  ', max_length=150, null=True)),
                ('Course_fee', models.PositiveIntegerField()),
                ('choicecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Deshboard.homecattegorywiseshowsec')),
            ],
        ),
        migrations.DeleteModel(
            name='HomeCattegoryWiseShow',
        ),
    ]
