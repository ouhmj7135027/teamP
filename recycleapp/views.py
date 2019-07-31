from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from .models import Category


def home(request):
    waste = Category.objects.all()
    search = request.GET.get('search', '')
    
    a = request.user.is_authenticated
    b = request.user.username
    
    if search:
        waste = waste.filter(waste_name__icontains=search)
        return render(request, 'recycleapp/board.html', {'Cate': waste})
    else :
        return render(request, 'recycleapp/home.html', {'a':a, 'b':b})

def board(request):
    content = {}
    waste = Category.objects.all()
    try:
        search = request.GET.get('search', '')
        if search:
            waste = waste.filter(waste_name__icontains=search)
            print(waste)
            return render(request, 'recycleapp/board.html', {'Cate': waste})
        else:
            content={'Cate':waste,"a" : request.user.is_authenticated, "b" : request.user.username}
    except:
        print('=2' *30)

        errMsg = "서버 오류입니다."
        content={'errMsg':errMsg,}

    return render(request, 'recycleapp/board.html', content)


def detail(request, id):
    post = get_object_or_404(Category, pk=id)
    return render(request, 'recycleapp/detail.html',{'post': post})


    