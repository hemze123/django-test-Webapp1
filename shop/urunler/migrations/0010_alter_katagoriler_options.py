# Generated by Django 5.1.3 on 2024-11-27 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0009_katagoriler_aciklama'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='katagoriler',
            options={'verbose_name': 'kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
    ]
