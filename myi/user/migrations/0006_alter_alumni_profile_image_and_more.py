# Generated by Django 4.1.5 on 2023-04-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alumni_profile_image_student_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='profile_image',
            field=models.ImageField(default='profile_pics/defalut.jpg', upload_to='profile_pics/alumnis'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(default='profile_pics/defalut.jpg', upload_to='profile_pics/students'),
        ),
    ]
