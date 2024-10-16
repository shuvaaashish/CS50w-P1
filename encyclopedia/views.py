from django.shortcuts import render
import markdown2
import random
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def converter(title):
    things=util.get_entry(title)
    if things != None:
        converted=markdown2.markdown(things)
        return converted
    else:
        return None

def entry(request,title):
    info=converter(title)
    if info==None:
        return render(request,"Encyclopedia/err.html",{
                "err":"This page doesn't exist"
            })
    else:
        return render(request,"encyclopedia/entry.html",{
            "info":info,
            "title":title
            })

def search(request):
  if request.method == "POST":
    title = request.POST['q']
    entri = util.list_entries()
    lowercase_list = list(map(str.lower, entri))
    
    if title.lower() in lowercase_list:
        return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))
    
    else:
        recommendation = []
        for entry in entri:
            if title.lower() in entry.lower():
                recommendation.append(entry)
        
        if not recommendation:
            return render(request,"encyclopedia/err.html",{
                "err":"This page doesn't exist"})
        
        return render(request, "encyclopedia/search.html", {
            "recommendation": recommendation,
        })

def new(request):
    if request.method=="GET":
        return render(request, "encyclopedia/new.html")
    else:
        title= request.POST['title']
        content=request.POST['info']
        Exist=util.get_entry(title)
        if Exist != None:
            return render(request,"Encyclopedia/err.html",{
                "err":"This page already exists"
            })
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))
            
def edit(request):
    if request.method=='POST':
        title=request.POST['title']
        info=util.get_entry(title)
        return render(request,"encyclopedia/edit.html",{
            "title":title,
            "info":info
        })

def save(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['info']
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))

def rand(request):
    Entri=util.list_entries()
    title= random.choice(Entri)
    return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))
    
        
        
        