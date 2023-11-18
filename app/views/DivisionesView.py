from django.shortcuts import render, get_object_or_404, redirect

from app.models.Division import Division
from app.Forms.DivisionForm import DivisionForm



def division_list(request):
    divisiones = Division.objects.all()
    return render(request, 'Division.html',
                  {'division': divisiones})

def division_detail(request, pk):
    division = get_object_or_404(Division, pk=pk)
    return render(request, 'Division.html',
                  {'division': division})

def division_new(request):
    if request.method == "POST":
        form = Division(request.POST)
        if form.is_valid():
            division = form.save()
            return redirect('Index.html', pk=division.pk)
    else:
        form = DivisionForm()
    return render(request, 'Division.html',
                  {'form': form})

def division_edit(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == "POST":
        form = DivisionForm(request.POST, instance=division)
        if form.is_valid():
            division = form.save()
            return redirect('division_detail', pk=division.pk)
    else:
        form = DivisionForm(instance=division)
    return render(request, 'Division.html',
                  {'form': form})

def division_delete(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == 'POST':
        division.delete()
        return redirect('division')
    return render(request, 'Division.html',
                  {'object': division})
