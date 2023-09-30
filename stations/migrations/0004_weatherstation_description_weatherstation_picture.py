# Generated by Django 4.2 on 2023-07-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_mushroomspot_description_mushroomspot_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherstation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
