from audioop import reverse
from contextlib import redirect_stderr
import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index</h1>")
def helo(request, id):
    print(id)
    return HttpResponse("<h1>Hello, %s</h1>" % id)

def about(request):
    return HttpResponse("<h1>About</h1>")

def get_projects(request):
    head = '''
    <head>
    <title>Create Project</title>
    # css
    <style>
    
            table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
        }
    </style>
    # bootstrap
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    # autores
    <meta name="author" content="mohamed">
    <meta name="description" content="project manager">
    <meta name="keywords" content="project manager">
       <meta charset="UTF-8">
    
    '''
    header = '''
    <header>
    <h1>Create Project</h1>
    </header>
    '''
    nav=''' <nav>
    <ul class="nav nav-tabs"> 
    <li class="nav-item"> 
    <a class="nav-link" href="{% url "home" %}">Home</a>
    </li> 
    <li class="nav-item">
    <a class="nav-link" href="{% url "about" %}">About</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "projects" %}">Projects</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "tasks" %}">Tasks</a>
    </li> 
    
                <li class="nav-item"> <a class="nav-link" href="{% url "project_tasks" id=project.id name=project.name %}">Tasks of project %s</a> </li>
    </ul> 
    </nav> '''
    main = '''
    <main>
    <table>
    <tr>
    <th>id</th>
    <th>name</th>
    <th>description</th>
    </tr>
    '''
    projects = Project.objects.all()
    for project in projects:
        main += '''
        <tr>
        <td><a href="/projects/%s">%s</a></td>
        <td>%s</td>
        <td>%s</td>
        </tr>
        ''' % (project.id, project.id, project.name, project.description)
    main += '''
    </table>
    </main>
    '''
    footer = '''
    <footer>
    <h3>footer</h3>
    </footer>
    '''
    body ='''
    <body>
    %s
    %s
    %s
    %s
    %s
    </body>
    '''% (head, header, nav, main, footer)
    html = '''
    <!DOCTYPE html>
    <html>
    %s
        %s
    </html>
    ''' % (head, body)
    return HttpResponse(html)
   
# path('projects/<int:id>', views.get_projects, name='project'),

def get_project(request, id): # <html> <head> <title>Project</title>  css style  bootstrap </head> <body> <h1>Project</h1> <nav> <ul class="nav nav-tabs"> <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li> </ul> </nav> <table> <tr> <th>id</th> <th>name</th> <th>description</th> </tr> <tr> <td><a href="/projects/%s">%s</a></td> <td>%s</td> <td>%s</td> </tr> </table> <h3>Tasks</h3> <table> <tr> <th>id</th> <th>name</th> <th>description</th> </tr> {% for task in tasks %} <tr> <td><a href="/tasks/%s">%s</a></td> <td>%s</td> <td>%s</td> </tr> {% endfor %} </table> <footer> <h3>Footer</h3> </footer> </body> </html> def get_project(request, id): # header header = ''' <h1>Project</h1> ''' # navigation nav=''' <nav> <ul class="nav nav-tabs"> <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li> </ul> </nav> ''' # table project = Project.objects.get(id=id) table = ''' <table> <tr> <th>id</th> <th>name</th> <th>description</th> </tr> <tr> <td><a href="/projects/%s">%s</a></td> <td>%s</td> <td>%s</td> </tr> </table> ''' % (project.id, project.id, project.name, project.description) # tasks tasks = Task.objects.filter(project=project) table += ''' <h3>Tasks</h3> <table> <tr> <th>id</th> <th>name</th> <th>description</th> </tr> ''' for task in tasks: table += ''' <tr> <td><a href="/tasks/%s">%s</a></td> <td>%s</td> <td>%s</td> </tr> ''' % (task.id, task.id, task.name, task.description) table += ''' </table> ''' # css style style = ''' <style> table, th, td { border: 1px solid black; border-collapse: collapse; } th, td { padding: 5px; } </style> ''' # footer footer = ''' <h3>Footer</h3> ''' # bootstrap bootstrap = ''' <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"> <script src="https
    project = Project.objects.get(id=id)
    title = "<title>Project</title>"
    css = "<style> table, th, td { border: 1px solid black; border-collapse: collapse; } th, td { padding: 5px; } </style>"
    bootstrap = ''' <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script> <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script> '''
    head =''' <head> %s %s %s </head> ''' % (title, css, bootstrap)
    header = ''' <header> <h1>Project</h1> </header> '''
    nav=''' <nav>
    <ul class="nav nav-tabs"> 
    <li class="nav-item"> 
    <a class="nav-link" href="{% url "home" %}">Home</a>
    </li> 
    <li class="nav-item">
    <a class="nav-link" href="{% url "about" %}">About</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "projects" %}">Projects</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "tasks" %}">Tasks</a>
    </li> 
    </ul> 
    </nav> '''
    info = ''' <h3>Project info</h3> '''
    # dos botones de editar y borrar  
    # table = 
    
