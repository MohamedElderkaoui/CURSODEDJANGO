from django.http import HttpResponse, JsonResponse
from .models import project, task

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index</h1>")
def helo(request, id):
    print(id)
    return HttpResponse("<h1>Hello, %s</h1>" % id)

def about(request):
    return HttpResponse("<h1>About</h1>")

def project(request):
    p = list(project.objects.values())
    return JsonResponse(p, safe=False)

def task(request):
    return HttpResponse("<h1>Task</h1>")