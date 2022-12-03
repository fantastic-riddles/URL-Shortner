"""update_view module defines the UpdateView view"""

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.generic import View
from shortner.models import Link
from django.shortcuts import render
import json



def login_test(request: HttpRequest):
    """put handles updating requests"""
    # import pdb; pdb.set_trace()
    # special_code = data["special_code"]
    return render(request, 'homepages/index.html', {})

def signup_test(request: HttpRequest):
    return render(request, 'test.html', {})