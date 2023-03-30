# Generated by Django 4.1.7 on 2023-03-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='takip', to='user.profile', verbose_name='Takip'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='takipci', to='user.profile', verbose_name='Takipçiler'),
        ),
    ]
