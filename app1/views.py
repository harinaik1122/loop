from django.shortcuts import render

# Create your views here.
def homepage(request):
    D = {'a' : 20, 'b': 30}
    return render(request, 'homepage.html', context = D)



def loop(request):
    d={'a': 'PRAKASH'}
    return render(request,'loop.html',context=d)
