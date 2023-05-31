from django.contrib import admin
from django.forms.widgets import SelectDateWidget
from data.models import *
from django.utils.translation import ugettext_lazy
from datetime import date

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from djangoql.admin import DjangoQLSearchMixin

from data.forms import *
import datetime


class AnggotaResource(resources.ModelResource):
    class Meta:
        model = Anggota
        exclude = ('created_at', 'updated_at', )


class KeluargaResource(resources.ModelResource):
    class Meta:
        model = Keluarga
        exclude = ('created_at', 'updated_at', )


class AnggotaInline(admin.TabularInline):
    model = Anggota


class KeluargaAdmin(ImportExportModelAdmin):
    resource_class = KeluargaResource
    list_display = ('id', 'nama_kepala_keluarga',)
    list_display_links = ('id', 'nama_kepala_keluarga',)
    icon_name = 'home'
    #actions = None
    #inlines = [AnggotaInline,]
    ordering = ['nama_kepala_keluarga']
    search_fields = ['nama_kepala_keluarga']

    def has_add_permission(self, request):
        return False


#class AnggotaAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
class AnggotaAdmin(ImportExportModelAdmin):
    form = AnggotaForm
    resource_class = AnggotaResource
    icon_name = 'person'
    formfield_overrides = {models.DateField: {"widget": SelectDateWidget(years=range(1920, 2024))}}
    list_display = ('nomor_anggota', 'nama_kepala_keluarga', 'nama_anggota', 'jenis_kelamin', 'tanggal_lahir', 'calculate_age', 'wilayah', 'verifikasi')
    list_display_links = ('nomor_anggota', 'nama_anggota',)
    #list_filter = ('status_anggota', 'wilayah' )

    #list_filter = ('nama_kepala_keluarga__nama_kepala_keluarga',)
    list_filter = ('verifikasi',)

    search_fields = ['nomor_anggota', 'nama_anggota', 'nama_kepala_keluarga__nama_kepala_keluarga', 'alamat', 'kelurahan', 'kecamatan', 'wilayah__nama_wilayah']
    #djangoql_completion_enabled_by_default = False

    readonly_fields = ('created_at', 'updated_at',)
    #actions = None

    fieldsets = (
            ('Keanggotaan', {
                'classes': ('wide','extrapretty',),
                'fields' : (
                    'verifikasi',
                    'nomor_anggota',
                    'status_anggota',
                    'alasan_non_aktif',
                    )
                }),
            ('Nama dan Alamat', {
                'classes': ('wide','extrapretty',),
                'fields' : (
                    'kepala_keluarga',
                    'nama_kepala_keluarga',
                    'foto_anggota',
                    'nama_anggota',
                    'jenis_kelamin',
                    'status_pernikahan',
                    'tanggal_lahir',
                    'tempat_lahir',
                    'alamat_kk',
                    'alamat',
                    'kelurahan', 'kecamatan', 'kota_kabupaten', 'kode_pos',
                    'wilayah', 'gereja_asal'
                )
                }),
            ('Telp/HP, Email dan Darurat', {
                'classes': ('collapse',),
                'fields': (
                    'nomor_telp', 'nomor_hp',
                    'alamat_email', 'nomor_darurat', 'hubungan_darurat'
                )
                }),
            ('Etnik, Pendidikan dan Profesi', {
                'classes': ('collapse',),
                'fields': (
                    'etnik', 'pendidikan',
                    'profesi', 'nob',
                )
                }),
            ('Golongan Darah', {
                'classes': ('collapse',),
                'fields': (
                    'golongan_darah', 'golongan_darah_rhesus',
                )
                }),
            ('Status Kehidupan', {
                'classes': ('collapse',),
                'fields': (
                   'status_kehidupan',
                   'lokasi_pemakaman', 'lokasi_sari_mulia',
                )
                }),
            ('Baptis, Sidi dan Nikah', {
                'classes': ('collapse',),
                'fields': (
                    'tanggal_baptis', 'gereja_baptis', 'pendeta_baptis',
                    'tanggal_sidi', 'gereja_sidi', 'pendeta_sidi',
                    'tanggal_nikah', 'gereja_nikah', 'pendeta_nikah',
                )
                }),
            ('Info Pelayanan', {
                'classes': ('collapse',),
                'fields' : ('minat_pelayanan', 'riwayat_pelayanan'),
                }),
            ('Keterangan Lain', {
                'classes': ('collapse',),
                'fields' : ('nomor_kartu_parkir', 'keterangan'),
                }),
            ('Timestamp', {
                'classes': ('collapse',),
                'fields' : ('created_at', 'updated_at',),
                }),
            )

    #autocomplete_fields = ['kepala_keluarga', 'wilayah']

    @admin.display(description='Generasi')
    def decade_born_in(self, obj):
      return '%d’s' % (obj.tanggal_lahir.year // 10 * 10)

    '''
    @admin.display(description='Usia')
    def calculate_age(self, obj):
        today = date.today()
        try:
            age = (today.year - obj.tanggal_lahir.year) - ((today.month, today.day) < (obj.tanggal_lahir.month, obj.tanggal_lahir.day))
        except:
            age = 0
        return '%d' % age
    '''

admin.site.register(Keluarga, KeluargaAdmin)
admin.site.register(Anggota, AnggotaAdmin)

