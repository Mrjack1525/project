from django.urls import path
from . import views

urlpatterns = [

    path('courses/',views.courses, name = 'courses'),
    path('contactpagecall/',views.contactpagecall,name='contactpagecall'),
    path('contactlogic/',views.contactlogic,name='contactlogic'),
    path('online_classes/', views.online_classes, name='online_classes'),
]
