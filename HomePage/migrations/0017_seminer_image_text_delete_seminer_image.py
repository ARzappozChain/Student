# Generated by Django 4.2.11 on 2024-05-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0016_seminer_image_seminer_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminer_Image_Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seminer_image', models.ImageField(blank=True, default=' ', null=True, upload_to='HomePage/media/')),
                ('seminer_text', models.TextField(blank=True, default=' ', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Seminer_Image',
        ),
    ]
