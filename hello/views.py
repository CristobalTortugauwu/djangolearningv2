from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myview(request):
    resp = HttpResponse('creando una cookie para el proyecto')
    resp.set_cookie('dj4e_cookie', '0e6a5ac6', max_age=1000)
    print(request.session)
    num_visitas = request.session.get('visit',0) + 1
    if num_visitas>4: del(request.session['visit'])        
    resp = HttpResponse('haz visitado esta página='+str(num_visitas))
    return resp