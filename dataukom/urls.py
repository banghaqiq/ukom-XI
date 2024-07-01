from django.urls import path 
from . import views

urlpatterns = [
 path('', views.beranda, name='beranda'),
 path('person/', views.person, name='persons'),
 path('siswa/<int:pk>/', views.siswa_detail, name='siswa_detail'),
 path('siswa/new/', views.siswa_new, name='siswa_new'),
 path('siswa/<int:pk>/edit/', views.siswa_edit, name='siswa_edit'),
  path('siswa/<int:pk>/delete/', views.siswa_delete, name='siswa_delete'),
]