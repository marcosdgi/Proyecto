from django import forms
from app.models.DepartamentoLegal import DepartamentoLegal
class DepartamentoLegalForm(forms.ModelForm):
    class Meta:
        model = DepartamentoLegal
        fields = ['id',
                  'nombre',
                  'direccion',
                  'descripcion',
                  'ano']
        widgets = {
            'id_contrato':forms.NumberInput(),
            'id_trabajador':forms.NumberInput(),
            'descripcion':forms.TextInput(),
            'id_departamentolegal':forms.NumberInput(),
            'ano':forms.DateInput(),
        }