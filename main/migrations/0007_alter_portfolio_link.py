# Generated by Django 4.1 on 2023-04-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_about_email_about_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]