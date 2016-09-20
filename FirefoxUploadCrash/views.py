from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

import time
import random


class ReceiveFiles(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ReceiveFiles, self).dispatch(*args, **kwargs)

    def options(self, request, *args, **kwargs):
        return HttpResponse()

    def post(self, request):
        # do some work
        time.sleep(random.random() * 0.1)
        return HttpResponse()
