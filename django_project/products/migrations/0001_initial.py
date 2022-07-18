# Generated by Django 4.0.6 on 2022-07-17 22:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='xeUlcRm', max_length=10)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='ProductUploads/')),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token', models.TextField(blank=True, max_length=500, null=True)),
                ('automated_control', models.BooleanField(default=True)),
                ('time_between_automated_action', models.TimeField(default=datetime.timedelta(seconds=600))),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]