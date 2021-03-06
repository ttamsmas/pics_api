# Generated by Django 3.0 on 2020-12-22 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201221_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Pic')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pic',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='likes', through='api.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='pics',
            field=models.ManyToManyField(blank=True, related_name='likes', through='api.Like', to='api.Pic'),
        ),
    ]
