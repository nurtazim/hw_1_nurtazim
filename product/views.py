from django.shortcuts import render, redirect
from product.models import Category
from product.models import Products
from product.forms import ProductForm
# Create your views here.

def category_vievs(request):
    category=Category.objects.all()
    produts=Products.objects.all()
    print(category)

    data={
        "Title":"Главная страница",
        "Category_list" : category,
        "Product_list": produts
    }
    return render(request,"index.html",context=data)


def category_item_views(request,Category_id):
    prod = Products.objects.filter(category_id=Category_id)
    category=Category.objects.all()
    produts = Products.objects.all()

    data = {
        "product_list":prod,
        "Category_list": category,
        "Product_list":produts
    }
    return render(request, "item.html", context=data)


def product_item_views(request,Product_id):
    product = Products.objects.get(id=Product_id)
    category = Category.objects.all()
    produts = Products.objects.all()
    data={
        "product":product,
        "Category_list": category,
        "Product_list": produts
    }
    return render(request, "product.html", context=data)


def add_product(request):
    if request.method =="GET":
        data={
            "form": ProductForm
        }
        return render(request,"add.html",context=data)
    elif request.method=="POST":
        form=ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")