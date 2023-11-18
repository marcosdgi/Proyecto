from django import forms
from app.models.DepartamentoComercial import DepartamentoComercial
class DepartamentoComercialForm(forms.ModelForm):
    class Meta:
        model = DepartamentoComercial
        fields = ['id',
                  'nombre',
                  'direccion',
                  'descripcion',
                  'codigo',
                  'fecha_comunicacion',
                  'id_DepartamentoLegal',]
        widgets = {
            'id_contrato':forms.NumberInput(),
            'id_trabajador':forms.NumberInput(),
            'id_DepartamentoLegal':forms.NumberInput(),
            'descripcion':forms.TextInput(),
            'codigo':forms.TextInput(),
            'id_departamentolegal':forms.NumberInput(),
            'fecha_comunicacion':forms.DateInput(),

        }