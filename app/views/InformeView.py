from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from app.models.Informe import Informe


@login_required
def buscar_informe(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = Informe.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in Informe._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = Informe.objects.filter(q_objects)
    else:
        resultados = Informe.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in Informe._meta.fields]
    return render(request, 'Informe.html', {'resultados': resultados, 'campos': campos})
