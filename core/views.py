from django.shortcuts import redirect, render
from django.views import View


class ClassIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/base.html')
