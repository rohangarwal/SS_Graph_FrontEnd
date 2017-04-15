# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
 # howdy/views.py
from django.views.generic import TemplateView

sys.path.insert(0, '/home/rohan/Desktop/sample_debug_folder/')
import sample

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'base.html', context=None)


def debug_ajax(request):
    input_data = request.GET.get('input_data', None)
    data_ = sample.foo()
    #print 'inside debug_ajax'
    ret_data = { 'working' : True,
                 'data_' : data_ }
    return JsonResponse(ret_data)
