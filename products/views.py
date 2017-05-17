from django.shortcuts import render, redirect,get_object_or_404
from models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import addMyProductform
from accounts.views import postMyProduct
from accounts.models import Profiledetails
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def all_products(request):
    products = Product.objects.exclude(owner= request.user)
    return render(request, "products.html", {"products": products})

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer

@login_required(login_url='/login')
def addMyProduct(request):
    if request.method == 'POST':
        form = addMyProductform(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
        return redirect(postMyProduct)
    else:
        form = addMyProductform()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'addproduct.html', args)

def product_detail(request, id):
    prod = get_object_or_404(Product, pk=id)
    prod.save()
    return render(request, "product_details.html", {'prod': prod})

def profile_detail(request, id):
    getprofile = get_object_or_404(Profiledetails, user_id=id)
    return render(request, "other_profile.html", {'getprofile': getprofile})

def others_products(request, id):
    otherproducts = Product.objects.filter(owner=id)
    return render(request, "otherUserProducts.html", {"otherproducts": otherproducts})

def otherprofile(request, id):
    getprofile = Profiledetails.objects.filter(user_id=id)
    return render(request, "other_profile.html", {'getprofile': getprofile})

def deleterequest(request, id):
    getdeleteobject = get_object_or_404(Product, pk=id)
    return render (request, "deleterequest.html", {'getdeleteobject': getdeleteobject})

def deleteobject (request, id):
    deleteobject = get_object_or_404(Product, pk=id)
    deleteobject.delete()
    return redirect(postMyProduct)

def deleteobjectno(request):
    return redirect(postMyProduct)