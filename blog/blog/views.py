from django.shortcuts import render

from apps.blogs.models import Blogs



def inicio(request):
    blogs = Blogs.objects.all()
    context={
        "blogs":blogs
    }
    return render(request,"inicio.html",context)