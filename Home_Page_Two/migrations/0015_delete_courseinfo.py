# Generated by Django 4.2.11 on 2024-05-04 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page_Two', '0014_rename_chooes_category_course_title_chooes_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseInfo',
        ),
    ]