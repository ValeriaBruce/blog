from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import postForm
from .models import Post


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})

    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("blog")
            except:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "el usuario ya existe"},
                )

        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": "contrasena no coinciden"},
        )


def blogPrincipal(request):
    posts= Post.objects.all()
    return render(request, "blog.html",{'posts':posts})


def salir(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "usuario o contrasena incorrecto",
                },
            )
        else:
            login(request, user)
            return redirect("blog")


def createPost(request):
    if request.method == "GET":
        return render(request, "create_post.html", {"form": postForm})

    else:
        try:
            post = postForm(request.POST)
            new_post = post.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect("blog")
        except ValueError:
            return render(
                request,
                "create_post.html",
                {"form": postForm, "error": "datos incorrectos"},
            )
