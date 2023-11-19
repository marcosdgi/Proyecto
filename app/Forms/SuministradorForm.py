from django import forms
from app.models.Suministrador import Suministrador
class SuministradorForm(forms.ModelForm):
    class Meta:
        model = Suministrador
        fields = ['id','nombre','nombre_calle',
                  'numero_calle','municipio'
                  ,'provincia','clasificacion',
                  ]
        widgets = {
            'id':forms.NumberInput(),
            'nombre':forms.TextInput(),
            'nombre_calle':forms.TextInput(),
            'numero_calle':forms.NumberInput(),
            'años_experiencia':forms.NumberInput(),
            'municipio':forms.TextInput(),
            'id_departamento':forms.NumberInput(),

        }