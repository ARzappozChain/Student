# Generated by Django 4.2.11 on 2024-04-30 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Deshboard', '0023_all_category_model_slug'),
        ('Home_Page_Two', '0008_remove_course_title_course_title_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course_Fee',
        ),
        migrations.AddField(
            model_name='all_course_data_header_name',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='course_all_data',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='course_all_data',
            name='choose_Header_Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home_Page_Two.all_course_data_header_name'),
        ),
        migrations.AddField(
            model_name='course_title',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='learning_topic',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='project_image',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='puropse_of_course',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='student_openion',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='student_question',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
        migrations.AddField(
            model_name='teacher_about',
            name='chooes_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Deshboard.all_category_card_data'),
        ),
    ]
