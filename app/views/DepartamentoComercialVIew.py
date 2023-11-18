from django.shortcuts import render, get_object_or_404, redirect

from app.models.DepartamentoComercial import DepartamentoComercial
from app.Forms.DepartamentoComercialForm import DepartamentoComercialForm



def departamentocomercial_list(request):
    departamentocomercial = DepartamentoComercial.objects.all()
    return render(request, 'departamentocomercial.html',
                  {'departamentocomerciales': departamentocomercial})

def departamentocomercial_detail(request, pk):
    departamentocomercial = get_object_or_404(DepartamentoComercialForm, pk=pk)
    return render(request, 'DepartamentoComercial.html',
                  {'departamentocomercial': departamentocomercial})

def departamentocomercial_new(request):
    if request.method == "POST":
        form = DepartamentoComercialForm(request.POST)
        if form.is_valid():
            departamentocomercial = form.save()
            return redirect('DepartamentoComercial.html'
                            , pk=departamentocomercial.pk)
    else:
        form = DepartamentoComercialForm()
    return render(request, 'DepartamentoComercial.html',
                  {'form': form})

def departamentocomercial_edit(request, pk):
    departamentocomercial = get_object_or_404(DepartamentoComercial, pk=pk)
    if request.method == "POST":
        form = DepartamentoComercialForm(request.POST, instance=departamentocomercial)
        if form.is_valid():
            departamentocomercial = form.save()
            return redirect('departamentocomercial_detail', pk=departamentocomercial.pk)
    else:
        form = DepartamentoComercialForm(instance=departamentocomercial)
    return render(request, 'DepartamentoComercial.html',
                  {'form': form})

def departamentocomercial_delete(request, pk):
    departamentocomercial = get_object_or_404(DepartamentoComercial, pk=pk)
    if request.method == 'POST':
        departamentocomercial.delete()
        return redirect('departamentocomercial')
    return render(request, 'DepartamentoComercial.html',
                  {'object': departamentocomercial})
