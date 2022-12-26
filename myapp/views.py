import json
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
    # Create your views here.
    p = project.objects.values()
    t= f'''<h1>Project</h1>
    <table>
    <tr>
    <th>Id</th>
    <th>Name</th>
    </tr>
    '''
    for i in p:
        t += f'''
        <tr>
        <td>{i['id']}</td>
        <td>{i['name']}</td>
        </tr>
        '''
    t += '</table>'
    return HttpResponse(t)

def task(request):# Create your views here.
    t = task.objects.values()
    