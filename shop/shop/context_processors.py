from urunler.models import Kategoriler


def kategoriler(request):
    return {
        'kategoriler':Kategoriler.objects.filter(menudegoster=True)
    }