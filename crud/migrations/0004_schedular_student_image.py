# Generated by Django 3.2 on 2022-01-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20220105_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedular',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Student Image'),
        ),
    ]
