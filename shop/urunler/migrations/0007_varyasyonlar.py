# Generated by Django 5.1.3 on 2024-11-27 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0006_urunler_anasayfa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Varyasyonlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varyasyon', models.CharField(max_length=155)),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stok', models.IntegerField()),
                ('aktifmi', models.BooleanField(default=True)),
                ('resim', models.ImageField(blank=True, null=True, upload_to='varyasyonresimleri')),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urunler.urunler')),
            ],
            options={
                'verbose_name': 'varyasyon',
                'verbose_name_plural': 'varyasyonlar',
            },
        ),
    ]
