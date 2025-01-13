from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('allchai/', views.all_chai, name="all_chai"),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
]
