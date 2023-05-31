import datetime
from django.shortcuts import render
from data.models import Anggota

# Create your views here.

def get_birthday_this_week():
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(6)
    anggota = Anggota.objects.filter(
        tanggal_lahir__day__gte=start_week.day,
        tanggal_lahir__day__lte=end_week.day,
        tanggal_lahir__month__gte=start_week.month,
        tanggal_lahir__month__lte=end_week.month,
    ).order_by('tanggal_lahir')
    return anggota

'''
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.models import Dashboard
from django.template.response import TemplateResponse

def DashboardView(request):
    template = 'dashboard/index.html'
    context = {
        'total_anggota': 99,
        'total_simpatisan': 9
        }
    return TemplateResponse(request, template, context)
    #return render(request, template, context)
    #return HttpResponse('Admin Custom View')
    '''
    
