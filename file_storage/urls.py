from django.urls import path
from . import views
app_name = 'files_storage'
urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('delete/<int:file_id>', views.delete_file , name ='delete_file' )
]
