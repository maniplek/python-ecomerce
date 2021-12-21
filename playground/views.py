from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view takes a request -> response // a request handler

'''
for View we can PuLL data from db
transform data 
send emails....

then we have to do a function that 
will return an HTTPRESPONNSE WITH a message 
and the we map this view to URL so,
when we get a request to dat ulr the function in view will be called 
'''
def say_hello(request):
    # return HttpResponse('helllo  world')
    
    return render(request, 'hello.html', {'name':'Maniple'})
    