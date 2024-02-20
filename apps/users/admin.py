from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # exclude = ('groups','is_superuser','user_permissions','is_staff',)
    list_display = ['username', 'email', 'movil', 'ci' ,'name', 'last_name',]
    search_fields = ['username', 'email','ci']
    
    def get_form(self, request, obj=None, **kwargs):
        # Obtén el formulario original
        form = super().get_form(request, obj, **kwargs)

        # Si el usuario es superadministrador, no excluir campos
        if request.user.is_superuser == True:
            return form
        else:
            form.base_fields.update(form.declared_fields)
            form.base_fields.pop('is_superuser', None)
            form.base_fields.pop('is_staff', None)
            form.base_fields.pop('groups', None)
            form.base_fields.pop('user_permissions', None)
        return form

        
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id=request.user.id)
        
    def has_add_permission(self, request):
        # Obtiene todos los Locales asociados con el usuario actual
        
        # Si el usuario ya tiene un Local, no permitimos agregar otro
        if request.user.is_superuser==False:
            return False
        return super().has_add_permission(request)