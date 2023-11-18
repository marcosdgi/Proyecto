from django import forms
from app.models.Producto import Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id',
                  'id_suministador',
                  'descripcion',
                  'fecha_produccion']
        widgets = {
            'id':forms.NumberInput(),
            'id_suministador':forms.NumberInput(),
            'descripcion':forms.TextInput(),
            'fecha_produccion':forms.DateInput(),

        }