from django.shortcuts import render
from rango.models import Category
from rango.models import Page


def index(request):
    
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'boldmessage':'Crunchy,creamy,cookie,candy,cupcake'}
   
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    context_dict = {'text':'This tutorial has been put together by Yuqi Li'}
    return render(request, 'about/about.html', context = context_dict)











