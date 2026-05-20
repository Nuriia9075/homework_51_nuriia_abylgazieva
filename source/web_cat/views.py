from django.shortcuts import render, redirect
from .cat_logis import Cat
cat =None


# Create your views here.
def index(request):
    return render(request, 'index.html')

def cat_stats(request):
    global cat
    if request.method == 'POST':
        if 'cat_name' in request.POST:
            cat_name = request.POST.get('cat_name')
            if not cat_name:
                return redirect('/')
            else:
                cat = Cat(cat_name)
                return render(request, 'cat_stats.html', {'cat': cat})
        if 'action' in request.POST:
            if cat is None:
                return redirect('/')
            method_name = request.POST.get('action')
            if method_name == 'play':
                cat.play()
            elif method_name == 'feed':
                cat.feed()
            else: cat.sleep()
            return render(request, 'cat_stats.html', {'cat': cat})
    else: return redirect('/')
