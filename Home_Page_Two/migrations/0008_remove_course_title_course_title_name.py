# Generated by Django 4.2.11 on 2024-04-29 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page_Two', '0007_category_wise_card_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_title',
            name='Course_Title_Name',
        ),
    ]
