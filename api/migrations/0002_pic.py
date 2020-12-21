# Generated by Django 3.0 on 2020-12-20 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('imgLink', models.CharField(max_length=100)),
                ('tag', models.CharField(choices=[('people', 'people'), ('pets', 'pets'), ('nature', 'nature'), ('action', 'action'), ('lifestyle', 'lifestyle')], default='people', max_length=9)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]