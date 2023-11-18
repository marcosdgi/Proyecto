from django import forms
from base.models.BaseDepartamento import BaseDepartamento
class DepartamentoForm(forms.ModelForm):


    class Meta:
        model = BaseDepartamento
        fields = ['id',
                  'nombre',
                  'direccion',
                  'descripcion']
        widgets = {
            'id':forms.NumberInput(),
            'nombre':forms.TextInput(),
            'descripcion':forms.TextInput(),
            'direccion':forms.TextInput(),

        }