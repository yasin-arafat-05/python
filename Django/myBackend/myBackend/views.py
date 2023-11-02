from django.http import HttpResponse
from django.shortcuts import render

#homepage routes 
def homepage(request):
    return HttpResponse("This is my home page.")

#blog list routes (dynamic route)
def bloglist(request,data):
    return HttpResponse(f"data is : {data}")

#reder html file from django.shortcuts
def html(request):
    dict={
        'title':"HOME",
        'text':"Welcome To My Home Page",
        'clist':['PHP','JAVA','PYTHON'],
        'student_details':[
            {'name':'Yasin'},
            {'name':'Arafat'},
        ]
    }
    return render(request,"index.html",dict)
