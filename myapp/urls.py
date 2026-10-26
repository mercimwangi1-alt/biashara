from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.error_404_view, name='error_404'),
    path('blog-details/', views.details, name='blog-details'),
    path('starter/', views.starter, name='starter'),
    path('blog/', views.blog, name='blog'),
    path('portfolio-details/', views.portfolio, name='portfolio-details'),
    path('services-details/', views.services, name='services-details'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),   
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.Edit, name='edit'),
]

