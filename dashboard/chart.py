from data.models import *
from data_support.models import *


# Count Status Pernikahan
def chart_marry():

    data_marry = {}
    all_marry = STATUS_PERNIKAHAN

    for e in all_marry:
        count_marry = Anggota.objects.filter(status_pernikahan=e[0]).count()
        data_marry[e[1]] = count_marry
    
    all_marry = list(data_marry.keys())
    return all_marry, data_marry

# Count Golongan Darah
def chart_blood():

    data_blood = {}
    all_blood = GOLONGAN_DARAH

    for e in all_blood:
        count_blood = Anggota.objects.filter(golongan_darah=e[0]).count()
        data_blood[e[1]] = count_blood
    
    all_blood = list(data_blood.keys())
    return all_blood, data_blood


# Count Gender
def chart_gender():

    data_gender = {}
    all_gender = JENIS_KELAMIN

    for e in all_gender:
        count_gender = Anggota.objects.filter(jenis_kelamin=e[0]).count()
        data_gender[e[1]] = count_gender
    
    all_gender = list(data_gender.keys())
    return all_gender, data_gender


# Count Etnik
def chart_etnik():

    data_etnik = {}
    all_etnik = Etnik.objects.all()

    for e in all_etnik:
        count_etnik = Anggota.objects.filter(etnik=e).count()
        data_etnik[e.nama_etnik] = count_etnik
    
    all_etnik = list(data_etnik.keys())
    return all_etnik, data_etnik


# Count Profesi
def chart_profesi():

    data_profesi = {}
    all_profesi = Profesi.objects.all()

    for e in all_profesi:
        count_profesi = Anggota.objects.filter(profesi=e).count()
        data_profesi[e.nama_profesi] = count_profesi

    all_profesi = list(data_profesi.keys())
    return all_profesi, data_profesi


# Count Pendidikan
def chart_pendidikan():

    data_pendidikan = {}
    all_pendidikan = Pendidikan.objects.all()

    for e in all_pendidikan:
        count_pendidikan = Anggota.objects.filter(pendidikan=e).count()
        data_pendidikan[e.nama_pendidikan] = count_pendidikan

    all_pendidikan = list(data_pendidikan.keys())
    return all_pendidikan, data_pendidikan


