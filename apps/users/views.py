from datetime import date
from django.db.models import Q
from django.shortcuts import render
from apps.locals.models import Local
from apps.offer.models import Offer
# Create your views here.

def index(request):
    query = request.GET.get('q')
    if query:
        locals = Local.objects.filter(active = True).filter(Q(type__icontains=query) | Q(local_name__icontains=query))
    else:
        locals = Local.objects.filter(active = True)
    offers = Offer.objects.filter(max_date__gte=date.today()).filter(min_date__lte=date.today())
    return render(request,'homepage/index.html',context = {"locals":locals, 'offers':offers,'q':query})