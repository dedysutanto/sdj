# Generated by Django 3.2.3 on 2022-08-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_anggota_status_anggota'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggota',
            name='alamat_kk',
            field=models.BooleanField(default=False),
        ),
    ]