# Generated by Django 4.1.7 on 2023-04-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_follow_alter_profile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='profile/default.jpeg', null=True, upload_to='profiles/', verbose_name='Profil Resmi'),
        ),
    ]
