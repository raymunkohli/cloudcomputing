from django.db import models

# Create your models here.


class Album(models.Model):
    idalbum = models.IntegerField(db_column='idAlbum', primary_key=True)  # Field name made lowercase.
    album_name = models.CharField(max_length=45, blank=True, null=True)
    artist_idartist = models.ForeignKey('Artist', models.DO_NOTHING, db_column='artist_idArtist', blank=True, null=True)  # Field name made lowercase.
    band_idband = models.ForeignKey('Band', models.DO_NOTHING, db_column='band_idBand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'album'


class Artist(models.Model):
    idartist = models.AutoField(db_column='idArtist', primary_key=True)  # Field name made lowercase.
    artist_name = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    band_idband = models.ForeignKey('Band', models.DO_NOTHING, db_column='band_idBand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artist'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Band(models.Model):
    idband = models.IntegerField(db_column='idBand', primary_key=True)  # Field name made lowercase.
    band_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'band'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Song(models.Model):
    idsong = models.AutoField(db_column='idSong', primary_key=True)  # Field name made lowercase.
    song_name = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=45, blank=True, null=True)
    album_idalbum = models.ForeignKey(Album, models.DO_NOTHING, db_column='album_idAlbum', null=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=45, blank=True, null=True)
    userid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'song'