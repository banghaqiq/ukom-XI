from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *

# Create your views here.

def beranda(request):
    listsiswa = Siswa.objects.all()
    context = {
        'siswa': listsiswa,
    }
    return render(request, 'views/beranda.html', context)

def person(request):
 return render(request, 'views/person.html')



# Fungsi untuk menampilkan detail data Siswa
def siswa_detail(request, pk):
    siswa = get_object_or_404(Siswa, pk=pk)
    return render(request, 'views/siswa_detail.html', {'siswa': siswa})

# Fungsi untuk menambah data Siswa baru
def siswa_new(request):
    if request.method == "POST":
        form = SiswaForm(request.POST)
        if form.is_valid():
            siswa = form.save()
            return redirect('/', pk=siswa.pk)
    else:
        form = SiswaForm()
    return render(request, 'views/siswa_edit.html', {'form': form})

# Fungsi untuk mengedit data Siswa
def siswa_edit(request, pk):
    siswa = get_object_or_404(Siswa, pk=pk)
    if request.method == "POST":
        form = SiswaForm(request.POST, instance=siswa)
        if form.is_valid():
            siswa = form.save()
            return redirect('/', pk=siswa.pk)
    else:
        form = SiswaForm(instance=siswa)
    return render(request, 'views/siswa_edit.html', {'form': form})

# Fungsi untuk menghapus data Siswa
def siswa_delete(request, pk):
    siswa = get_object_or_404(Siswa, pk=pk)
    if request.method == "POST":
        siswa.delete()
        return redirect('beranda')
    return render(request, 'views/siswa_delete.html', {'siswa': siswa})