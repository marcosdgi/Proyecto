from django import forms
from app.models.Director import Director
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['id','nombre','primer_apellido',
                  'segundo_apellido','fecha_nacimiento'
                  ,'edad','annos_experiencia',
                  'ocupacion','id_departamento','grado_adademico']
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
            'grado_academico':forms.TextInput(),

        }