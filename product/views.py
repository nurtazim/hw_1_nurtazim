from django.shortcuts import render
from product.models import Category
from product.models import Products
# Create your views here.

def category_vievs(request):
    category=Category.objects.all()
    print(category)

    data={
        "Title":"Главная страница",
        "Category_list" : category
    }
    return render(request,"index.html",context=data)


def category_item_views(request,Category_id):
    prod = Products.objects.filter(category_id=Category_id)

    data = {
        "product_list":prod
    }
    return render(request, "item.html", context=data)

