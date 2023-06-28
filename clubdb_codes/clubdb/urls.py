"""clubdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index,name='index'),
    path('login',views.login,name="login"),
    path('Insertclub', views.Insertclub, name="Insertclub"),
    path('Insertevent', views.Insertevent, name="Insertevent"),
    path('showclub', views.showclub, name="showclub"),
    path('showevent', views.showevent, name="showevent"),
    path('EditClub/<int:id>',views.EditClub,name="EditClub"),
    path('updateclub/<int:id>', views.updateclub, name="updateclub"),
    path('DeleteClub/<int:id>',views.DeleteClub,name="DeleteClub"),
    path('EditEvent/<int:id>',views.EditEvent,name="EditEvent"),
    path('updateevent/<int:id>', views.updateevent, name="updateevent"),
    path('DeleteEvent/<int:id>',views.DeleteEvent,name="DeleteEvent"),
    path('runQueryClub',views.runQueryClub,name="runQueryClub"),
    path('sortclub',views.sortclub,name="sortclub"),
    path('sortevent',views.sortevent,name="sortevent"),
    path('showaddress',views.showaddress,name="showaddress"),
    path('sortaddress',views.sortaddress,name="sortaddress"),

    path('ProcessCustomQuery/', views.ProcessCustomQuery, name="ProcessCustomQuery"),
    path('InputCustomQuery/', views.InputCustomQuery, name="InputCustomQuery"),
]

