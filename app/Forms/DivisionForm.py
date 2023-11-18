from django import forms
from app.models.Division import Division

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['id',
                  'nombre',
                  'direccion',
                  'clasificacion']
        widgets = {
            'id':forms.NumberInput(),
            'nombre':forms.TextInput(),
            'clasificacion':forms.TextInput(),
            'direccion':forms.NumberInput(),

        }