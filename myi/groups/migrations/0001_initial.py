# Generated by Django 4.1.5 on 2023-04-28 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0007_alter_alumni_profile_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='posts/images')),
                ('video', models.FileField(null=True, upload_to='posts/videos')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_admin', to='user.alumni')),
                ('alumnis', models.ManyToManyField(to='user.alumni')),
                ('posts', models.ManyToManyField(to='groups.post')),
            ],
        ),
    ]
