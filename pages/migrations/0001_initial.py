# Generated by Django 3.2 on 2021-04-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diety_image', models.CharField(max_length=200)),
                ('diety_name', models.CharField(max_length=200)),
                ('file_name', models.CharField(max_length=200)),
                ('file_size', models.CharField(max_length=200)),
            ],
        ),
    ]
