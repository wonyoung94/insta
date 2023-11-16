from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')

    context = {
        'posts':posts,
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form':form,
    }

    return render(request, 'form.html', context)

@login_required
def likes(request, id):
    user = request.user
    post = Post.objects.get(id=id)

    # 이미 좋아요 버튼을 누른 경우
    # if post in user.like_posts.all(): user가 좋아요 누른 목록들을 모두 조회 해서 그 중 post가 있으면, 
    if user in post.like_users.all(): # 좋아요가 있는 post에 해당 user가 있으면
        post.like_users.remove(user) # 하트를 제거 해주세요.
    else:
        post.like_users.add(user) # (post에 좋아요 한 user의 수를 add)
        # user.like_posts.add(post)로 써도 무방(user이 좋아요 한 post에 숫자를 add)



    return redirect('posts:index')

#3. detail, comment 기능 구현
@login_required
def detail(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()

    context = {
        'form': form,
        'post': post
    }

    
    return render(request, 'detail.html', context)

@login_required
def comment_create(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  
            comment.save()

            return redirect('posts:detail', post_id=post_id)
    else:
        form = CommentForm()

    return redirect('posts:detail', id=post_id)


@login_required 
def comment_delete(request, post_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()

    return redirect('posts:detail', id=post_id)

#20231114 수업
from django.http import JsonResponse

def likes_async(request, id):
    user = request. user
    post = Post.objects.get(id=id)

    if user in post.like_users.all():
        post.like_users.remove(user)
        status = False
    else:
        post.like_users.add(user)
        status = True

    context = {
        'status':status,
        'count': len(post.like_users.all())
    }

    return JsonResponse(context)