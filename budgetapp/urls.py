"""budgetapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from expensemanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('today/', views.TransactionTodayArchiveView.as_view(), name="today"),
    path('monthly/', views.monthlyView, name="monthly"),
    # path('<int:year>/<int:month>/', views.MonthArchiveView.as_view(), name='monthly'),
    path('create/', views.TransactionCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.TransactionUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', views.TransactionDeleteView.as_view(), name="delete"),
    
]