# crear proyecto
def create_project(request):
    head = '''
    <head>
    <title>Create Project</title>
    # css
    <style>
    
            table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
        }
    </style>
    # bootstrap
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    # autores
    <meta name="author" content="mohamed">
    <meta name="description" content="project manager">
    <meta name="keywords" content="project manager">
       <meta charset="UTF-8">
    
    '''
    header = '''
    <header>
    <h1>Create Project</h1>
    </header>
    '''
    nav=''' <nav>
    <ul class="nav nav-tabs"> 
    <li class="nav-item"> 
    <a class="nav-link" href="{% url "home" %}">Home</a>
    </li> 
    <li class="nav-item">
    <a class="nav-link" href="{% url "about" %}">About</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "projects" %}">Projects</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "tasks" %}">Tasks</a>
    </li> 
    
                <li class="nav-item"> <a class="nav-link" href="{% url "project_tasks" id=project.id name=project.name %}">Tasks of project %s</a> </li>
    </ul> 
    </nav> '''
    form = '''
    <form action="/projects/create/" method="POST">
    {% csrf_token %}
    <table>
        <tr>
            <th>name</th>
            <td><input type="text" name="name" value=""></td>
        </tr>
    
</table>
<input type="submit" value="Create">
<input type="reset" value="Reset">
</form>
         '''
    footer = '''<footer> <p>Created by: mohamed</p> </footer>'''
    body = '''<body> %s %s %s %s %s </body>''' % (header, nav, form, footer)
    html = '''<html> %s %s </html>''' % (head, body)
    # finalizar el proceso de creacion del proyecto y redireccionar a la pagina de proyectos
    if request.method == 'POST':
        print("POST")
        name = request.POST.get('name')
        print(name)
        Project.objects.create(name=name)
        return redirect_stderr('projects')
    
    return HttpResponse(html)





def update_project(request, id):
    head = '''
    <head>
    <title>Update Project</title>
    # css
    <style>
    
            table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
        }
    </style>
    # bootstrap
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    # autores
    <meta name="author" content="mohamed">
    <meta name="description" content="project manager">
    <meta name="keywords" content="project manager">
       <meta charset="UTF-8">
    
    '''
    header = '''
    <header>
    <h1>Update Project</h1>
    </header>
    '''
    nav=''' <nav>
    <ul class="nav nav-tabs"> 
    <li class="nav-item"> 
    <a class="nav-link" href="{% url "home" %}">Home</a>
    </li> 
    <li class="nav-item">
    <a class="nav-link" href="{% url "about" %}">About</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "projects" %}">Projects</a>
    </li> <li class="nav-item">
    <a class="nav-link" href="{% url "tasks" %}">Tasks</a>
    </li> 
    </ul> 
    </nav> '''
  
    footer = '''<footer> <p>Created by: mohamed</p> </footer>'''
  # con js en el html hacer un alert de confirmacion de modificacion """
    alert = ''' 
    <script>
    function myFunction() {
        if(confirm("Confirm update")) {
            alert("Project updated");
        } else {
            alert("Project not updated");
        }
    }
'''
    form = '''

    <form action="/projects/update/%s/" method="POST">
    {% csrf_token %}
    <table>
        <tr>
            <th>name</th>
            <td><input type="text" name="name" value="%s"></td>
        </tr>
    
</table>
<input type="submit" value="Update" onclick="myFunction()">
<input type="reset" value="Reset">
</form>
         ''' % (id, Project.objects.get(id=id).name)
    body = '''<body> %s %s %s %s %s </body>''' % (header, nav, form, alert, footer)
    html = '''<html> %s %s </html>''' % (head, body)
    # finalizar el proceso de creacion del proyecto y redireccionar a la pagina de proyectos
    if request.method == 'POST':
        print("POST")
        name = request.POST.get('name')
        print(name)
        Project.objects.filter(id=id).update(name=name)
        return redirect_stderr('projects')
    
    return HttpResponse(html)
        





