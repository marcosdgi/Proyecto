from django.shortcuts import render, get_object_or_404, redirect

from app.models.DepartamentoLegal import DepartamentoLegal
from app.Forms.DepartamentoLegalForm import DepartamentoLegalForm



def departamentolegal_list(request):
    departamentolegal = DepartamentoLegal.objects.all()
    return render(request, 'DepartamentoLegal.html',
                  {'departamentolegales': departamentolegal})

def departamentolegal_detail(request, pk):
    departamentolegal = get_object_or_404(DepartamentoLegal, pk=pk)
    return render(request, 'DepartamentoLegal.html',
                  {'departamentolegal': departamentolegal})

def departamentolegal_new(request):
    if request.method == "POST":
        form = DepartamentoLegalForm(request.POST)
        if form.is_valid():
            departamentolegal = form.save()
            return redirect('DepartamentoLegal.html'
                            , pk=departamentolegal.pk)
    else:
        form = DepartamentoLegalForm()
    return render(request, 'DepartamentoLegal.html',
                  {'form': form})

def departamentolegal_edit(request, pk):
    departamentolegal = get_object_or_404(DepartamentoLegal, pk=pk)
    if request.method == "POST":
        form = DepartamentoLegalForm(request.POST, instance=departamentolegal)
        if form.is_valid():
            departamentolegal = form.save()
            return redirect('departamentolegal_detail', pk=departamentolegal.pk)
    else:
        form = DepartamentoLegalForm(instance=departamentolegal)
    return render(request, 'DepartamentoLegal.html',
                  {'form': form})

def departamentolegal_delete(request, pk):
    departamentolegal = get_object_or_404(DepartamentoLegal, pk=pk)
    if request.method == 'POST':
        departamentolegal.delete()
        return redirect('departamentolegal')
    return render(request, 'DepartamentoLegal.html',
                  {'object': departamentolegal})
