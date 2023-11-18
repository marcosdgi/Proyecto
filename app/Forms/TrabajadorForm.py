from django import forms
from base.models.Trabajadores import BaseTrabajador
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = BaseTrabajador
        fields = ['id','nombre','primer_apellido',
                  'segundo_apellido','fecha_nacimiento'
                  ,'edad','annos_experiencia',
                  'ocupacion','id_departamento']
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

        }