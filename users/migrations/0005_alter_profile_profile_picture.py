# Generated by Django 5.1.7 on 2025-04-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profiles/default_profile.jpeg', upload_to='profiles/'),
        ),
    ]
