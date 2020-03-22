from django.shortcuts import render,reverse, get_object_or_404
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from todolist_app.models import dolist
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse


def first(request):
    print(request.user.username)
    return render(request,'todolist_app/first.html')

def home(request):
    print(request.user.username)
    return render(request,'todolist_app/home.html')    

def Usertodolist(request):

    to = dolist.objects.filter(owner=request.user).order_by('-date_edited')
    context = {'todos':to}

    return render(request,'todolist_app/list.html',context)

class ToDoList_Detail(DetailView):
    model = dolist

class ToDoList_Add(LoginRequiredMixin, CreateView):
    model = dolist
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list')    



class ToDoList_Delete(LoginRequiredMixin, DeleteView):
    model = dolist
    success_url = '/home/list/'

class ToDoList_Update(LoginRequiredMixin, UpdateView):
    model = dolist
    fields = ['content']
    
