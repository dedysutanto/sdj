# Generated by Django 3.2.3 on 2022-08-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggota',
            name='hubungan_darurat',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='anggota',
            name='nomor_darurat',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]