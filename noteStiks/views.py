from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login, NewRegister
from .models import Users

# Create your views here.
data = {
    'appTitle' : 'MyStiky'
}
def index(request):
    return render(request, "index.html", data)

def signin(request):
    form = Login(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Pass']

            all_users = Users.objects.all()

            if len(all_users) != 0:
                for user in all_users:
                    if user.Email == email:
                        if user.Pass == password:
                            data = {
                                "title" : 'Signin',
                                "username" : user.Email,
                                "password" : user.Pass
                            }
                            #return render(request, "login.html", data)
                            return HttpResponse(f"{user.Email} and {user.Pass}")
                        else:
                            return HttpResponse("Your password is incorrect!!")
                    else:
                        return HttpResponse("Your username and password incorrect!!")
            else:
                return HttpResponse(f"{len(all_users)} database is emplty")
        else:
            return HttpResponse("Invalid data")
    else:
        return HttpResponse("<h3>Invalid Method</h3>")
    

def signup(request):
    form = NewRegister(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            full_name = form.cleaned_data['FullName']
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Pass']

            all_users = Users.objects.all()

            for user in all_users:
                if user.Email == email:
                    return HttpResponse(f"{full_name} already exist!!")
            else:
                new_obj = Users(FullName=full_name,Email=email,Pass=password)
                new_obj.save()
                return HttpResponse("Signup success!!")
                     
            #return render(request, "login.html", data)
        else:
            return HttpResponse("Invalid data")
    else:
        return HttpResponse("<h3>Invalid Method</h3>")