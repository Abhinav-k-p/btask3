# Generated by Django 5.0.4 on 2024-04-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electroapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'TV'), ('ML', 'MOBILE'), ('LS', 'GROCERY'), ('MS', 'FURNITURE'), ('PN', 'TOYS'), ('GH', 'FASHION')], max_length=2),
        ),
    ]
