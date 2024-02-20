from django import forms
from apps.offer.models import Winer
from django.db.models import Q

class WinerForm(forms.ModelForm):
    class Meta:
        model = Winer
        fields = ['winer_name', 'winer_ci', 'winer_movil', 'promo']
        widgets = {
            'winer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre '}),
            'winer_ci': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Carnet'}),
            'winer_movil': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Movil'}),
            'promo': forms.Select(attrs={'class': 'form-control-none hidden-field'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        winer_ci = cleaned_data.get('winer_ci')
        winer_movil = cleaned_data.get('winer_movil')
        promo = cleaned_data.get('promo')
        
        if winer_ci and len(str(winer_ci)) !=  11:
            raise forms.ValidationError("El carnet debe tener exactamente  11 dígitos.")
        if winer_movil and len(str(winer_movil)) !=  8:
            raise forms.ValidationError("El número de móvil debe tener exactamente  8 dígitos.")
        if Winer.objects.filter(Q(winer_ci=winer_ci) | Q(winer_movil=winer_movil), promo=promo).exists():
            print('error')
            raise forms.ValidationError("Ya existe un ganador con el mismo carnet o número de celular en esta promoción.")

        return cleaned_data