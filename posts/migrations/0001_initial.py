# Generated by Django 4.1.7 on 2023-03-14 17:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_rename_crated_at_profile_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('content', models.TextField(max_length=500)),
                ('image', models.FileField(upload_to='posts', verbose_name='Thumbnail')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('isPublish', models.BooleanField(default=False, verbose_name='Yayınla')),
                ('dislike', models.ManyToManyField(related_name='dislikes', to='user.profile', verbose_name='Beğenmeyenler')),
                ('like', models.ManyToManyField(related_name='likes', to='user.profile', verbose_name='Beğenenler')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owners', to='user.profile', verbose_name='Yazar')),
            ],
        ),
    ]
