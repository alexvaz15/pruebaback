from django.urls import  path, re_path

from Datos import views

urlpatterns = [
    re_path(r'^datosModel_url', views.DatosModelView.as_view()),
    path('datos_get', views.DatosModelView.as_view()),
    path('datos_delete/<slug:id>', views.DatosModelView.as_view()),
    path('datos_edit/<slug:id>', views.DatosModelView.as_view())
]

