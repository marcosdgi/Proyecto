from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.Contrato import Contrato
from app.Forms.ContratoForm import ContratoForm


@login_required
def contrato_list(request):
    contratos = Contrato.objects.all()
    return render(request, 'Contrato.html',
                  {'trabajadores': contratos})
@login_required
def buscar_contrato(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = Contrato.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in Contrato._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = Contrato.objects.filter(q_objects)
    else:
        resultados = Contrato.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in Contrato._meta.fields]
    return render(request, 'Contrato.html', {'resultados': resultados, 'campos': campos})

def contrato_new(request):
    if request.method == "POST":
        form = ContratoForm(request.POST)
        if form.is_valid():
            contrato = form.save()
            return redirect('Index.html', pk=contrato.pk)
    else:
        form = ContratoForm()
    return render(request, 'Contrato.html',
                  {'form': form})

def contrato_edit(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == "POST":
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            trabajador = form.save()
            return redirect('trabajador_detail', pk=contrato.pk)
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'Contrato.html',
                  {'form': form})

def contrato_delete(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        contrato.delete()
        return redirect('trabajadores')
    return render(request, 'Contrato.html',
                  {'object': contrato})