from django.shortcuts import render

from apps.blogs.models import Blogs



def inicio(request):
    blogs = Blogs.objects.all()
    context={
        "blogs":blogs
    }
    return render(request,"inicio.html",context)


def login(request):
    
    return render(request,"login.html")

def profile(request):
    context={
        "Usuario":"Nombre",
        "Mail":"mail@mail.com",
        "Blogs":"Aqui irian los blogs que hizo"
    }
    return render(request,"profile.html",context)
