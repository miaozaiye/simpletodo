from django.shortcuts import render,redirect,Http404,HttpResponse
from todo.models import TodoItem
from todo.form import NewForm,DoneForm
# Create your views here.

def index(request):
    todo_new = TodoItem.objects.filter(item_status = 'new')
    todo_done = TodoItem.objects.filter(item_status = 'done')
    context = {}
    context['todo_new'] = todo_new
    context['todo_done'] = todo_done
    context['count_new'] = todo_new.count()
    context['count_done'] = todo_done.count()

    index_page = render(request,'index.html',context)
    return index_page

def new(request):
    form = NewForm(request.POST)
    newitem = form['item'].value()
    newtodo = TodoItem(item = newitem,item_status = 'new')
    newtodo.save()
    return redirect(to = 'index')

def done(request):
    form = DoneForm(request.POST)
    doneid = form['id'].value()
    print('id is:',doneid)
    print('form is :', form)

    donetodo = TodoItem.objects.get(id = doneid)
    print ('donetodo is:',donetodo.item)
    donetodo.item_status='done'
    donetodo.save()

    return redirect(to='index')