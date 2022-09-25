from random import choice
from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "content": util.get_entry(entry)
    })

def search(request):
    if request.method == 'POST':
        name = request.POST['q']
        names = util.search_entry(name)
        if type(names) == list:
            return render(request, "encyclopedia/search.html", {
            "names": names
            })
        else:
            return redirect(f'wiki/{name}')

def create(request):
    if request.method =='POST':
        title = request.POST['tile']
        content = request.POST['content']
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html")
        else:
            util.save_entry(title, content)
            return redirect(f'wiki/{title}')
    else:
        return render(request, "encyclopedia/create.html")

def edit(request,entry):
    if request.method == 'POST':
        content = request.POST['edit_content']
        util.save_entry(entry, content)
        return redirect('entry', entry=entry)
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": entry,
            "content": util.edit_entry(entry)
        })

def random(request):
    list_name = util.list_entries()
    entry = choice(list_name)
    print(entry)
    return redirect('entry', entry=entry)


        


