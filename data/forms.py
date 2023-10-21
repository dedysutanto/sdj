from data.models import *
from data_support.models import *
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class AnggotaForm(forms.ModelForm):

    #is_alamat_kk = forms.BooleanField(label=_('Alamat sama dengan Kepala Keluarga'))

    class Meta:
        model = Anggota
        fields = '__all__'

        labels = {
            'alamat_kk': _('Alamat sama dengan Kepala Keluarga'),
            'nama_anggota': _('Nama'),
            'kepala_keluarga': _('Kepala Keluarga atau Single'),
            'nama_kepala_keluarga': _('Nama Kepala Keluarga'),
            'jenis_kelamin': _('Jenis Kelamin'),
            'status_pernikahan': _('Status Pernikahan'),
            'kota_kabupaten': _('Kota'),
            'gereja_asal': _('Gereja Asal'),
            'nomor_anggota': _('Nomor Anggota'),
            'status_anggota': _('Status Anggota'),
            'verifikasi': _('Terverifikasi'),
            'alasan_non_aktif': _('Alasan Non Aktif'),
            'nomor_telp': _('Nomor Telpon'),
            'nomor_hp': _('Nomor HP'),
            'nomor_darurat': _('Kontak Darurat'),
            'alamat_email': _('Email'),
            'nob': _('Nature Of Business'),
            'golongan_darah': _('Golongan Darah'),
            'golongan_darah_rhesus': _('Golongan Darah Rhesus'),
            'status_kehidupan': _('Status Kehidupan'),
            'lokasi_pemakaman': _('Lokasi Pemakaman'),
            'lokasi_sari_mulia': _('Lokasi di Sari Mulia'),
            'tanggal_baptis': _('Tanggal Baptis'),
            'gereja_baptis': _('Baptis di Gereja'),
            'pendeta_baptis': _('Dibaptis oleh Pendeta'),
            'tanggal_sidi': _('Tanggal Sidi'),
            'gereja_sidi': _('Sidi di Gereja'),
            'pendeta_sidi': _('Disidi oleh Pendeta'),
            'tanggal_nikah': _('Tanggal Nikah'),
            'gereja_nikah': _('Nikah di Gereja'),
            'pendeta_nikah': _('Diberkati oleh Pendeta'),
            'minat_pelayanan': _('Minat Pelayanan'),
            'riwayat_pelayanan': _('Riwayat Pelayanan'),
            'nomor_kartu_parkir': _('Nomor Kartu Parkir'),

        }
        help_texts = {
            'kepala_keluarga': _('Check kalau kepala keluarga atau single'),
            'nama_kepala_keluarga': _('Jika bukan kepala keluarga atau single, ini harus diisi'),
            'verifikasi': _('Jika data sudah di verifikasi, check ini'),
            'lokasi_pemakaman': _('Apakah di pemakaman Sari Mulia atau bukan?'),
            'lokasi_sari_mulia': _('Nomor kavling di Sari Mulia'),
            'nama_anggota': _('Tidak boleh kosong'),
            'status_pernikahan': _('Tidak boleh kosong'),
            'jenis_kelamin': _('Tidak boleh kosong'),
            'tanggal_lahir': _('Tidak boleh kosong'),
            'alamat': _('Tidak boleh kosong'),

        }
        error_messages = {
            'nama_anggota': {
                'max_length': _("Nama kepanjangan"),
                'required': _('Nama tidak boleh kosong'),
            },
            'alamat': {
                'required': _('Alamat tidak boleh kosong'),
            }
        }

    def __init__(self, *args, **kwargs):
        super(AnggotaForm, self).__init__(*args, **kwargs)
        self.fields['nama_kepala_keluarga'].required = False
        self.fields['nomor_anggota'].required = True
        #self.fields['nomor_anggota'].widget.attrs['readonly'] = True
        self.fields['nama_anggota'].requied = True
        self.fields['status_pernikahan'].required = True
        self.fields['jenis_kelamin'].required = True
        self.fields['status_anggota'].required = False
        self.fields['tanggal_lahir'].required = True
        #self.fields['alamat'].required = True
        self.fields['alamat'].required = False
        self.fields['golongan_darah'].required = False
        self.fields['golongan_darah_rhesus'].required = False
        self.fields['status_kehidupan'].required = False
        self.fields['lokasi_pemakaman'].required = False
        self.fields['etnik'].required = False

        self.fields['verifikasi'].initial = False

    def clean(self):
        form_data = self.cleaned_data

        field_kepala_keluarga = form_data['kepala_keluarga']
        #field_nomor_anggota = form_data['nomor_anggota']
        field_nama_kepala_keluarga = form_data['nama_kepala_keluarga']
        field_status_anggota = form_data['status_anggota']
        field_verifikasi = form_data['verifikasi']
        field_alamat_kk = form_data['alamat_kk']
        field_nama_anggota = form_data['nama_anggota']

        ''' Try to get nomor_anggota '''
        '''
        try:
            field_nomor_anggota = form_data['nomor_anggota']
        except:
            raise ValidationError({'nomor_anggota': 'Check Nomor Anggota. Tidak boleh kosong!'})
        '''

        ''' Try to get nama_anggota '''
        '''
        try:
            field_nama_anggota = form_data['nama_anggota']
        except:
            raise ValidationError({'nama_anggota': 'Check Nama Anggota. Tidak boleh kosong!'})
        '''

        '''
        if Anggota.objects.filter(nomor_anggota=field_nomor_anggota).exists():
            raise ValidationError({'nomor_anggota': 'Nomor Anggota sudah digunakan. Nomor Anggota harus unik!'})
        '''
        ''' Verifikasi nomor anggota '''
        '''
        try:
            ang = Anggota.objects.get(nomor_anggota=field_nomor_anggota)
            raise ValidationError({'nomor_anggota': 'Nomor Anggota sudah digunakan. Nomor Anggota harus unik!'})

        except ObjectDoesNotExist:
            pass
        '''

        '''
        if field_nomor_anggota[1:] != "":
            print("Here ", field_nomor_anggota)
            nomor_anggota_part = ("{:07d}".format(int(field_nomor_anggota[1:])))
            #print("No Angg: %s" % nomor_anggota_part)
        else:
            START_FROM = 6000
            total_anggota = Anggota.objects.count() + START_FROM + 1
            nomor_anggota_part = ("{:07d}".format(total_anggota))
            print("Herepart ", nomor_anggota_part)

        if field_status_anggota == 'ANGGOTA_SIDI':
            nomor_anggota_ok = 'D' + nomor_anggota_part
        elif field_status_anggota == 'ANGGOTA_ANAK':
            nomor_anggota_ok = 'A' + nomor_anggota_part
        elif field_status_anggota == 'SIMPATISAN':
            nomor_anggota_ok = 'S' + nomor_anggota_part
        elif field_status_anggota == 'NON_AKTIF':
            nomor_anggota_ok = 'N' + nomor_anggota_part

        self.cleaned_data['nomor_anggota'] = nomor_anggota_ok
        '''

        #if form_data['nama_anggota'] == '':
            #raise ValidationError({'nama_anggota': 'Nama tidak boleh kosong'})
        if form_data['jenis_kelamin'] == 'NN':
            raise ValidationError({'jenis_kelamin': 'Jenis Kelamin tidak boleh kosong'})
        #if form_data['alamat'] == '':
        #    raise ValidationError({'alamat': 'Alamat tidak boleh kosong'})


        ''' Verifikasi Data '''

        if field_verifikasi == True:
            #print("Tanggal Lahir: %s" % form_data['tanggal_lahir'])

            #if form_data['tanggal_lahir'] == None:
            #    raise ValidationError({'tanggal_lahir': 'Tanggal Lahir tidak boleh kosong'})
            if form_data['wilayah'] == None:
                raise ValidationError({'wilayah': 'Wilayah tidak boleh kosong'})
            #if form_data['etnik'] == None:
            #    raise ValidationError({'etnik': 'Etnik tidak boleh kosong'})
            #if form_data['pendidikan'] == None:
            #    raise ValidationError({'pendidikan': 'Pendidikan tidak boleh kosong'})
            #if form_data['profesi'] == None:
            #    raise ValidationError({'profesi': 'Profesi tidak boleh kosong'})
            #if form_data['golongan_darah'] == 'NN':
            #    raise ValidationError({'golongan_darah': 'Golongan Darah tidak boleh kosong'})
            #if form_data['golongan_darah_rhesus'] == 'NN':
            #    raise ValidationError({'golongan_darah_rhesus': 'Golongan Darah Rhesus tidak boleh kosong. Mayoritas Rhesus Positif.'})

        ''' Verifikasi nama_kepala_keluarga '''
        if field_kepala_keluarga == True:
            if field_nama_kepala_keluarga == None:
                try:
                    kk = Keluarga.objects.get(nama_kepala_keluarga__icontains=field_nama_anggota.upper())
                except ObjectDoesNotExist:
                    kk = Keluarga.objects.create(
                        nama_kepala_keluarga = field_nama_anggota
                    )
                self.cleaned_data['nama_kepala_keluarga'] = kk

                if form_data['alamat'] == '':
                    raise ValidationError({'alamat': 'Alamat tidak boleh kosong'})

        else:
            if field_nama_kepala_keluarga == None:
                raise ValidationError("Nama Kepala Keluarga tidak boleh kosong!")

            if field_alamat_kk:
                try:
                    alamat_kepala_keluarga = Anggota.objects.get(
                        nama_kepala_keluarga=field_nama_kepala_keluarga,
                        kepala_keluarga=True
                    )
                    self.cleaned_data['alamat'] = alamat_kepala_keluarga.alamat
                    self.cleaned_data['kelurahan'] = alamat_kepala_keluarga.kelurahan
                    self.cleaned_data['kecamatan'] = alamat_kepala_keluarga.kecamatan
                    self.cleaned_data['kota_kabupaten'] = alamat_kepala_keluarga.kota_kabupaten
                    self.cleaned_data['kode_pos'] = alamat_kepala_keluarga.kode_pos
                    self.cleaned_data['wilayah'] = alamat_kepala_keluarga.wilayah
                except ObjectDoesNotExist:
                    raise ValidationError("Nama Kepala Keluarga tidak boleh kosong!")

            else:
                if form_data['alamat'] == '':
                    raise ValidationError({'alamat': 'Alamat tidak boleh kosong'})


