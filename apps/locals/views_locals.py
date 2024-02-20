from django.shortcuts import render
from apps.locals.models import Category, Gallery, Local,Aggregate, Ingredient,  Product
from django.db.models import Q
from apps.offer.forms.winer_forms import WinerForm
from apps.offer.models import Promo

# Create your views here.


def product_detail(request,pk):
    product = Product.objects.filter(pk = pk).filter(active = True).first()
    aggregates = Aggregate.objects.filter(product = product.id)
    ingredients = Ingredient.objects.filter(product = product.id)
    return render(request,'product.html',context = {"product":product,"aggregates":aggregates,"ingredients":ingredients,})



# Create your views here.


def local_detail(request,pk):
    query = request.GET.get('q')
    local = Local.objects.filter(pk = pk).filter(active = True).first()
    galleries = Gallery.objects.filter(local=pk)
    local_categories=Category.objects.filter(local=pk)
    categories =[]
    cart = []
    promo = Promo.objects.filter(local=pk).first()
    if query:
        for category in local_categories:
            products = Product.objects.filter(category=category).filter(Q(product_name__icontains=query)).exclude(active=False)
            if products.exists():
                categories.append(category)
                cart.append({
                    'category': category.category_name,
                    'products': products
                })
    else:
        for category in local_categories:
            products = Product.objects.filter(category=category).exclude(active=False)
            if products.exists():
                categories.append(category)
                cart.append({
                    'category': category.category_name,
                    'products': products
                })
                
    if request.method == 'POST':
        form = WinerForm(request.POST)
        if form.is_valid():
            form.save()
      
    else:
        
        form = WinerForm(initial={'promo': promo})
    
    
    return render(request,'local.html',context = {"local":local,'galleries':galleries,'categories':categories,'cart':cart,'q':query,'form': form,'promo':promo})