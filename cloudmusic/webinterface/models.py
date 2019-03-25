from django.db import models

# Create your models here.

class Album(models.Model):
    idalbum = models.IntegerField(db_column='idAlbum', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    releasedate = models.CharField(max_length=45, blank=True, null=True)
    cover = models.TextField(blank=True, null=True)
    artist_idartist = models.ForeignKey('Artist', models.DO_NOTHING, db_column='Artist_idArtist', blank=True, null=True)  # Field name made lowercase.
    band_idband = models.ForeignKey('Band', models.DO_NOTHING, db_column='band_idBand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Album'


class Artist(models.Model):
    idartist = models.AutoField(db_column='idArtist', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    band_idband = models.ForeignKey('Band', models.DO_NOTHING, db_column='band_idBand', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Artist'


class Song(models.Model):
    idsong = models.AutoField(db_column='idSong', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=45, blank=True, null=True)
    album_idalbum = models.ForeignKey(Album, models.DO_NOTHING, db_column='Album_idAlbum')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Song'


class Band(models.Model):
    idband = models.IntegerField(db_column='idBand', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    startdate = models.CharField(max_length=45, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'band'