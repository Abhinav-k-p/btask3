# Generated by Django 5.0.3 on 2024-03-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=100)),
                ('directorname', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
