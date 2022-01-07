from django.http.response import Http404
from django.shortcuts import redirect, render

# Create your views here.
def login(request):
    flag = False
    if request.method == 'POST':
        name = request.POST['email']
        secret = request.POST['password']
        
        #print(f"Email : {name}, and Secret : {secret}")
        if name == "rajat@gmail.com" and secret == "Rajat@26560":
            return redirect('home/')
        else:
            flag = True

    context = {'flag': flag}
    return render(request, 'login.html', context)

def home(request):
    return render(request, 'home.html')