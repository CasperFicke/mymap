# Generated by Django 4.2 on 2023-10-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_delete_mushroomspot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherstation',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='stations/'),
        ),
    ]
