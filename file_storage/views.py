import os
from django.http import FileResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import File
from django.contrib.auth.models import User


@login_required
def file_list(request):
    files = File.objects.filter(user=request.user)
    return   render(request, 'file_list.html', {'files': files})

@login_required
def upload_file(request):
    if request.method == 'POST':
        new_file = File(user=request.user, file=request.FILES['file'])
        new_file.save()
        return redirect('files_storage:file_list')
    return render(request, 'upload_file.html')

@login_required
def download_file(request, file_id):
    file = File.objects.get(id=file_id)
    if file.user !=request.user:
        return JsonResponse("not authorised", safe= False)
    response = FileResponse(open(file.file.path, 'rb'))
    return response

@login_required
def delete_file(request, file_id):
    file = File.objects.get(id=file_id)
    if file.user !=request.user:
        return JsonResponse("not authorised", safe= False)
    file.delete()
    #with open(file.file.path)  as hfh:  i need to remove the file from disk also  this solution is not working, the above line file.delete() deltes the record of file from database only 
    #    os.remove(hfh)
    return redirect('files_storage:file_list')