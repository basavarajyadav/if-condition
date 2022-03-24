from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'x':20}
    return render(request,'conditional.html',context=d)

def yadav(request):
    d1={'b':'raj'}
    return render(request,'cond.html',context=d1)
