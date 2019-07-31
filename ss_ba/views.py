from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator # !!!새로 수정된 곳 (paginator 적용)
from .models import Write
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate
def new(request): # 상품 등록 페이지
    loggeduser = request.user.username #현재 로그인 중인 사용자 아이디
    return render(request, 'auction/new.html',{'loggeduser':loggeduser})


def create(request): # 상품 등록
    board = Write()
    board.title = request.POST['title']
    board.content = request.POST['content']
    if request.method == 'POST'and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        board.image = fs.url(filename)
    board.save()
    return redirect(reverse('main'))

def main(request): # 등록된 게시글 페이지 !!!새로 수정된 곳 (paginator 적용)
    post = Write.objects
    post_list = Write.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'post':post, 'posts':posts, 'a': request.user.is_authenticated}
    return render(request, 'auction/main.html', context)

def detail(request, id):
    post = get_object_or_404(Write, pk=id)
    post.lookup = post.lookup + 1
    post.save()
    context = {'post':post, 'a' : request.user.is_authenticated}
    return render(request, 'auction/detail.html', context)

def delete(request, id):
    post = Write.objects.get(pk=id)
    post.delete()
    return redirect(reverse('main'))

def edit(request, id):
    post = Write.objects.get(pk=id)
    if request.method == "POST":
        if request.FILES.get('image'):
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            post.image = fs.url(filename)
            post.title = request.POST.get('title')
            post.content = request.POST.get('description')
            post.save()
            return redirect('detail', id=id)
        else:
            post.title = request.POST.get('title')
            post.content = request.POST.get('description')
            post.save()
            return redirect('detail', id=id)
    else :
        return render(request, 'auction/edit.html', {'post':post})