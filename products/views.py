from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request, 'products/product.html')

def products(request):
        return render(request, 'products/products.html', {'pro':Product.objects.all() })
       # return render(request, 'products/products.html', {'pro':Product.objects.get(id=1) }) msh sha3'la
        #return render(request, 'products/products.html', {'pro':Product.objects.all().filter(price=88) })
       # return render(request, 'products/products.html', {'pro':Product.objects.all().filter(id=1) })
        #return render(request, 'products/products.html', {'pro':Product.objects.all().filter(name='oppo') })
        #return render(request, 'products/products.html', {'pro':Product.objects.all().order_by('price')})
        #return render(request, 'products/products.html', {'pro':str((Product.objects.all().count()))}) msh sha3'la
       # return render(request, 'products/products.html', {'pro':Product.objects.all().exclude(price =10)})
        #return render(request, 'products/products.html', {'pro':Product.objects.all().exclude(category='phone') })
        #return render(request, 'products/products.html', {'pro':Product.objects.all().filter(price__exact=88) })
        #return render(request, 'products/products.html', {'pro':Product.objects.all().filter(name__contains='p') })
        #return render(request, 'products/products.html', {'pro':Product.objects.all().filter(price__in=[500,600]) })
        #return render(request, 'products/products.html', {'pro':Product.objects.all().filter(price__range=[10,400]) })












