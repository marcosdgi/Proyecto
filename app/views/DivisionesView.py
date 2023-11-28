from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.Division import Division
from app.Forms.DivisionForm import DivisionForm


@login_required()
def buscar_division(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = Division.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in Division._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = Division.objects.filter(q_objects)
    else:
        resultados = Division.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in Division._meta.fields]
    return render(request, 'Division.html', {'resultados': resultados, 'campos': campos})
