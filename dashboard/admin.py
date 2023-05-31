from data.models import Anggota, Keluarga
from django.contrib import admin
from django.urls import path
from dashboard.models import *
from dashboard.views import *
from dashboard.chart import *
from django.template.response import TemplateResponse


class BirthdayAdmin(admin.ModelAdmin):

    template_name = 'dashboard/birthday.html'

    def get_urls(self):
        birthday_view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', self.birthday_view, name=birthday_view),
        ]

    def birthday_view(self, request):
        context = {
            **self.admin_site.each_context(request),
            'dashboard_title': 'Dashboard',
            'anggota': get_birthday_this_week()
        }
        return TemplateResponse(request, self.template_name, context)


class ChartAdmin(admin.ModelAdmin):

    template_name = 'dashboard/chart.html'

    def get_urls(self):
        chart_view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', self.chart_view, name=chart_view),
        ]

    def chart_view(self, request):
        total_verifikasi = Anggota.objects.filter(verifikasi=True).count()
        total_lk = Anggota.objects.filter(jenis_kelamin='LAKILAKI').count()
        total_pr = Anggota.objects.filter(jenis_kelamin='PEREMPUAN').count()

        list_gender, count_gender = chart_gender()
        list_profesi, count_profesi = chart_profesi()
        list_etnik, count_etnik = chart_etnik()
        list_blood, count_blood = chart_blood()
        list_marry, count_marry = chart_marry()
        list_pendidikan, count_pendidikan = chart_pendidikan()


        from datetime import date
        from dateutil.relativedelta import relativedelta

        ''' Up to 20 '''
        age_up_to_twenty = Anggota.objects.filter(tanggal_lahir__gt=date.today() - relativedelta(years=+20)).count()
        ''' 20 - 40 '''
        age_twenty_to_forty = Anggota.objects.filter(
                tanggal_lahir__lt=date.today() - relativedelta(years=+20)
            ).filter(
                tanggal_lahir__gt=date.today() - relativedelta(years=+40)
            ).count()
        ''' 40 - 60 '''
        age_forty_to_sixties = Anggota.objects.filter(
                tanggal_lahir__lt=date.today() - relativedelta(years=+40)
            ).filter(
                tanggal_lahir__gt=date.today() - relativedelta(years=+60)
            ).count()
        ''' More then 60 '''
        age_gt_sixties = Anggota.objects.filter(tanggal_lahir__lt=date.today() - relativedelta(years=+60)).count()


        context = {
            **self.admin_site.each_context(request),
            'dashboard_title': 'Dashboard',
            'total_jemaat': Anggota.objects.count(),
            'total_keluarga': Keluarga.objects.count(),
            'total_verifikasi': total_verifikasi,
            'total_lk': total_lk,
            'total_pr': total_pr,
            'list_gender': list_gender,
            'count_gender': count_gender,
            'list_profesi': list_profesi,
            'count_profesi': count_profesi,
            'list_pendidikan': list_pendidikan,
            'count_pendidikan': count_pendidikan,
            'list_etnik': list_etnik,
            'count_etnik': count_etnik,
            'list_blood': list_blood,
            'count_blood': count_blood,
            'list_marry': list_marry,
            'count_marry': count_marry,
            'age_up_to_twenty': age_up_to_twenty,
            'age_twenty_to_forty': age_twenty_to_forty,
            'age_forty_to_sixties': age_forty_to_sixties,
            'age_gt_sixties': age_gt_sixties
        }

        return TemplateResponse(request, self.template_name, context)

admin.site.register(Chart, ChartAdmin)
admin.site.register(Birthday, BirthdayAdmin)
