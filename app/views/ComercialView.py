from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.Comercial import Comercial
from app.Forms.ComercialForm import ComercialForm


@login_required
def comercial_list(request):
    comerciales = Comercial.objects.all()
    return render(request, 'Comercial.html',
                  {'comerciales': comerciales})
@login_required()
def buscar_comercial(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = Comercial.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in Comercial._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = Comercial.objects.filter(q_objects)
    else:
        resultados = Comercial.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in Comercial._meta.fields]
    return render(request, 'Comercial.html', {'resultados': resultados, 'campos': campos})

@login_required
def comercial_new(request):
    if request.method == "POST":
        form = ComercialForm(request.POST)
        if form.is_valid():
            comercial = form.save()
            return redirect('Comercial.html', pk=comercial.pk)
    else:
        form = ComercialForm()
    return render(request, 'Comercial.html',
                  {'form': form})
@login_required
def comercial_edit(request, pk):
    comercial = get_object_or_404(Comercial, pk=pk)
    if request.method == "POST":
        form = ComercialForm(request.POST, instance=comercial)
        if form.is_valid():
            comercial = form.save()
            return redirect('comercial_detail', pk=comercial.pk)
    else:
        form = ComercialForm(instance=comercial)
    return render(request, 'Comercial.html',
                  {'form': form})
@login_required
def comercial_delete(request, pk):
    comercial = get_object_or_404(Comercial, pk=pk)
    if request.method == 'POST':
        comercial.delete()
        return redirect('comerciales')
    return render(request, 'Comercial.html',
                  {'object': comercial})
