import pandas as pd
import numpy as np
import csv
from data.models import *
from data_support.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError
from django.utils.dateparse import parse_date

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


'''
with open('data-sdj.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, dialect='excel')
    print(csv_reader)
    line_count = 0
    for row in csv_reader:
        #if line_count == 0:
        #    print(f'Column names are {";".join(row)}')
        #    line_count += 1
        #print(f'\t{row["Status Anggota"]} works in the {row["Nama Lengkap"]} department, and was born in {row["Tanggal Lahir"]}.')
        line_count += 1
        print(row)
    #print(f'Processed {line_count} lines.')
'''


def find_in_choices(choices, choice):
    for option in choices:
        if choice in option:
            result = option[0]
            #print(STATUS)
            break
    return result


def find_blood(choices, choice):
    result = 'NN'
    for option in choices:
        if choice in option[1]:
            result = option[0]
            #print(STATUS)
            break
    return result


def find_pendidikan(choice):
    choice = 'Diploma'.upper() if choice == 'D3' else choice
    choice = 'Diploma'.upper() if choice == 'D4' else choice

    choice = str(choice).upper()
    try:
        return Pendidikan.objects.get(nama_pendidikan=choice)
    except ObjectDoesNotExist:
        return Pendidikan.objects.get(nama_pendidikan='SD')


def find_profesi(choice):
    choice = 'Pegawai Negeri/Daerah/Pemerintah/Bumn'.upper() if choice == 'Pegawai Negeri/Daerah/Pemerintah/BUMN' else choice
    choice = 'Tni/Polri'.upper() if choice == 'TNI/Polri' else choice
    choice = 'Praktisi/Penegak Hukum (Jaksa, Hakim, Lawyer, Notaris Dll)'.upper() \
        if choice == 'Praktisi/Penegak Hukum (Jaksa, Hakim, Pengacara, Notaris, dll)' else choice
    choice = 'Pensiunan - Pegawai Negeri/Daerah/Pemerintah/Bumn/Swasta'.upper() \
        if choice == 'Pensiunan - Pegawai Negeri/Daerah/Pemerintah/BUMN/Swasta' else choice
    choice = 'Profesional, Designer, Arsitek, Akuntan Dan Konsultan Lainnya'.upper() \
        if choice == 'Profesional, Desainer, Arsitek, Akuntan, dan Konsultan lainnya' else choice
    choice = 'Tenaga Lepas/Kecil: Buruh/Asn/Satpam/Satpol Pp'.upper() \
        if choice == 'Tenaga Lepas/Kecil: Buruh/ASN/Satpam/Satpol PP' else choice
    choice = 'Pengurus Lsm/Partai/Organisasi/Yayasan Kemasyarakatan'.upper() \
        if choice == 'Pengurus LSM/Partai/Organisasi/Yayasan Kemasyarakatan'.upper() else choice
    choice = 'Pengurus Legislatif/Dpr/Dprd'.upper() \
        if choice == 'Pengurus Legislatif/DPR/DPRD' else choice

    choice = str(choice).upper()
    try:
        return Profesi.objects.get(nama_profesi__iexact=choice)
    except ObjectDoesNotExist:
        return Profesi.objects.get(nama_profesi='Lainnya'.upper())


def find_nob(choice):
    choice = 'Ekonomi, Manajemen Dan Keuangan'.upper() if choice == 'Ekonomi, Manajemen, dan Keuangan' else choice
    choice = 'Teknik - It/Komputer'.upper() if choice == 'Teknik - IT/Komputer' else choice
    choice = 'Pertambangan Dan Perminyakan'.upper() if choice == 'Pertambangan dan Perminyakan' else choice
    choice = 'Pertahanan Dan Keamanan'.upper() if choice == 'Pertahanan dan Keamanan' else choice
    choice = 'Sejarah Dan Budaya'.upper() if choice == 'Sejarah dan Budaya' else choice
    choice = 'Farmasi Dan Kimia'.upper() if choice == 'Farmasi dan Kimia' else choice

    choice = str(choice).upper()

    try:
        return Nob.objects.get(nama_nob=choice)
    except ObjectDoesNotExist:
        return Nob.objects.get(nama_nob='Lainnya'.upper())


