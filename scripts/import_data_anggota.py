from django.core.exceptions import MultipleObjectsReturned, ValidationError
from django.db.models.deletion import SET_NULL
from data.models import *
import csv
import datetime
import re
import sys
import string

#path = sys.argv[1] 
#argv_nama_wilayah = sys.argv[2]
path = 'file.csv'

with open(path) as f:
    reader = csv.reader(f,delimiter=';')
    prev_alamat = 'sda'
    prev_nama_anggota = ''
    prev_kk = None

    for row in reader:
        if row[0] != '' and row[1] != '' and row[2] != '':
            st_anggota = 'ANGGOTA_SIDI'
            try:
                alamat_lower = row[2].lower()
            except:
                alamat_lower = ''

            print('Alamat Before: %s' % alamat_lower)


            ''' Status Menikah '''
            try:
                is_anak = row[0].translate({ord(c): None for c in string.whitespace}).upper().find('A')
            except:
                is_anak = -1
            st_menikah = 'MENIKAH'
            print("NOMOR")
            if is_anak != -1:
                st_anggota = 'ANGGOTA_ANAK'
                st_menikah = 'BELUM_MENIKAH'
                new_nomor = row[0]
            else:
                ''''Reformat nomor'''
                if row[0] != '' and len(row[0]) == 8 :
                    digit_nomor = "{:07d}".format(int(row[0][1:]))
                    new_nomor = "D" + digit_nomor
                else:
                    total_anggota = Anggota.objects.count() + 6000
                    new_nomor = ("D{:07d}".format(total_anggota))

            if new_nomor.find('.') != -1:
                new_nomor = "".join(new_nomor.split('.'))
            ''' Check Nomor '''
            try:
                is_nomor = Anggota.objects.get(nomor_anggota__icontains=new_nomor)
            except ObjectDoesNotExist:
                is_nomor = None

            if is_nomor != None:
                new_nomor = new_nomor[:1] + "{:07d}".format(int(new_nomor[1:]) + 7000)


            ''' Clean Nama '''
            nama_ok = re.sub("\(.*?\)","",row[1])

            is_kepala_keluarga = True
            if (alamat_lower.find('sda') != -1):
                ala = prev_alamat
                print('Alamat After: %s' % ala)
                print('Prev KK: %s' % prev_nama_anggota.strip().strip("."))
                '''
                try:
                    kk = Keluarga.objects.get(nama_kepala_keluarga__icontains=prev_nama_anggota.strip().strip("."))
                except MultipleObjectsReturned:
                    try:
                        kk = Keluarga.objects.get(nama_kepala_keluarga__iexact=prev_nama_anggota.strip())
                    except:
                        pass

                '''
                if prev_kk != None:
                    kk = prev_kk

                #kk = Keluarga.objects.get('nama_kepala_keluarga__icontains', prev_nama_anggota[:30])
                is_kepala_keluarga = False
                print('KK After: %s' % kk)

            else:
                ala = row[2]
                nama_kk_ok = nama_ok + " #" + new_nomor[1:]
                try:
                    #kk = Keluarga.objects.get(nama_kepala_keluarga__icontains=nama_kk_ok)
                    kk = Keluarga.objects.get(nama_kepala_keluarga__icontains=new_nomor[1:])
                except ObjectDoesNotExist:
                    kk = Keluarga.objects.create (
                        nama_kepala_keluarga = nama_kk_ok
                    )

                prev_kk = kk
                prev_nama_anggota = nama_ok
                #prev_alamat = ala


            ''' Check tanggal_lahir '''
            try:
                dob = datetime.datetime.strptime(row[5], "%d-%b-%Y").strftime("%Y-%m-%d")

            except:
                try:
                    dob = datetime.datetime.strptime(row[5], "%d %b %Y").strftime("%Y-%m-%d")
                except:
                    dob = None
            print("DOB %s" % dob)

            ''' Check golongan_darah'''
            darah_ok = 'NN'
            darah_rhesus_ok = 'NN'
            try:
                is_darah = row[6].translate({ord(c): None for c in string.whitespace})
            except:
                is_darah = ""
            if (is_darah != ""):
                darah_ok = row[6].translate({ord(c): None for c in string.whitespace}).upper()
                darah_rhesus_ok = 'RP'
            print("DARAH %s" % darah_ok)

            ''' Check Pendidikan '''
            try:
                is_pendidikan = row[7].translate({ord(c): None for c in string.whitespace}).lower()
                try:
                    the_key = Pendidikan.objects.get(nama_pendidikan__icontains=is_pendidikan)
                except:
                    the_key = None
            except ObjectDoesNotExist:
                the_key = None

            pendidikan_ok = the_key

            print("PENDIDIKAN %s" % pendidikan_ok)

            ''' Check Pekerjaan '''
            if row[8] != '':
                is_profesi = row[8].lower()
                try:
                    the_key = Profesi.objects.get(nama_profesi__icontains=row[8].lower())
                except (ObjectDoesNotExist,MultipleObjectsReturned):
                    try:
                        the_key = Profesi.objects.get(nama_profesi__iexact=row[8].upper())
                    except (ObjectDoesNotExist, MultipleObjectsReturned):
                        the_key = None

            else:
                the_key = None

            profesi_ok = the_key
            print("PROFESI %s" % profesi_ok)

            ''' Check Etnik '''
            if row[9] != '':
                is_etnik = row[9].lower()
                try:
                    the_key = Etnik.objects.get(nama_etnik__icontains=is_etnik)
                except ObjectDoesNotExist:
                    the_key = None
            else:
                the_key = None

            etnik_ok = the_key
            print("ETNIK %s" % etnik_ok)

            ''' Check Email '''
            if (row[10].find('@') != -1):
                try:
                    email_ok = row[10].translate({ord(c): None for c in string.whitespace}).lower()
                except:
                    email_ok = ''
            else:
                email_ok = ''
            print("EMAIL %s" % email_ok)

            ''' Check Keterangan '''
            keterangan_ok = row[11]

            ''' Check Riwayat Pelayanan '''
            riwayat_pelayanan_ok = row[12]

            ''' Check Wilayah '''
            #try:
                #the_key = Wilayah.objects.get(nama_wilayah__icontains=row[12].lower())
            #except ObjectDoesNotExist:
                #the_key = None

            #wilayah_ok = the_key

            #wil = Wilayah.objects.get(nama_wilayah__icontains = 'KENCANA LOKA')
            #wil = Wilayah.objects.get(nama_wilayah__icontains = argv_nama_wilayah.upper())

            #print('Kepala Keluarga: %s' % kk.nama_kepala_keluarga)
            #print('Alamat: %s' % row[2])

            print("%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s" % (
                is_kepala_keluarga,
                new_nomor, nama_ok,
                st_anggota, kk,
                ala, kelurahan_ok,
                row[3], row[4],
                dob, st_menikah,
                darah_ok, darah_rhesus_ok,
                email_ok,
                wilayah_ok, etnik_ok,
                pendidikan_ok, profesi_ok,
                keterangan_ok,
                riwayat_pelayanan_ok
            ))

            try:
                anggota = Anggota.objects.create (
                    kepala_keluarga = is_kepala_keluarga,
                    nomor_anggota = new_nomor,
                    nama_anggota = nama_ok,
                    status_anggota = st_anggota,
                    nama_kepala_keluarga = kk,
                    alamat = ala,
                    kelurahan = kelurahan_ok,
                    nomor_telp = row[3],
                    nomor_hp = row[4],
                    tanggal_lahir = dob,
                    status_pernikahan = st_menikah,
                    golongan_darah = darah_ok,
                    golongan_darah_rhesus = darah_rhesus_ok,
                    alamat_email = email_ok,
                    wilayah = wilayah_ok,
                    etnik = etnik_ok,
                    pendidikan = pendidikan_ok,
                    profesi = profesi_ok,
                    keterangan = keterangan_ok,
                    riwayat_pelayanan = riwayat_pelayanan_ok
                )
            except ValidationError as e:
                print("Exception: %s" % e)

            prev_alamat = ala

        if row[0] != '' and row[1] == '':
            kelurahan_ok = row[0]
            print('Kelurahan: %s' % kelurahan_ok)

        if row[0].upper() == 'WILAYAH':
            print('Wilayah: %s' % row[1].upper())

            ''' Check Wilayah '''
            try:
                the_key = Wilayah.objects.get(nama_wilayah__icontains=row[1].lower())
            except ObjectDoesNotExist:
                the_key = None

            wilayah_ok = the_key
