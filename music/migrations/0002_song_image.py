# Generated by Django 4.2.2 on 2024-02-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, upload_to='song_images/'),
        ),
    ]