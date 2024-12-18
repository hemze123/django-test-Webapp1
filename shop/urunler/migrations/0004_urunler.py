# Generated by Django 5.1.3 on 2024-11-20 14:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_markalar_alter_katagoriler_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Urunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=155)),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('indirimlifiyat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('kisa_aciklama', models.TextField(blank=True, null=True)),
                ('aciklama', models.TextField(blank=True, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=155, null=True)),
                ('seo_description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=155, null=True, unique=True)),
                ('aktifmi', models.BooleanField(default=True)),
                ('resim', models.ImageField(blank=True, null=True, upload_to='markaresimleri')),
                ('tarih', models.DateTimeField(auto_now=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urunler.katagoriler')),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urunler.markalar')),
            ],
            options={
                'verbose_name': 'urun',
                'verbose_name_plural': 'urunler',
            },
        ),
    ]