def get_tasks(request):
    # header
    header = '''
     <h1>Tasks</h1>
     
    '''
    # navigation
    nav='''
    <nav>
     <ul class="nav nav-tabs">
    <li class="nav-item"> <a class="nav-link" href="%s">Home</a> </li>
    <li class="nav-item"> <a class="nav-link" href="%s">About</a> </li>
    <li class="nav-item"> <a class="nav-link" href="%s">Projects</a> </li>
    <li class="nav-item"> <a class="nav-link" href="%s">Tasks</a> </li>
    </ul>
    </nav>
    ''' % ('{% url "home" %}', '{% url "about" %}', '{% url "projects" %}', '{% url "tasks" %}')
    # table
    tasks = Task.objects.all()
    table = '''
    <table>
        <tr>
            <th>id</th>
            <th>name</th>
            <th>project</th>
            <th>description</th>
        </tr>
    '''
    for task in tasks:
        table += '''
        <tr>
            <td><a href="/tasks/%s">%s</a></td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
        ''' % (task.id, task.id, task.name, task.project.name, task.description)
    table += '''
    </table>
    '''
    #    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
#        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    bootstrap = '''
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    '''

    # css style
    style = '''
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 5px;
        }
    </style>
    '''

    # footer
    footer = '''
    <h3>Footer</h3>
    '''
    head = '''
     <head>
        <title>Tasks</title>
        <!-- css-->
        %s
        <!-- bootstrap-->
        %s
    </head>
    
    ''' % (style, bootstrap)
    body = '''
    <body>
        %s
        %s
        %s
        %s
    </body>
    ''' % (header, nav, table, footer)
    html = '''
    <html>
        %s
        %s
    </html>
    ''' % (head, body)
    return HttpResponse(html)
    
def get_task(request, id):# info about task with id = id <html> <head> <title>Task</title>  css style  bootstrap </head> <body> <h1>Task</h1> <nav> <ul class="nav nav-tabs"> <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li> <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li> </ul> </nav> <table> <tr> <th>id</th> <th>name</th> <th>project</th> <th>description</th> </tr> <tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> </tr> </table> </body> </html>
    task = Task.objects.get(id=id)
    html = '''
    <html>
        <head>
            <title>Task</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 5px;
                }
            </style>
        </head>
        <body>
            <h1>Task</h1>
            <nav>
                <ul class="nav nav-tabs">
                <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "project_tasks" id=project.id name=project.name %}">Tasks of project %s</a> </li>
                </ul>
            </nav>
            <table>
                <tr>
                    <th>id</th>
                    <th>name</th>
                    <th>project</th>
                    <th>description</th>
                </tr>
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
            </table>
        </body>
    </html>
    ''' % (task.id, task.name, task.project.name, task.description)
    return HttpResponse(html)


# get_project_tasks(request, id) - info about all tasks of project with id = id
def get_project_tasks(request, id, name):
    project = Project.objects.get(id=id)
    tasks = project.task_set.all()
    # bouton create task of project with id = id top right height and width of 100px
    def create_task_l(nem):
        html = '''
        <div style="position: absolute; top: 0; right: 0; height: 100px; width: 100px;">
            <a href="{% url "create_task" id=project.id name= %s 
            %}"><button type="button" class="btn btn-primary">Create task</button></a>
              </div>
        '''% (name)
        return html
    html = '''
    <html>
        <head>
            <title>Tasks</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 5px;
                }
            </style>
        </head>
        <body>
            <h1>Tasks</h1>
            %s
            <nav>
                <ul class="nav nav-tabs">
                <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li>
                <li class="nav-item"> <a class="nav-link" href="{% url "project_tasks" id=project.id name=project.name %}">Tasks of project %s</a> </li>
                </ul>
            </nav>
            <table>
                <tr>
                    <th>id</th>
                    <th>name</th>
                    <th>project</th>
                    <th>description</th>
                </tr>
    ''' % (create_task_l(name), name)
    for task in tasks:
        html+= '''
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
        ''' % (task.id, task.name, task.project.name, task.description)
    html += '''
            </table>
        </body>
    </html>
    '''
    return HttpResponse(html)
# Create your views here. delete_project
# delete_project(request, id) - delete project with id = id
# as a page with a form with a button to delete the project
# with a confirmation message and with css styles and js scripts (bootstrap)
def delete_project(request, id):
    head = '''
    <html>
        <head>
            <title>Delete project</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 5px;
                }
            </style>
        </head>
        <body>
    '''
    project = Project.objects.get(id=id)
    body = '''
        <h1>Delete project</h1>
        <nav>
            <ul class="nav nav-tabs">
            <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "project_tasks" id=project.id name=project.name %}">Tasks of project %s</a> </li>
            </ul>
        </nav>
        <h3>Are you sure you want to delete project %s?</h3>
        <form action="{% url "delete_project" id=project.id %}" method="post">
            {% csrf_token %}
            <input class="btn btn-danger" type="submit" value="Delete">
        </form>
    ''' % (project.name, project.name)
    tail = '''
        </body>
    </html>
    '''
    if request.method == 'POST':
        project.delete()
        return HttpResponseRedirect(reverse('projects'))
    return HttpResponse(head + body + tail)

def create_task(request):
    head = '''
    <html>
        <head>
            <title>Create task</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 5px;
                }
            </style>
        </head>
        <body>
    '''
    body = '''
        <h1>Create task</h1>
        <nav>
            <ul class="nav nav-tabs">
            <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li>
            </ul>
        </nav>
        <form action="{% url "create_task" %}" method="post">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Name:</td>
                    <td><input type="text" name="name"></td>
                </tr>
                <tr>
                    <td>Description:</td>
                    <td><input type="text" name="description"></td>
                </tr>
                <tr>
                    <td>Project:</td>
                    <td>
                        <select name="project">
    '''
    projects = Project.objects.all()
    for project in projects:
        body += '''
                            <option value="%s">%s</option>
        ''' % (project.id, project.name)
        body += '''
                        </select>
                    </td>
                </tr>
            </table>
            <input class="btn btn-success" type="submit" value="Create">
        </form>
    '''
    tail = '''
    <footer>
    <p>Created by mohammad</p>
    </footer>
        </body>
    </html>
    '''
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        project_id = request.POST.get('project')
        project = Project.objects.get(id=project_id)
        task = Task(name=name, description=description, project=project)
        task.save()
        return HttpResponseRedirect(reverse('tasks'))
    return HttpResponse(head + body + tail)


def update_task( request, id):
    head = '''
    <html>
        <head>
            <title>Update task</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 5px;
                }
            </style>
        </head>
        <body>
    '''
    task = Task.objects.get(id=id)
    body = '''
        <h1>Update task</h1>
        <nav>
            <ul class="nav nav-tabs">
            <li class="nav-item"> <a class="nav-link" href="{% url "home" %}">Home</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "about" %}">About</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "projects" %}">Projects</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "tasks" %}">Tasks</a> </li>
            <li class="nav-item"> <a class="nav-link" href="{% url "project_tasks" id=task.project.id name=task.project.name %}">Tasks of project %s</a> </li>
            </ul>
        </nav>
        <form action="{% url "update_task" id=task.id %}" method="post">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Name:</td>
                    <td><input type="text" name="name" value="%s"></td>
                </tr>
                <tr>
                    <td>Description:</td>
                    <td><input type="text" name="description" value="%s"></td>
                </tr>
                <tr>
                    <td>Project:</td>
                    <td>
                        <select name="project">
                            ''' % (task.project.name, task.name, task.description)
    projects = Project.objects.all()
    for project in projects:
        if project.id == task.project.id:
            body += '''
                            <option value="%s" selected>%s</option>
            ''' % (project.id, project.name)
        else:
            body += '''
                            <option value="%s">%s</option>
            ''' % (project.id, project.name)
    body += '''
                        </select>
                    </td>
                </tr>
            </table>
            <input class="btn btn-success" type="submit" value="Update">
        </form>
    '''
    tail = '''
    <footer>
    <p>Created by mohammad</p>
    </footer>
        </body>
    </html>
    '''
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        project_id = request.POST.get('project')
        project = Project.objects.get(id=project_id)
        task.name = name
        task.description = description
        task.project = project
        task.save()
        return HttpResponseRedirect(reverse('tasks'))
    return HttpResponse(head + body + tail)