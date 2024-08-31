
from django.urls import path
from app import views
urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact'),
  
  path('insert', views.insertData, name='insertData'),
  path('update/<id>', views.deleteData, name='deleteData'),
  path('delete/<id>', views.updateData, name='updateData'),
  
  
  
    
    
]
