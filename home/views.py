from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Slot , Category
from django.views.generic import CreateView,View , DetailView
from home.forms import SlotForm
from users.models import CustomUser
from django.contrib.auth.models import User
from typing import Any


def index(request):
    posts = Slot.objects.all()
    categories = Category.objects.all()
    return render(request,'home/slotss.html', context={'posts':posts , 'categories':categories})

class CreateSlotVeiw(CreateView):
    template_name ='home/creat_post.html'
    form_class = SlotForm
    def form_valid(self,form):
       
        data = form.data
        post= Slot(name=data.get('name'),link=data.get('link'),size=data.get('size'),price=data.get('price'), category_id = data.get('category'))
        
        post.author = self.request.user
        # post.category=Category.objects.get(pk=data.get('category'))
        post.save()
        return redirect('index')
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryView(DetailView):
    model = Category
    template_name = 'home/category.html'
    context_object_name = 'category'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['slots'] = Slot.objects.filter(category=kwargs['object'])
        return context