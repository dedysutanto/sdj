from datetime import date
from django.db import models
from django.urls import reverse
from data_support.models import *
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

JENIS_KELAMIN = [
    ('NN', 'None'),
    ('LAKILAKI', 'Laki-Laki'),
    ('PEREMPUAN', 'Perempuan'),
]

# Golongan Darah
GOLONGAN_DARAH = [
    ('NN', 'None'),
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O'),
]

GOLONGAN_DARAH_RHESUS = [
    ('NN', 'None'),
    ('RP', 'Rhesus Positif'),
    ('RN', 'Rhesus Negatif'),
]

STATUS_PERNIKAHAN = [
    ('MENIKAH', 'Menikah'),
    ('BELUM_MENIKAH', 'Belum Menikah'),
    ('DUDA_JANDA', 'Duda/Janda'),
]

# Status Keanggotaan
STATUS_KEANGGOTAAN = [
    ('ANGGOTA_SIDI', 'Anggota Sidi'),
    ('ANGGOTA_ANAK', 'Anggota Anak'),
    ('SIMPATISAN', 'Simpatisan'),
    ('NON_AKTIF', 'Non Aktif'),
]

# Status Keanggotaan
STATUS_KEHIDUPAN = [
    ('HIDUP', 'Hidup'),
    ('ALMARHUM', 'Almarhum'),
]

LOKASI_PEMAKAMAN = [
    ('NON_SARIMULIA', 'Bukan Sari Mulia'),
    ('YES_SARIMULIA', 'Sari Mulia'),
]

ALASAN_NON_AKTIF = [
    ('TIDAK_ADA', 'Tidak Ada Alasan'),
    ('ALMARHUM', 'Almarhum'),
    ('ATESTASI_KELUAR', 'Atestasi Keluar'),
    ('PINDAH_KOTA', 'Pindah Keluar Kota'),
    ('PINDAH_AGAMA', 'Pindah Agama'),
]


# Model Keluarga
class Keluarga(models.Model):
    nama_kepala_keluarga = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'keluarga'
        verbose_name_plural = 'Keluarga'

    def __str__(self):
        return "%s" % (self.nama_kepala_keluarga)

    def clean(self):
        s = " ".join(self.nama_kepala_keluarga.split())
        self.nama_kepala_keluarga = s.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Keluarga, self).save(*args, **kwargs)


