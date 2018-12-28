from django.urls import path, include
from . import views

app_name = 'maskingapp'

urlpatterns = [
    path('', views.index, name='index'),
    url('dialog/', include('censor_app.dialog.urls')),
]
