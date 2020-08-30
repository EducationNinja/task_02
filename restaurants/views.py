from django.shortcuts import render

def my_view(request):
    context = {
        "msg": "Hello World!"
    }
    return render(request, "hello.html", context)