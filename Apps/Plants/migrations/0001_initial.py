# Generated by Django 4.0.1 on 2022-02-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='PlantsUploads/')),
                ('is_supported', models.BooleanField(default=False)),
            ],
        ),
    ]
