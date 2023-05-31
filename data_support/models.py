from django.db import models

# https://en.wikipedia.org/wiki/Ethnic_groups_in_Indonesia
class Etnik(models.Model):
    nama_etnik = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'etnik'
        verbose_name_plural = 'Etnik'
    
    def __str__(self):
        return '%s' % self.nama_etnik
 
    def clean(self):
        self.nama_etnik = self.nama_etnik.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Etnik, self).save(*args, **kwargs)


class Pendidikan(models.Model):
    nama_pendidikan = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'pendidikan'
        verbose_name_plural = 'Pendidikan'
    
    def __str__(self):
        return '%s' % self.nama_pendidikan
 
    def clean(self):
        self.nama_pendidikan = self.nama_pendidikan.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Pendidikan, self).save(*args, **kwargs)


class Profesi(models.Model):
    nama_profesi = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'profesi'
        verbose_name_plural = 'Profesi'
    
    def __str__(self):
        return '%s' % self.nama_profesi
 
    def clean(self):
        self.nama_profesi = self.nama_profesi.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Profesi, self).save(*args, **kwargs)


class Nob(models.Model):
    nama_nob = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'nob'
        verbose_name_plural = 'Nature Of Business'
    
    def __str__(self):
        return '%s' % self.nama_nob

    def clean(self):
        self.nama_nob = self.nama_nob.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Nob, self).save(*args, **kwargs)


class Pelayanan(models.Model):
    nama_pelayanan = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'pelayanan'
        verbose_name_plural = 'Minat Pelayanan'
    
    def __str__(self):
        return '%s' % self.nama_pelayanan

    def clean(self):
        self.nama_pelayanan = self.nama_pelayanan.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Pelayanan, self).save(*args, **kwargs)


class Wilayah(models.Model):
    nama_wilayah = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'wilayah'
        verbose_name_plural = 'Wilayah'

    def __str__(self):
        return '%s' % self.nama_wilayah

    def clean(self):
        self.nama_wilayah = self.nama_wilayah.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Wilayah, self).save(*args, **kwargs)
        

