from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.DepartamentoComercial import DepartamentoComercial
from app.Forms.DepartamentoComercialForm import DepartamentoComercialForm


@login_required()
def buscar_departamentocomercial(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = DepartamentoComercial.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in DepartamentoComercial._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = DepartamentoComercial.objects.filter(q_objects)
    else:
        resultados = DepartamentoComercial.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in DepartamentoComercial._meta.fields]
    return render(request, 'DepartamentoComercial.html', {'resultados': resultados, 'campos': campos})