# Model Anggota
class Anggota(models.Model):
    nomor_anggota = models.CharField(max_length=10, unique=True)
    status_anggota = models.CharField(max_length=30, choices=STATUS_KEANGGOTAAN, default='ANGGOTA_SIDI')
    kepala_keluarga = models.BooleanField(default=False)
    nama_kepala_keluarga = models.ForeignKey(Keluarga, on_delete=models.PROTECT, null=True, blank=True)
    nama_anggota = models.CharField(max_length=100)
    tanggal_lahir = models.DateField(null=True, blank=True)
    tempat_lahir = models.CharField(max_length=50, blank=True)
    alamat = models.CharField(max_length=200, blank=True)
    kelurahan = models.CharField(max_length=50, blank=True)
    kecamatan = models.CharField(max_length=50, blank=True)
    kota_kabupaten = models.CharField(max_length=50, blank=True)
    kode_pos = models.CharField(max_length=10, blank=True)
    wilayah = models.ForeignKey(Wilayah, on_delete=models.PROTECT, null=True, blank=True)
    jenis_kelamin = models.CharField(max_length=15, choices=JENIS_KELAMIN, default='NN')
    nomor_telp = models.CharField(max_length=30, blank=True)
    nomor_hp = models.CharField(max_length=30, blank=True)
    nomor_darurat = models.CharField(max_length=50, blank=True)
    hubungan_darurat = models.CharField(max_length=100, blank=True)
    alamat_email = models.EmailField(blank=True)
    status_pernikahan = models.CharField(max_length=15, choices=STATUS_PERNIKAHAN, default='MENIKAH')
    status_kehidupan = models.CharField(max_length=15, choices=STATUS_KEHIDUPAN, default='HIDUP')
    lokasi_pemakaman = models.CharField(max_length=15, choices=LOKASI_PEMAKAMAN, default='NON_SARIMULIA')
    lokasi_sari_mulia = models.CharField(max_length=50, blank=True)
    golongan_darah = models.CharField(max_length=2, choices=GOLONGAN_DARAH, default='NN')
    golongan_darah_rhesus = models.CharField(max_length=2, choices=GOLONGAN_DARAH_RHESUS, default='NN')
    etnik = models.ForeignKey(Etnik, on_delete=models.PROTECT, null=True, blank=True)
    pendidikan = models.ForeignKey(Pendidikan, on_delete=models.PROTECT, null=True, blank=True)
    profesi = models.ForeignKey(Profesi, on_delete=models.PROTECT, null=True, blank=True)
    nob = models.ForeignKey(Nob, on_delete=models.PROTECT, null=True, blank=True )
    tanggal_nikah = models.DateField(null=True, blank=True)
    gereja_nikah = models.CharField(max_length=100, blank=True)
    pendeta_nikah = models.CharField(max_length=100, blank=True)
    tanggal_baptis = models.DateField(null=True, blank=True)
    gereja_baptis = models.CharField(max_length=100, blank=True)
    pendeta_baptis = models.CharField(max_length=100, blank=True)
    tanggal_sidi = models.DateField(null=True, blank=True)
    gereja_sidi = models.CharField(max_length=100, blank=True)
    pendeta_sidi = models.CharField(max_length=100, blank=True)
    minat_pelayanan = models.ForeignKey(Pelayanan, on_delete=models.PROTECT, null=True, blank=True)
    foto_anggota = models.ImageField(upload_to='images/', blank=True)
    nomor_kartu_parkir = models.CharField(max_length=50, blank=True)
    alasan_non_aktif = models.CharField(max_length=50, choices=ALASAN_NON_AKTIF, default='TIDAK_ADA')
    keterangan = models.TextField(blank=True)
    riwayat_pelayanan = models.TextField(blank=True)
    gereja_asal = models.CharField(max_length=50, blank=True)
    verifikasi = models.BooleanField(default=False)
    alamat_kk = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'anggota'
        verbose_name_plural = 'Anggota'

    def __str__(self):
        return "%s %s" % (self.nomor_anggota, self.nama_anggota)

    def clean(self):
        #s = " ".join(self.nama_anggota.split())
        #self.nama_anggota = s.upper()

        if self.status_kehidupan == 'ALMARHUM':
            self.status_anggota = 'NON_AKTIF'
            self.alasan_non_aktif = 'ALMARHUM'

        if self.alasan_non_aktif == 'ALMARHUM':
            self.status_kehidupan = 'ALMARHUM'
            self.status_anggota = 'NON_AKTIF'

        '''
        if self.nomor_anggota is not None:
            try:
                Anggota.objects.exclude(tanggal_lahir=self.tanggal_lahir).get(
                    nomor_anggota__icontains=self.nomor_anggota)
                is_nomor = False
            except ObjectDoesNotExist:
                try:
                    Anggota.objects.get(
                        nomor_anggota__icontains=self.nomor_anggota, tanggal_lahir=self.tanggal_lahir)
                    is_nomor = True
                except ObjectDoesNotExist:
                    is_nomor = False

            except MultipleObjectsReturned:
                is_nomor = False


            if is_nomor:
                #self.nomor_anggota = self.nomor_anggota.upper()
                #nomor_anggota_part = ("{:07d}".format(int(self.nomor_anggota[1:])))
                nomor_anggota_part = self.nomor_anggota[1:]
            else:
                #digit_nomor = int(self.nomor_anggota[1:]) + 8000
                #new_nomor = self.nomor_anggota[:1] + "{:07d}".format(digit_nomor)
                #self.nomor_anggota = new_nomor
                START_FROM = 6000
                total_anggota = Anggota.objects.count() + START_FROM + 1
                nomor_anggota_part = ("{:07d}".format(total_anggota))
        else:
            START_FROM = 6000
            total_anggota = Anggota.objects.count() + START_FROM + 1
            nomor_anggota_part = ("{:07d}".format(total_anggota))

        if self.status_anggota == 'ANGGOTA_SIDI':
            nomor_anggota_ok = 'D' + nomor_anggota_part
        elif self.status_anggota == 'ANGGOTA_ANAK':
            nomor_anggota_ok = 'A' + nomor_anggota_part
        elif self.status_anggota == 'SIMPATISAN':
            nomor_anggota_ok = 'S' + nomor_anggota_part
        elif self.status_anggota == 'NON_AKTIF':
            nomor_anggota_ok = 'N' + nomor_anggota_part

        self.nomor_anggota = nomor_anggota_ok
        '''

        self.nama_anggota = self.nama_anggota.upper()
        self.tempat_lahir = self.tempat_lahir.upper()
        self.alamat = self.alamat.upper()
        self.kelurahan = self.kelurahan.upper()
        self.kecamatan = self.kecamatan.upper()
        self.kota_kabupaten = self.kota_kabupaten.upper()
        self.gereja_sidi = self.gereja_sidi.upper()
        self.gereja_baptis = self.gereja_baptis.upper()
        self.gereja_nikah = self.gereja_nikah.upper()
        self.pendeta_sidi = self.pendeta_sidi.upper()
        self.pendeta_baptis = self.pendeta_baptis.upper()
        self.pendeta_nikah = self.pendeta_nikah.upper()
        self.gereja_asal = self.gereja_asal.upper()
        self.alamat_email = self.alamat_email.lower()

        #self.nama_kepala_keluarga = self.nama_anggota + ' #' + self.nomor_anggota[1:]

        if self.kepala_keluarga == True:
            if self.nama_kepala_keluarga == None:
                nama_kk_ok = self.nama_anggota + ' #' + self.nomor_anggota[1:]
                try:
                    kk = Keluarga.objects.get(nama_kepala_keluarga__icontains=nama_kk_ok)
                except ObjectDoesNotExist:
                    kk = Keluarga.objects.create(
                        nama_kepala_keluarga = nama_kk_ok
                    )
                self.nama_kepala_keluarga = kk
            else:
                nama_kk_ok = self.nama_anggota + ' #' + self.nomor_anggota
                try:
                    kk = Keluarga.objects.get(nama_kepala_keluarga=self.nama_kepala_keluarga)
                    kk.nama_kepala_keluarga = nama_kk_ok
                    kk.save()
                except ObjectDoesNotExist:
                    pass

        '''
            else:
                try:
                    kk = Keluarga.objects.get(nama_kepala_keluarga__icontains=self.nama_kepala_keluarga)
                except ObjectDoesNotExist:
                    kk = Keluarga.objects.create(
                        nama_kepala_keluarga = self.nama_kepala_keluarga
                    )
        '''

        if self.nomor_anggota:
            if self.id:
                try:
                    Anggota.objects.exclude(id=self.id).get(nomor_anggota=self.nomor_anggota)
                    raise ValidationError({'nomor_anggota': 'Nomor Anggota sudah digunakan'})
                except ObjectDoesNotExist:
                    pass
            else:
                try:
                    Anggota.objects.get(nomor_anggota=self.nomor_anggota)
                    raise ValidationError({'nomor_anggota': 'Nomor Anggota sudah digunakan'})
                except ObjectDoesNotExist:
                    pass

        #print("%s %s" % (self.nama_kepala_keluarga, self.nama_anggota))


    def save(self, *args, **kwargs):
        self.clean()
        self.validate_unique()
        #self.full_clean()
        return super(Anggota, self).save(*args, **kwargs)


    def calculate_age(self):
        today = date.today()
        try:
            age = (today.year - self.tanggal_lahir.year) - ((today.month, today.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day))
        except:
            age = 0
        return '%d' % age
    calculate_age.short_description = 'Usia'

    def change_url(self):
        return reverse('admin:data_anggota_change', args=(self.id,))


