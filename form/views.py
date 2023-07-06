from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class Auth(View):
    def get(self, request):
        return render(request, 'form/form.html')
    

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        User = authenticate(username=username, password=password)

        if User is None:
            return HttpResponse('User khong ton tai')
        
        login(request, User)
        return redirect('product')


class Product(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return HttpResponse('<h1>CÓ CÁI CON KẶC HAHAHAHA</h1>')