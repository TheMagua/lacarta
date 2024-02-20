from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Offer)



@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ['promo_name', 'min_date','max_date', 'local']
    list_per_page = 10
    search_fields = ['promo_name']
    
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(local__user=request.user)
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "local":
            kwargs["queryset"] = Local.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Winer)
class WinerAdmin(admin.ModelAdmin):
    list_display = ['winer_name', 'winer_ci','winer_movil', 'promo']
    list_per_page = 10
    search_fields = ['winer_name','winer_ci','winer_movil']
    
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(promo__local__user=request.user)
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "promo":
            kwargs["queryset"] = Promo.objects.filter(local__user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)