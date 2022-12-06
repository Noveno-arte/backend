from django.urls import path, include
from recetas import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/recetas/', views.RecetaList.as_view()),
    path('api/recetas/<int:pk>/', views.RecetaDetail.as_view()),
    path('api/receta/nueva', views.RecetaNueva.as_view())    
]

urlpatterns = format_suffix_patterns(urlpatterns)