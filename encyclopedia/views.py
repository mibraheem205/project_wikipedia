from django.shortcuts import render
from markdown2 import Markdown
from django.http import HttpResponse

from . import util

import re
import markdown2
import tkinter

from tkinter import messagebox


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "h1":"All Pages"
    })

def markdown2html(content):
        res = util.get_entry(content)
        return markdown2.markdown(res)

def entry(request1,name):
    return render(request1, "encyclopedia/entry.html",{
        "entry1": markdown2html(name),
        "title":name
    })

   

def get_query(request):
    qry = str(request.GET.get('q')).lower()
    entries_list = util.list_entries()
    for i in range(len(entries_list)):
        entries_list[i] = entries_list[i].lower()
    if qry != "":
        if qry in entries_list:
            return render(request, "encyclopedia/entry.html", {
                "entry1":markdown2html(qry),
                "title":qry.capitalize
            })

        else:
            entries_list2 = [x for x in entries_list if re.search(qry, x)]
            for i in range(len(entries_list2)):
                entries_list2[i] = entries_list2[i].capitalize()
            return render(request,"encyclopedia/index.html",{
                "entries": entries_list2,
                "h1": "You Might Search:"
            })
    else:
        return index(request)
      
def new_page(request):
    title = request.POST.get('title')
    content = request.POST.get('new_content')
    util.save_entry(title,content)
    #index(request) 
    return render(request,"encyclopedia/newpage.html",{

    })
