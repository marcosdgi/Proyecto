from django.shortcuts import render, get_object_or_404, redirect

from app.models.Contrato import Contrato
from app.Forms.ContratoForm import ContratoForm



def contrato_list(request):
    contratos = Contrato.objects.all()
    return render(request, 'Contrato.html',
                  {'trabajadores': contratos})

def contrato_detail(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    return render(request, 'Contrato.html',
                  {'trabajador': contrato})

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