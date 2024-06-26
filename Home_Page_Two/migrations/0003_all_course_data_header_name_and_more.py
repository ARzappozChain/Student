# Generated by Django 4.2.11 on 2024-04-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page_Two', '0002_course_all_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_course_data_header_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header_Name', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course_all_data',
            name='Info_Title',
        ),
        migrations.AlterField(
            model_name='course_all_data',
            name='Left_text',
            field=models.CharField(blank=True, default=' ', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='course_all_data',
            name='Right_text',
            field=models.TextField(blank=True, default=' ', max_length=300, null=True),
        ),
    ]
