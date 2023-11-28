from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from base.models.Trabajadores import BaseTrabajador
from app.Forms.TrabajadorForm import TrabajadorForm


@login_required
def trabajador_list(request):
    trabajadores = BaseTrabajador.objects.all()
    return render(request, 'Trabajador.html',
                  {'trabajadores': trabajadores})



from django.db.models import Q

@login_required()
def buscar_trabajador(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = BaseTrabajador.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in BaseTrabajador._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = BaseTrabajador.objects.filter(q_objects)
    else:
        resultados = BaseTrabajador.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in BaseTrabajador._meta.fields]
    return render(request, 'Trabajador.html', {'resultados': resultados, 'campos': campos})


@login_required
def trabajador_detail(request, pk):
    trabajador = get_object_or_404(BaseTrabajador, pk=pk)
    return render(request, 'Trabajador.html',
                  {'trabajador': trabajador})
@login_required
def trabajador_new(request):
    if request.method == "POST":
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            trabajador = form.save()
            return redirect('Trabajador.html', pk=trabajador.pk)
    else:
        form = TrabajadorForm()
    return render(request, 'Trabajador.html',
                  {'form': form})

@login_required
def trabajador_edit(request, pk):
    trabajador = get_object_or_404(BaseTrabajador, pk=pk)
    if request.method == "POST":
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            trabajador = form.save()
            return redirect('trabajador_detail', pk=trabajador.pk)
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'Trabajador.html',
                  {'form': form})

@login_required
def trabajador_delete(request, pk):
    trabajador = get_object_or_404(BaseTrabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajadores')
    return render(request, 'Trabajador.html',
                  {'object': trabajador})
