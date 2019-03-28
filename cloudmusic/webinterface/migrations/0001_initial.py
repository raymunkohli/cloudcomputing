# Generated by Django 2.1.7 on 2019-03-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('idalbum', models.IntegerField(db_column='idAlbum', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('releasedate', models.CharField(blank=True, max_length=45, null=True)),
                ('cover', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Album',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('idartist', models.AutoField(db_column='idArtist', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('picture', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Artist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('idband', models.IntegerField(db_column='idBand', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('startdate', models.CharField(blank=True, max_length=45, null=True)),
                ('logo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'band',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('idsong', models.AutoField(db_column='idSong', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Song',
                'managed': False,
            },
        ),
    ]