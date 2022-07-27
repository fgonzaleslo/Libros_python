from django.urls import path
from . import views
from .views import ReporteExel,GeneratePdf,importar_libro
#gracias a path obtendremos la vista
urlpatterns = [
#URL LIBROS 
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>',views.editar, name='editar'),
    path('reporte_excel_libro/',ReporteExel.as_view(), name='reporte_excel_libro'),
    path('reporte_pdf_libro/',GeneratePdf.as_view(), name='reporte_pdf_libro'),
    #path('buscar',busqueda_libros, name='buscar'),
    #path('importar_csv/',import_csv, name='importar_csv')
    #path('libros/seleccionar', views.seleccionar, name='seleccionar'),
    # #URL AUTORES
    path('importar_libro/',importar_libro,name='importar_libro'),
    path('exportar_excel/',views.exportar_excel_reporte,name='exportar_excel'),


#URL AUTORES
    path('autores', views.autores, name='autores'),
    path('autores/crear_autor', views.crear_autor, name='crear_autor'),
    path('eliminar_autor/<int:id>',views.eliminar_autor, name='eliminar_autor'),
    path('autores/editar_autor/<int:id>',views.editar_autor, name='editar_autor'),
    path('exportar_csv/',views.exportar_csv_reporte,name='exportar_csv'),
] 
