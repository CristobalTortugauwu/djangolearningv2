from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myview(request):
    #print(request.COOKIES)
    #oldval = request.COOKIES.get('visit', 0)
    #resp = HttpResponse('haz visitado es página=', str(oldval))
    #if oldval!=0:
    #    resp.set_cookie('visit', int(oldval)+1)
    #else:
    #    resp.set_cookie('visit', 1)        
    num_visitas = request.session.get('visit',0)+1
    resp = HttpResponse('haz visitado esta página='+str(num_visitas))
    resp.set_cookie('dj4e_cookie', '0e6a5ac6', max_age=1000)
    print(request.COOKIES)
    request.session['visit'] = num_visitas
    print(num_visitas)
    if num_visitas>4: del(request.session['visit'])        
    return resp