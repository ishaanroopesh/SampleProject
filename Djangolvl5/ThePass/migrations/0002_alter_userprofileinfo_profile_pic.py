# Generated by Django 4.2.6 on 2023-10-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThePass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='ThePass/profile_pics'),
        ),
    ]