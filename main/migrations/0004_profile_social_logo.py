# Generated by Django 4.1 on 2023-03-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_home_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
    ]
