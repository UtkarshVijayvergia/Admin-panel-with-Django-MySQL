# Generated by Django 3.2 on 2022-01-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_schedular_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedular',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/', verbose_name='Student Image'),
        ),
    ]
