from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.utils.text import slugify


# Create your models here.
class Katagoriler(models.Model):
    isim = models.CharField(max_length=155)
    ustkategori = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                    help_text="ustkategoriniz varsa girin")
    aciklama = models.TextField(blank=True, null=True)
    aktifmi = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True)
    menudegoster = models.BooleanField(default=True)



    class Meta:
        verbose_name_plural="Kategoriler"
        verbose_name="kategori"

    def __str__(self):
        return self.isim




class Markalar(models.Model):
    isim = models.CharField(max_length=155)
    aciklama=models.TextField(blank=True,null=True)
    aktifmi = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True)
    resim=models.ImageField(upload_to="markaresimleri",blank=True,null=True)


    class Meta:
        verbose_name_plural="markalar"
        verbose_name="marka"


    def __str__(self):
        return self.isim

class Etiketler(models.Model):
    isim = models.CharField(max_length=155)
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True)
    aktifmi = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Etiketler"
        verbose_name = "Etiket"

    def __str__(self):
        return self.isim

class Urunler(models.Model):
    isim = models.CharField(max_length=155)
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    marka=models.ForeignKey(Markalar,on_delete=models.CASCADE)
    kategori=models.ForeignKey(Katagoriler,on_delete=models.CASCADE)
    indirimlifiyat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    kisa_aciklama=models.TextField(blank=True,null=True)
    aciklama = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=155, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=155, unique=True, blank=True, null=True)
    aktifmi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to="markaresimleri", blank=True, null=True)
    tarih = models.DateTimeField(auto_now=True)
    etiketler=models.ManyToManyField(Etiketler,blank=True)
    anasayfa= models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "urunler"
        verbose_name = "urun"

    def __str__(self):
        return self.isim

    def save( self, *args,**kwargs):
        if not self.slug:

            self.slug=slugify(self.isim)
        super(Urunler, self).save(*args, **kwargs)
        return self.slug





class Varyasyonlar(models.Model):
    urun = models.ForeignKey(Urunler, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    varyasyon = models.CharField(max_length=155)
    fiyat=models.DecimalField(max_digits=10, decimal_places=2)
    stok= models.IntegerField()
    aktifmi=models.BooleanField(default=True)
    resim=models.ImageField(upload_to='varyasyonresimleri',blank=True,null=True)
    class Meta:
        verbose_name_plural = "varyasyonlar"
        verbose_name = "varyasyon"

    def __str__(self):
        return self.varyasyon