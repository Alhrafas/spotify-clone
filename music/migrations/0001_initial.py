# Generated by Django 4.2.2 on 2024-02-02 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('released_date', models.DateField()),
                ('cover_img', models.ImageField(upload_to='album_covers/')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('bio', models.TextField(blank=True, null=True)),
                ('artist_img', models.ImageField(upload_to='artists_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('song_img', models.ImageField(upload_to='songs_images/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
    ]
