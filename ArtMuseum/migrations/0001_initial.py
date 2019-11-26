# Generated by Django 2.2.7 on 2019-11-26 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=200)),
                ('movement', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('birth_year', models.IntegerField(default=0)),
                ('death_year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('medium', models.CharField(max_length=200)),
                ('picture_url', models.CharField(max_length=500)),
                ('year', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArtMuseum.Artist')),
            ],
        ),
    ]
