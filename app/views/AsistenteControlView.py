from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.AsistenteControl import AsistenteControl
from app.Forms.AsistenteControlForm import AsistenteControlForm


@login_required
def asistente_list(request):
    asistentes = AsistenteControl.objects.all()
    return render(request, 'AsistenteControl.html',
                  {'asistentees': asistentes})
@login_required()
def buscar_asistente(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = AsistenteControl.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in AsistenteControl._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = AsistenteControl.objects.filter(q_objects)
    else:
        resultados = AsistenteControl.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in AsistenteControl._meta.fields]
    return render(request, 'AsistenteControl.html', {'resultados': resultados, 'campos': campos})


@login_required
def asistente_new(request):
    if request.method == "POST":
        form = AsistenteControlForm(request.POST)
        if form.is_valid():
            asistente = form.save()
            return redirect('AsistenteControl.html', pk=asistente.pk)
    else:
        form = AsistenteControlForm()
    return render(request, 'AsistenteControl.html',
                  {'form': form})
@login_required
def asistente_edit(request, pk):
    asistente = get_object_or_404(AsistenteControl, pk=pk)
    if request.method == "POST":
        form = AsistenteControlForm(request.POST, instance=asistente)
        if form.is_valid():
            asistente = form.save()
            return redirect('asistente_detail', pk=asistente.pk)
    else:
        form = AsistenteControlForm(instance=asistente)
    return render(request, 'AsistenteControl.html',
                  {'form': form})
@login_required
def asistente_delete(request, pk):
    asistente = get_object_or_404(AsistenteControl, pk=pk)
    if request.method == 'POST':
        asistente.delete()
        return redirect('asistentees')
    return render(request, 'C:/Users/Developer/Desktop/proyecto/app/templates/AsistenteControl.html',
                  {'object': asistente})
