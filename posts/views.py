from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    posts = Post.objects.filter(isPublish=True).order_by('-created_at')
    if request.method=='POST':
        if request.user.is_authenticated:
            postId= request.POST['postId']
            post = Post.objects.get(id = postId)
            if 'like' in request.POST:
                if request.user.profile in post.like.all():
                    post.like.remove(request.user.profile)
                    post.save()
                    return redirect('index')
                else:
                    post.like.add(request.user.profile)
                    post.dislike.remove(request.user.profile)
                    post.save()
                    return redirect('index')
            if 'dislike' in request.POST:
                if request.user.profile in post.dislike.all():
                    post.dislike.remove(request.user.profile)
                    post.save()
                    return redirect('index')
                else:
                    post.dislike.add(request.user.profile)
                    post.like.remove(request.user.profile)
                    post.save()
                    return redirect('index')

    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

 
@login_required(login_url='login')
def create(request):
    #formu sayfa ilk açıldıüında normal haliyle göstermek için
    form = PostForm()
    #sayfada çalıştırılan bir post methodu var mı?
    if request.method=='POST':
        #post methodu ile gönderilen formun içerisindeki bilgileri ve resimleri çekmek için
        form = PostForm(request.POST, request.FILES)
        #formun doğruluğunu kontrol etme
        if form.is_valid():
            #kaydetmeden önce form üzerinde değişiklik yapmak için commit=false ile kaydetme özelliğini devre dışı bıraktık
            post = form.save(commit=False)
            #postun owner bilgisini girişli kullanıcıya bağlama
            post.owner = request.user.profile
            #post kaydetme
            post.save()
            #mesaj
            messages.success(request, 'Postunuzu oluşturulmuştur. Denetlenildekten sonra yayınlanacaktır.')
            #yönlendirme
            return redirect('index')
    #form değişkeni içerisine tanımlanan formu html sayfada göstermek için önce context'e tanımlanır 
    #sonra render fonksiyonu içerisine ekler

    
    context = {
        'form':form
    }
    return render(request, 'create.html', context)

def detail(request, postId, slug):
    post= Post.objects.get(id= postId, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'detail.html', context)