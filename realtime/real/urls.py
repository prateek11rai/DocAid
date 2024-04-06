from django.urls import path
from .views import index
                    
urlpattens=[
    path('',index)
]