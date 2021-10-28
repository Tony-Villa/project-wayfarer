from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse('Yo yo')

class  Signup(View):
    def get(self,request):
        form = UserCreationForm():
        context = {"form":form}
        return render(request,'registration/signup.html',context)

    def post (self,request):
        form = UserCreationFrom(request.POST)
        if form.is_valid():
            user= form.save()
            login (request,user)
            return redirect ('profile.html')
        else:
            context = {"form":form}
            return render(request,"registrations/signup.html", context)