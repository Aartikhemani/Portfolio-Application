# Generated by Django 4.1 on 2022-11-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='certificate'),
        ),
    ]
