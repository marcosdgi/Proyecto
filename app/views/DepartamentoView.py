from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from base.models.BaseDepartamento import BaseDepartamento
from app.Forms.DepartamentoForm import DepartamentoForm


@login_required
def buscar_departamento(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = BaseDepartamento.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in BaseDepartamento._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = BaseDepartamento.objects.filter(q_objects)
    else:
        resultados = BaseDepartamento.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in BaseDepartamento._meta.fields]
    return render(request, 'Departamento.html', {'resultados': resultados, 'campos': campos})
