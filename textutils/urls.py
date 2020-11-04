from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index,name='HomeScreen'), 
    path('analyze',views.analyze,name="AnalyzeText"),
]
