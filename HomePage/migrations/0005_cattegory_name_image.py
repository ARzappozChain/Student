# Generated by Django 4.2.11 on 2024-04-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0004_header_li'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cattegory_Name_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cattegory_name', models.CharField(blank=True, max_length=150, null=True)),
                ('cattegory_image', models.ImageField(blank=True, null=True, upload_to='HomePage/media/')),
            ],
        ),
    ]