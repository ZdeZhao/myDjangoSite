import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import ValidationError

# Create your views here.
from django.urls import reverse

import app
from app.forms import MomentForm


def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter.<h1>")


def moments_input(request):
    if request.method == 'POST':
        data = {
            'content': 'Please input the content',
            'user_name': '匿名',
            'kind': 'Python技术',
        }
        form = MomentForm(request.POST, initial=data)
        if form.has_changed():
            print('如下字段进行了修改：')
            for field in form.changed_data:
                print(field)
            if form.is_valid():
                moment = form.save()
                moment.save()
                return HttpResponseRedirect(reverse(app.views.welcome)) # reverse 视图全称方法
        # else:
        #     raise ValidationError("请修改后提交")
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'), {'form': form})