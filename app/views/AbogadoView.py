from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.Abogado import Abogado
from app.Forms.AbogadoForm import AbogadoForm

from autenticacion.views.IniciarSesion import login_required

@login_required
def abogado_list(request):
    abogados = Abogado.objects.all()
    return render(request, 'Abogado.html',
                  {'abogados': abogados})


@login_required()
def buscar_abogado(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = Abogado.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in Abogado._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = Abogado.objects.filter(q_objects)
    else:
        resultados = Abogado.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in Abogado._meta.fields]
    return render(request, 'Abogado.html', {'resultados': resultados, 'campos': campos})


@login_required
def abogado_new(request):
    if request.method == "POST":
        form = AbogadoForm(request.POST)
        if form.is_valid():
            abogado = form.save()
            return redirect('Abogado.html'
                            , pk=abogado.pk)
    else:
        form = AbogadoForm()
    return render(request, 'Abogado.html',
                  {'form': form})
@login_required
def abogado_edit(request, pk):
    abogado = get_object_or_404(Abogado, pk=pk)
    if request.method == "POST":
        form = AbogadoForm(request.POST, instance=abogado)
        if form.is_valid():
            abogado = form.save()
            return redirect('abogado_detail', pk=abogado.pk)
    else:
        form = AbogadoForm(instance=abogado)
    return render(request, 'Abogado.html',
                  {'form': form})
@login_required
def abogado_delete(request, pk):
    abogado = get_object_or_404(Abogado, pk=pk)
    if request.method == 'POST':
        abogado.delete()
        return redirect('abogado')
    return render(request, 'Abogado.html',
                  {'object': abogado})
