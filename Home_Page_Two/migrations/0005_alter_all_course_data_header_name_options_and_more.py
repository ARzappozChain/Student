# Generated by Django 4.2.11 on 2024-04-29 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0022_alter_all_category_card_data_options_and_more'),
        ('Home_Page_Two', '0004_alter_course_all_data_right_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='all_course_data_header_name',
            options={'verbose_name': 'All_course_data_header_name', 'verbose_name_plural': 'All_course_data_header_name'},
        ),
        migrations.AlterModelOptions(
            name='course_all_data',
            options={'verbose_name': 'Course_All_Data', 'verbose_name_plural': 'Course_All_Data'},
        ),
        migrations.AlterModelOptions(
            name='course_fee',
            options={'verbose_name': 'Course_Fee', 'verbose_name_plural': 'Course_Fee'},
        ),
        migrations.AlterModelOptions(
            name='course_title',
            options={'verbose_name': 'Course_Title', 'verbose_name_plural': 'Course_Title'},
        ),
        migrations.AlterModelOptions(
            name='learning_topic',
            options={'verbose_name': 'Learning_Topic', 'verbose_name_plural': 'Learning_Topic'},
        ),
        migrations.AlterModelOptions(
            name='project_image',
            options={'verbose_name': 'Project_image', 'verbose_name_plural': 'Project_image'},
        ),
        migrations.AlterModelOptions(
            name='puropse_of_course',
            options={'verbose_name': 'Puropse_of_course', 'verbose_name_plural': 'Puropse_of_course'},
        ),
        migrations.AlterModelOptions(
            name='student_openion',
            options={'verbose_name': 'Student_openion', 'verbose_name_plural': 'Student_openion'},
        ),
        migrations.AlterModelOptions(
            name='student_question',
            options={'verbose_name': 'Student_Question', 'verbose_name_plural': 'Student_Question'},
        ),
        migrations.AlterModelOptions(
            name='teacher_about',
            options={'verbose_name': 'Teacher_About', 'verbose_name_plural': 'Teacher_About'},
        ),
        migrations.CreateModel(
            name='Heading_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_summery_text', models.TextField(blank=True, default=' ', null=True)),
                ('Category_image', models.ImageField(blank=True, default=' ', null=True, upload_to='Home_Page_Two/media/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Deshboard.cattegorymodel')),
            ],
            options={
                'verbose_name': 'Heading_title',
                'verbose_name_plural': 'Heading_title',
            },
        ),
    ]
