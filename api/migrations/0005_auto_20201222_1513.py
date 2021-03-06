# Generated by Django 3.0 on 2020-12-22 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201222_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='like',
            name='pic_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pics',
        ),
        migrations.AddField(
            model_name='like',
            name='pic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pics', to='api.Pic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pic',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='pics', through='api.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Mango',
        ),
    ]
