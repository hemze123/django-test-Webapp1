from django.contrib import admin
from .models import Katagoriler, Markalar, Urunler, Etiketler,Varyasyonlar


# Register your models here.
class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim','seo_title','seo_description','slug','aktifmi']
    list_filter = ['aktifmi']
    search_fields = ['isim','seo_title','seo_description','slug']

admin.site.register(Katagoriler,KategoriAdmin)


class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim', 'seo_title', 'seo_description', 'slug', 'aktifmi','resim']
    list_filter = ['aktifmi','isim']
    search_fields = ['isim', 'seo_title',  'slug']

admin.site.register(Markalar,MarkalarAdmin)

class InlineVaryasyon(admin.StackedInline):
    model = Varyasyonlar
    extra=1

class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['isim', 'fiyat', 'marka','kategori','indirimlifiyat','aktifmi','resim','tarih',]
    list_filter = ['aktifmi', 'isim','kategori','marka']
    search_fields = ['resim', 'seo_title', 'slug']
    inlines = [InlineVaryasyon]



admin.site.register(Urunler, UrunlerAdmin)
admin.site.register(Etiketler)