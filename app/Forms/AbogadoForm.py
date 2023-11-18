from django import forms
from app.models.Abogado import Abogado
class AbogadoForm(forms.ModelForm):
    class Meta:
        model = Abogado
        fields = ['id','nombre','primer_apellido',
                  'segundo_apellido','fecha_nacimiento'
                  ,'edad','annos_experiencia',
                  'ocupacion','id_departamento','division','direccion']
        widgets = {
            'id':forms.NumberInput(),
            'nombre':forms.TextInput(),
            'primer_apellido':forms.TextInput(),
            'segundo_apellido':forms.TextInput(),
            'fecha_nacimiento':forms.DateInput(),
            'edad':forms.NumberInput(),
            'años_experiencia':forms.NumberInput(),
            'ocupacion':forms.TextInput(),
            'id_departamento':forms.NumberInput(),
            'cantidad_contratos':forms.NumberInput(),
            'grado_academico':forms.TextInput(),
            'division':forms.TextInput(),
            'direccion':forms.TextInput(),

        }