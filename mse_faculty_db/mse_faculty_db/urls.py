"""
URL configuration for mse_faculty_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from staff_data import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faculty-id/', views.FacultyIdView.as_view(), name='faculty_id_view'),
    path('accounts/', views.accounts_page, name='accounts_page'),
    path('faculty/<uuid:faculty_id>/', views.get_faculty_entries, name='get_faculty_entries'),
    path('', views.home, name='home'),
    path('input/', views.input_view, name='input_page'),
    path('run_script/', views.run_script, name='run_script'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