def find_etnik(choice):
    #choice = 'Ekonomi, Manajemen Dan Keuangan' if choice == 'Ekonomi, Manajemen, dan Keuangan' else choice

    choice = str(choice).upper()
    try:
        return Etnik.objects.get(nama_etnik=choice)
    except ObjectDoesNotExist:
        return Etnik.objects.get(nama_etnik='Lainnya'.upper())


def find_wilayah(choice):
    #choice = 'Ekonomi, Manajemen Dan Keuangan' if choice == 'POS JEMAAT CIKOLEANG' else choice

    try:
        return Wilayah.objects.get(nama_wilayah=choice)
    except ObjectDoesNotExist:
        return None


def find_minat_pelayanan(choice):
    choice = 'Paduan Suara'.upper() if choice == 'PaduanSuara' else choice
    choice = 'Klinik Kesehatan'.upper() if choice == 'KlinikKesehatan' else choice
    choice = 'Pemandu Nyanyian Jemaat'.upper() if choice == 'PemanduNyanyianJemaat' else choice
    choice = 'Pelayanan Anak Berkebutuhan Khusus'.upper() if choice == 'PelayananAnakBerkebutuhanKhusus' else choice
    choice = 'Fasilitator Pa'.upper() if choice == 'Fasilitator PA' else choice

    choice = str(choice).upper()
    try:
        return Pelayanan.objects.get(nama_pelayanan=choice)
    except ObjectDoesNotExist:
        return None


