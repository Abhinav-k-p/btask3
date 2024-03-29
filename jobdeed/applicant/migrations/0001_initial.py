# Generated by Django 5.0.3 on 2024-03-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resume/')),
            ],
        ),
        migrations.CreateModel(
            name='Job_apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('experience', models.PositiveIntegerField()),
                ('phonenumber', models.PositiveIntegerField()),
                ('coverletter', models.TextField(max_length=100)),
                ('file', models.FileField(upload_to='recruiter/resume/')),
            ],
        ),
    ]
