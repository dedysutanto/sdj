# Generated by Django 3.2.3 on 2022-08-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20220829_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota',
            name='status_anggota',
            field=models.CharField(choices=[('ANGGOTA_SIDI', 'Anggota Sidi'), ('ANGGOTA_ANAK', 'Anggota Anak'), ('SIMPATISAN', 'Simpatisan'), ('NON_AKTIF', 'Non Aktif')], default='ANGGOTA_SIDI', max_length=30),
        ),
    ]
