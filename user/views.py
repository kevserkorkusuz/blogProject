from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from posts.models import *

# Create your views here.
def like(request):
    postId= request.POST['postId']
    post = Post.objects.get(id = postId)
    if 'like' in request.POST:
        if request.user.profile in post.like.all():
            post.like.remove(request.user.profile)
            post.save()
        else:
            post.like.add(request.user.profile)
            post.dislike.remove(request.user.profile)
            post.save()
    if 'dislike' in request.POST:
        if request.user.profile in post.dislike.all():
            post.dislike.remove(request.user.profile)
            post.save()
        else:
            post.dislike.add(request.user.profile)
            post.like.remove(request.user.profile)
            post.save()


def userRegister(request):
    username = ''
    name=''
    surname=''
    email=''

    if request.method == 'POST':
        username =request.POST['username']
        email =request.POST['email']
        name =request.POST['name']
        surname =request.POST['surname']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if password1== password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Bu kullanıcı adı zaten alınmış.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Bu email zaten alınmış.')
            elif len(password1)<6:
                messages.error(request, 'Şifreniz en az 6 karakter olmalıdır.')
            elif username.lower() in password1:
                messages.error(request, 'Şifrenizi kullanıcı adınızı kullanamazsınız.')
            else:
                user=User.objects.create_user(username=username, email=email, password= password1)
                user.save()
                Profile.objects.create(
                    user=user,
                    name=name,
                    surname=surname
                )
                messages.success(request, 'Başarıyla Kayıt Oldunuz!')
                return redirect('index')
        else:
            messages.error(request, 'Şifreleriniz Uyuşmuyor.')
    context = {
        'username': username,
        'email': email,
        'name': name,
        'surname': surname
    }
    return render(request, 'user/register.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Giriş Yapıldı.")
            return redirect('index')
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı.")
            return redirect('login')
    return render(request, 'user/login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('index')

def profile(request, slug):
    profil = Profile.objects.get(slug=slug)
    paylasim =Post.objects.filter(owner = profil)
    begen = Post.objects.filter(like__in = [profil])
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'takip' in request.POST:
                hesabim = Profile.objects.get(user = request.user)
                if Profile.objects.filter(slug=slug, followers__in = [hesabim]).exists():
                    profil.followers.remove(hesabim)
                    hesabim.follow.remove(profil)
                    messages.success(request, f'{profil.user.username} kullanıcısını takip etmeyi bıraktınız')
                    return redirect('profile', slug=slug)
                else:
                    profil.followers.add(hesabim)
                    hesabim.follow.add(profil)
                    messages.success(request, f'{profil.user.username} kullanıcısını takip etmeye başladınız')
                    return redirect('profile', slug=slug)
            elif 'sil' in request.POST:
                postId= request.POST['postId']
                post = Post.objects.get(id = postId)
                post.delete()
                messages.success(request, 'Paylaşım Silindi')
                return redirect('profile', slug=slug)
            
            else:
                like(request)
                return redirect('profile', slug=slug)
        else:
            messages.error(request, 'Lütfen giriş yapınız')
            return redirect('login')

    context = {
        'profil' : profil,
        'paylasim': paylasim,
        'begen' : begen
    }
    return render(request, 'user/profile.html', context)

@login_required(login_url='login')
def update(request):
    myUser = request.user
    myProfile = request.user.profile
    form = UserForm(instance= myUser) #bilgilerini göstermek istediğimiz kullnıcıyı instance olarak belirtiyoruz
    profilForm = ProfilForm(instance= myProfile)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = myUser)
        profilForm = ProfilForm(request.POST, request.FILES, instance= myProfile)
        if form.is_valid() and profilForm.is_valid():
            form.save()
            profilForm.save()
            messages.success(request, 'Profiliniz Güncellendi.')
            return redirect('profile', slug=myProfile.slug)

    context = {
        'form': form,
        'profilForm': profilForm
    }
    return render(request, 'user/update.html', context)

@login_required(login_url='login')
def reset(request):
    myUser=request.user 
    if request.method == 'POST':
        eski = request.POST['eski']
        yeni = request.POST['yeni']
        confirm = request.POST['confirm']

        user = authenticate(request, username=request.user, password =eski)
        if user is not None:
            if yeni==confirm:
                myUser.set_password(yeni)
                myUser.save()
                messages.success(request, 'Şifreniz Güncellendi!')
                return redirect('login')

        else: 
            messages.error(request, 'Mevcut şifre hatalı!')
    return render(request, 'user/password.html')