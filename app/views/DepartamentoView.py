from django.shortcuts import render, get_object_or_404, redirect

from base.models.BaseDepartamento import BaseDepartamento
from app.Forms.DepartamentoForm import DepartamentoForm



def departamento_list(request):
    departamentos = BaseDepartamento.objects.all()
    return render(request, 'Departamento.html',
                  {'departamentos': departamentos})

def departamento_detail(request, pk):
    departamento = get_object_or_404(BaseDepartamento, pk=pk)
    return render(request, 'Departamento.html',
                  {'departamento': departamento})

def departamento_new(request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            departamento = form.save()
            return render(request,'Creado.html')
    else:
        form = DepartamentoForm()
    return render(request, 'Departamento.html',
                  {'form': form})

def departamento_edit(request, pk):
    departamento = get_object_or_404(BaseDepartamento, pk=pk)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            departamento = form.save()
            return redirect('departamento_detail', pk=departamento.pk)
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'Departamento.html',
                  {'form': form})

def departamento_delete(request, pk):
    departamento = get_object_or_404(BaseDepartamento, pk=pk)
    if request.method == 'POST':
        departamento.delete()
        return redirect('departamentoes')
    return render(request, 'Departamento.html',
                  {'object': departamento})
