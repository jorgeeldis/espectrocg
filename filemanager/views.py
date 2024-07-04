import os
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.conf import settings
from datetime import datetime

# Create your views here.
def index(request):
    base_path = settings.MEDIA_ROOT
    folders = ["pdf", "csv", "png"]
    list_of_files = []

    for folder in folders:
        path = os.path.join(base_path, folder)
        dir_list = os.listdir(path)

        for file_name in dir_list:
            file_path = os.path.join(path, file_name)
            normal_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            file_info = {
                "name": file_name,
                "size": os.path.getsize(file_path),
                "date": normal_date,
                "type": folder.upper()
            }
            list_of_files.append(file_info)

    return render(request, "main.html", {"files": list_of_files})


def about(request):
    return render(request, "about.html", {"name": "John Doe"})


# En tu archivo views.py
# @csrf_exempt
def subir_documento(request):
    if request.method == "POST":
        print(request.FILES)
        form = DocumentForm(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DocumentForm()
    return render(request, "upload_document.html", {"form": form})
