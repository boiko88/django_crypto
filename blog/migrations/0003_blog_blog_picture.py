# Generated by Django 5.1.7 on 2025-04-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogreaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_picture',
            field=models.ImageField(default='blogs/default_blog.jpeg', upload_to='blogs/'),
        ),
    ]