def import_data(kk=True):
    df = pd.read_excel(r'data-import/data-sdj.xls', dtype=str)
    df = df.replace(np.nan, '', regex=True)  # All data frame

    for row in df.iterrows():
        row_dict = row[1].to_dict()

        wilayah = str(row_dict['Wilayah']).upper()
        status_anggota = row_dict['Status Anggota'].replace(' GKI Serpong', '')
        jenis_kelamin = row_dict['Jenis Kelamin'].replace(' ', '')
        status_pernikahan = row_dict['Status Pernikahan']
        tanggal_lahir = str(row_dict['Tanggal Lahir']).replace(' 00:00:00', '')
        tempat_lahir = row_dict['Tempat Lahir']
        alamat_domisili = row_dict['Alamat Domisili']
        kelurahan = row_dict['Kelurahan']
        kecamatan = row_dict['Kecamatan']
        kota_kabupaten = row_dict['Kota/Kabupaten']
        kode_pos = row_dict['Kode Pos']
        gereja_asal = row_dict['Gereja Asal']
        nomor_telepon = row_dict['Nomor Telepon (rumah)']
        nomor_hp = row_dict['Nomor HP Pribadi']
        email = row_dict['Email Pribadi']
        nomor_darurat = row_dict['Nama dan Nomor HP Kontak Darurat (orang lain terdekat)']
        hubungan_darurat = row_dict['Hubungan dengan kontak darurat']
        posisi_dalam_keluarga = row_dict['Posisi dalam keluarga']
        nama_lengkap = str(row_dict['Nama Lengkap']).upper()
        nama_lengkap_kepala_keluarga = str(row_dict['Nama Lengkap Kepala Keluarga']).upper()
        golongan_darah = row_dict['Golongan Darah']
        rhesus_golongan_darah = row_dict['Rhesus Golongan Darah']
        pendidikan = row_dict['Pendidikan']
        profesi = row_dict['Profesi']
        nob = row_dict['Nature of Business']
        etnik = row_dict['Etnik']
        tanggal_baptis = str(row_dict['Tanggal Baptis']).replace(' 00:00:00', '')
        gereja_baptis = row_dict['Gereja tempat berlangsungnya Baptis']
        pendeta_baptis = row_dict['Pendeta yang melayani Baptis']
        tanggal_sidi = row_dict['Tanggal Sidi']
        gereja_sidi = row_dict['Gereja tempat berlangsungnya Sidi']
        pendeta_sidi = row_dict['Pendeta yang melayani Sidi']
        tanggal_nikah = str(row_dict['Tanggal Pernikahan']).replace(' 00:00:00', '')
        gereja_nikah = row_dict['Gereja tempat berlangsungnya Pernikahan']
        pendeta_nikah = row_dict['Pendeta yang memberkati Pernikahan']
        minat_pelayanan = str(row_dict['Minat Pelayanan'])
        if ',' in minat_pelayanan:
            pelayanan = minat_pelayanan.split(',')
            minat_pelayanan = pelayanan[0].replace(' ', '')
        riwayat_pelayanan = row_dict['Riwayat Pelayanan']

        '''
        print(find_in_choices(STATUS_KEANGGOTAAN, status_anggota),
            find_in_choices(JENIS_KELAMIN, jenis_kelamin),
            find_in_choices(STATUS_PERNIKAHAN, status_pernikahan),
            find_blood(GOLONGAN_DARAH, golongan_darah),
            find_blood(GOLONGAN_DARAH_RHESUS, rhesus_golongan_darah),
            tanggal_lahir,
            posisi_dalam_keluarga)
        '''

        nama_lengkap = nama_lengkap.replace("'", "")
        nama_lengkap = nama_lengkap.replace('  ', ' ')
        nama_lengkap_kepala_keluarga = nama_lengkap_kepala_keluarga.replace('  ', ' ')
        nama_lengkap_kepala_keluarga = nama_lengkap_kepala_keluarga.replace('\'', '')

        try:
            tanggal_lahir = parse_date(tanggal_lahir)
        except TypeError:
            tanggal_lahir = None

        try:
            tanggal_baptis = parse_date(tanggal_baptis)
        except TypeError:
            tanggal_baptis = None

        try:
            tanggal_sidi = parse_date(tanggal_sidi)
        except TypeError:
            tanggal_sidi = None

        try:
            tanggal_nikah = parse_date(tanggal_nikah)
        except TypeError:
            tanggal_nikah = None

        is_verify = True
        if kk:
            if posisi_dalam_keluarga == 'Kepala Keluarga' or posisi_dalam_keluarga == 'Single':
                is_save = True
                kepala_keluarga = True
                #print(nama_lengkap)
                try:
                    #Keluarga.objects.get(nama_kepala_keluarga__icontains=nama_lengkap)
                    Anggota.objects.get(
                        nama_anggota__istartswith=nama_lengkap.strip(),
                        tanggal_lahir=tanggal_lahir)
                    is_save = False
                except ObjectDoesNotExist:
                    try:
                        #Anggota.objects.get(
                        #    nama_anggota__istartswith=nama_lengkap.strip(),
                        #    tempat_lahir__istartswith=tempat_lahir)
                        Keluarga.objects.get(nama_kepala_keluarga__istartswith=nama_lengkap.strip() + ' #')
                        is_save = False
                    except ObjectDoesNotExist:
                        pass
            else:
                is_save = False
                kepala_keluarga = False
        else:
            if posisi_dalam_keluarga != 'Kepala Keluarga':
                if nama_lengkap_kepala_keluarga is None:
                    nama_lengkap_kepala_keluarga = nama_lengkap
                is_save = True
                kepala_keluarga = False
                is_miss_kk = False
                #print(nama_lengkap)
                try:
                    Anggota.objects.get(
                        nama_anggota__istartswith=nama_lengkap.strip(), tanggal_lahir=tanggal_lahir)
                    is_save = False
                except ObjectDoesNotExist:
                    try:
                        my_kk = Keluarga.objects.get(
                            nama_kepala_keluarga__istartswith=nama_lengkap_kepala_keluarga.strip() + ' #')
                        #print(my_kk)
                        my_kepala_keluarga = Anggota.objects.get(
                            kepala_keluarga=True,
                            nama_kepala_keluarga=my_kk
                        )
                    except ObjectDoesNotExist:
                        is_save = True
                        is_verify = False
                        print(
                            '{};{};{};{};{};{};{};{};{};{};{};{}'.format(
                                posisi_dalam_keluarga,
                                find_in_choices(STATUS_KEANGGOTAAN, status_anggota),
                                nama_lengkap_kepala_keluarga,
                                nama_lengkap,
                                tanggal_lahir,
                                tempat_lahir,
                                find_in_choices(JENIS_KELAMIN, jenis_kelamin),
                                find_in_choices(STATUS_PERNIKAHAN, status_pernikahan),
                                find_wilayah(wilayah),
                                find_profesi(profesi),
                                find_nob(nob),
                                find_blood(GOLONGAN_DARAH, golongan_darah),
                                find_blood(GOLONGAN_DARAH_RHESUS, rhesus_golongan_darah),
                            )
                        )
                        my_kepala_keluarga = Anggota()
                        my_kepala_keluarga.nama_anggota = nama_lengkap_kepala_keluarga.strip()
                        my_kepala_keluarga.status_anggota = find_in_choices(STATUS_KEANGGOTAAN, status_anggota)
                        my_kepala_keluarga.kepala_keluarga = True
                        my_kepala_keluarga.save()
                        my_kk = Keluarga.objects.get(
                            nama_kepala_keluarga__istartswith=nama_lengkap_kepala_keluarga.strip() + ' #')
                        is_miss_kk = True
            else:
                is_save = False
                kepala_keluarga = False

        if is_save:
            anggota = Anggota()
            if not kepala_keluarga:
                anggota.nama_kepala_keluarga = my_kk

            anggota.kepala_keluarga = kepala_keluarga
            anggota.nama_anggota = str(nama_lengkap).strip()
            anggota.status_anggota = find_in_choices(STATUS_KEANGGOTAAN, status_anggota)
            anggota.jenis_kelamin = find_in_choices(JENIS_KELAMIN, jenis_kelamin)
            anggota.status_pernikahan = find_in_choices(STATUS_PERNIKAHAN, status_pernikahan)
            anggota.tanggal_lahir = tanggal_lahir
            anggota.tempat_lahir = str(tempat_lahir).strip()
            if kepala_keluarga or is_miss_kk:
                anggota.wilayah = find_wilayah(wilayah)
                anggota.alamat = str(alamat_domisili).strip()
                anggota.kelurahan = str(kelurahan).strip()
                anggota.kecamatan = str(kecamatan).strip()
                anggota.kota_kabupaten = str(kota_kabupaten).strip()
                anggota.kode_pos = str(kode_pos).strip()
            else:
                anggota.wilayah = my_kepala_keluarga.wilayah
                anggota.alamat = my_kepala_keluarga.alamat
                anggota.kelurahan = my_kepala_keluarga.kelurahan
                anggota.kecamatan = my_kepala_keluarga.kecamatan
                anggota.kota_kabupaten = my_kepala_keluarga.kota_kabupaten
                anggota.kode_pos = my_kepala_keluarga.kode_pos

            anggota.gereja_asal = str(gereja_asal).strip()
            # Profesi
            anggota.profesi = find_profesi(profesi)
            anggota.nob = find_nob(nob)
            anggota.golongan_darah = find_blood(GOLONGAN_DARAH, golongan_darah)
            anggota.golongan_darah_rhesus = find_blood(GOLONGAN_DARAH_RHESUS, rhesus_golongan_darah)
            anggota.etnik = find_etnik(etnik)
            anggota.pendidikan = find_pendidikan(pendidikan)
            # Kontak
            anggota.alamat_email = str(email).strip()
            anggota.nomor_telp = str(nomor_telepon).strip()
            anggota.nomor_hp = str(nomor_hp).strip()
            anggota.nomor_darurat = str(nomor_darurat).strip()
            anggota.hubungan_darurat = str(hubungan_darurat).strip()
            anggota.tanggal_baptis = tanggal_baptis
            anggota.tanggal_sidi = tanggal_sidi
            anggota.tanggal_nikah = tanggal_nikah
            anggota.gereja_baptis = str(gereja_baptis).strip()
            anggota.gereja_sidi = str(gereja_sidi).strip()
            anggota.gereja_nikah = str(gereja_nikah).strip()
            anggota.pendeta_baptis = str(pendeta_baptis).strip()
            anggota.pendeta_sidi = str(pendeta_sidi).strip()
            anggota.pendeta_nikah = str(pendeta_nikah).strip()
            anggota.minat_pelayanan = find_minat_pelayanan(pelayanan)
            anggota.riwayat_pelayanan = str(riwayat_pelayanan)
            anggota.verifikasi = is_verify
            anggota.save()


def update_nomor_anggota():
    path = 'result.csv'

    with open(path) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row[0], row[1])
            try:
                angg = Anggota.objects.get(nama_anggota__icontains=row[1])
                angg.nomor_anggota = row[0]
                angg.save()
                print("Importing", row[0], row[1])
            except ObjectDoesNotExist:
                print("Does NOT Exists", row[0], row[1])
            except MultipleObjectsReturned:
                print("Multiple", row[0], row[1])
            except ValidationError:
                print("Nomor Double", row[0], row[1])

