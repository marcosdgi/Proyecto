from django import forms
from app.models.Contrato import Contrato
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['id_contrato',
                  'id_trabajador',
                  'id_departamentolegal',
                  'descripcion']
        widgets = {
            'id_contrato':forms.NumberInput(),
            'id_trabajador':forms.NumberInput(),
            'descripcion':forms.TextInput(),
            'id_departamentolegal':forms.NumberInput(),

        }