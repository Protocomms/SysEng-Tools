from django.urls import path

from . import views

app_name = 'requirements'

urlpatterns = [
    path('', views.RequirementIndex.as_view(), name='index'),
    path('<int:pk>/', views.RequirementDetail.as_view(), name='detail'),
	path('create', views.RequirementCreate.as_view(), name='create'),
    path('<int:pk>/edit/', views.RequirementUpdate.as_view(), name='edit')
]
