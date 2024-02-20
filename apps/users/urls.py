from django.urls import path
from apps.users import views
from apps.locals import views_locals
urlpatterns = [
    path('', views.index, name='index'),
    path('local/<int:pk>', views_locals.local_detail, name='local'),
    path('product/<int:pk>', views_locals.product_detail, name='product'),
]
