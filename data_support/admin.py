from django.contrib import admin
from data_support.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class EtnikResource(resources.ModelResource):
    class Meta:
        model = Etnik
        exclude = ('created_at', 'updated_at', )


class PendidikanResource(resources.ModelResource):
    class Meta:
        model = Pendidikan
        exclude = ('created_at', 'updated_at', )


class ProfesiResource(resources.ModelResource):
    class Meta:
        model = Profesi
        exclude = ('created_at', 'updated_at', )


class NobResource(resources.ModelResource):
    class Meta:
        model = Nob
        exclude = ('created_at', 'updated_at', )


class PelayananResource(resources.ModelResource):
    class Meta:
        model = Pelayanan
        exclude = ('created_at', 'updated_at', )


class WilayahResource(resources.ModelResource):
    class Meta:
        model = Wilayah
        exclude = ('created_at', 'updated_at', )


class EtnikAdmin(ImportExportModelAdmin):
    resource_class = EtnikResource
    list_display = ('id', 'nama_etnik')
    ordering = ['id']
    search_fields =  ['nama_etnik']


class PendidikanAdmin(ImportExportModelAdmin):
    resource_class = PendidikanResource
    list_display = ('id', 'nama_pendidikan')
    ordering = ['id']
    search_fields =  ['nama_pendidikan']


class ProfesiAdmin(ImportExportModelAdmin):
    resource_class = ProfesiResource
    list_display = ('id', 'nama_profesi')
    ordering = ['id']
    search_fields =  ['nama_profesi']


class NobAdmin(ImportExportModelAdmin):
    resource_class = NobResource
    list_display = ('id', 'nama_nob')
    ordering = ['id']
    search_fields =  ['nama_nob']


class PelayananAdmin(ImportExportModelAdmin):
    resource_class = PelayananResource  
    list_display = ('id', 'nama_pelayanan')
    ordering = ['id']
    search_fields =  ['nama_pelayanan']


class WilayahAdmin(ImportExportModelAdmin):
    resource_class = WilayahResource
    list_display = ('id', 'nama_wilayah')
    ordering = ['id']
    search_fields =  ['nama_wilayah']


admin.site.register(Etnik, EtnikAdmin)
admin.site.register(Pendidikan, PendidikanAdmin)
admin.site.register(Profesi, ProfesiAdmin)
admin.site.register(Nob, NobAdmin)
admin.site.register(Pelayanan, PelayananAdmin)
admin.site.register(Wilayah, WilayahAdmin)
