from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.


def loginpage(request):
    if request.method == "POST":
        username = request.POST["usernameId"]
        password = request.POST["passwordId"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # checks if user has streak already or create streak if not
            streak, created = Streak.objects.get_or_create(user=user)

            current_date = date.today()

            # check if last login is today or not
            if streak.last_login_date != current_date:
                # check if last login date was less than 1 day ago
                if streak.last_login_date < current_date - timedelta(days=1):
                    streak.count = 1
                else:
                    streak.count += 1

                # Update last login date
                streak.last_login_date = timezone.now().date()
                streak.save()
            else:
                pass

            return redirect("index")
        else:
            messages.success(request, ("Wrong Login Details"))
            return redirect("loginpage")
    else:
        return render(request, "loginpage.html")


def logout_user(request):
    logout(request)
    return redirect("index")


@login_required
def userprofilepage(request):
    user = request.user
    try:
        streakcount = Streak.objects.get(user=user).count
    except Streak.DoesNotExist:
        streakcount = 0

    profile = {"user": user, "streakcount": streakcount}
    context = {"profile": profile}
    return render(request, "userprofile.html", context)


def registerpage(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpage")
    else:
        form = UserRegistrationForm()
    return render(request, "registerpage.html", {"form": form})


def leaderboard(request):
    streaks = Streak.objects.order_by("-count")
    return render(request, "leaderboard.html", {"streaks": streaks})


def index(request):
    return render(request, "index.html")


def workoutpage(request):
    exercises = Exercise.objects.all()
    return render(request, "workoutpage.html", {"exercises": exercises})


def listpage(request, exercise_name=None):
    if exercise_name:
        exerciselists = Excercisepost.objects.filter(typeexercise=exercise_name)
        heading = str(exercise_name)
        return render(
            request, "lists.html", {"exerciselists": exerciselists, "heading": heading}
        )
    else:
        exerciselists = Excercisepost.objects.all()
        return render(request, "lists.html", {"exerciselists": exerciselists})


def contentpage(request, content_name):
    contentpost = Excercisepost.objects.filter(name=content_name)
    exerciselists = Excercisepost.objects.all()
    return render(
        request,
        "content.html",
        {"contentpost": contentpost, "exerciselists": exerciselists},
    )


def bmipage(request):
    return render(request, "bmi.html")


# diet pages
def dietpage(request):
    diets = DietCat.objects.all()
    return render(request, "diet_page.html", {"diets": diets})


def dietlist(request, diettype=None):
    if diettype:
        dietposts = DietPosts.objects.filter(typeName=diettype)
    else:
        dietposts = DietPosts.objects.all()

    return render(request, "dietlists.html", {"dietposts": dietposts})


def dietcontent(request, name):
    dietdata = DietPosts.objects.filter(name=name)
    return render(request, "dietcontent.html", {"dietdata": dietdata})


# Contact


def contactpage(request):
    if request.method == "POST":
        name = request.POST.get("nameId")
        email = request.POST.get("emailId")
        desc = request.POST.get("descId")
        comment = Contact(
            name=name,
            email=email,
            desc=desc,
        )
        comment.save()
        return redirect("index")
    return render(request, "contactpage.html")
