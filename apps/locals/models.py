from django.db import models
from apps.users.models import User
from utils.validates.validates import validate_letters_numbers_and_spaces
from django.contrib import messages
from django.core.validators import MinLengthValidator, MaxValueValidator,MinValueValidator

# Create your models here.
# Local
class Local(models.Model):
    TYPE_CHOICES = [
        ('Restaurant', 'Restaurant'),
        ('Bar', 'Bar'),
        ('Café', 'Café'),
        ('Ice cream shop', 'Ice cream shop'),
        ('Pizza shop', 'Pizza shop'),

    ]
    type = models.CharField('Tipo de local',max_length=15,default='Restaurant' ,choices=TYPE_CHOICES, blank=False, null=False)
    local_name = models.CharField('Nombre del local',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    active = models.BooleanField('Activo', default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,blank=False, null= False)
    address = models.TextField('Direccion',default='AAA',blank=False, null= False)
    image = models.ImageField('Imagen',upload_to='locals', null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Local."""

        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        """Unicode representation of Local."""
        return f'{self.local_name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.user = self.user
        super(Local, self).save(*args, **kwargs)


# Categories of Local
class Category(models.Model):
    
    category_name = models.CharField('Nombre de la categoria', max_length=255, blank=False , null=False)
    local = models.ForeignKey(Local,on_delete=models.CASCADE, verbose_name='Local',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Category."""
        return self.category_name
    
# Product  
class Product(models.Model):
    """Model definition for Product."""
    
    product_name = models.CharField('Nombre del producto', max_length=255, blank=False , null=False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    active = models.BooleanField(default=True)
    discount = models.PositiveIntegerField('Descuento de %', default=0, blank=False, null=False)
    image = models.ImageField('Imagen', upload_to='product_image/', blank=True, null=True)
    stars= models.PositiveSmallIntegerField('Estrellas',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
            ],
        help_text='Number of stars between 1 and 5',  
        default=5,blank=False, null=False)
    category = models.ForeignKey(Category,related_name='productCategory', on_delete=models.CASCADE, verbose_name='Category',blank=False, null= False)
    # Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.product_name
    
    
    

class Aggregate(models.Model):
    """Model definition for Aggregate."""
    agregate_name = models.CharField('Nombre del agregado', max_length=255, blank=False , null=False)
    measurement_unit = models.CharField('Unidad de medida', max_length=50, blank=False , null=False)
    measurement_unit_quantity = models.DecimalField('cantidad en unidades de medida', max_digits=10,  decimal_places=2, blank= False, null= False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    product = models.ForeignKey(Product,related_name='agregateProduct', on_delete=models.CASCADE, verbose_name='Product',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Aggregate."""

        verbose_name = 'Agregado'
        verbose_name_plural = 'Agregados'

    def __str__(self):
        return f'id:{self.id} {self.agregate_name}. id:{self.product.id} Product {self.product.product_name}'


class Ingredient(models.Model):
    """Model definition for Ingredient."""
    ingredient_name = models.CharField('Nombre del ingrediente', max_length=255, blank=False , null=False)
    product = models.ForeignKey(Product,related_name='ingredientProduct', on_delete=models.CASCADE, verbose_name='Product',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Ingredient."""

        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return self.ingredient_name


class Gallery(models.Model):
    """Model definition for Gallery."""
    image = models.ImageField('Imagen del local', upload_to='local_gallery_image/', blank=False, null=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, verbose_name='Gallery',blank=False, null= False)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Gallery."""

        verbose_name = 'Galeria de imagenes'
        verbose_name_plural = 'Galeria de imagenes'

    def __str__(self):
        return f'Photo {self.id} of local {self.local.local_name}'
