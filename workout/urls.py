from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "FitLifeHub Admin"
admin.site.site_title = "FitLifeHub Admin Portal"
admin.site.index_title = "Welcome to FitLifeHub Portal"
urlpatterns = [
    # home
    path("index/", views.index, name="index"),
    # login & register
    path("", views.loginpage, name="loginpage"),
    path("", include("django.contrib.auth.urls")),
    path("logoutpage/", views.logout_user, name="logoutpage"),
    path("registerpage/", views.registerpage, name="registerpage"),
    # userprofile
    path("userprofilepage/", views.userprofilepage, name="userprofilepage"),
    # Workouts
    path("workoutpage/", views.workoutpage, name="workoutpage"),
    path("listpage/", views.listpage, name="listpage"),
    path("listpage/<str:exercise_name>/", views.listpage, name="listpage"),
    path("contentpage/<str:content_name>/", views.contentpage, name="contentpage"),
    # bmi
    path("bmipage/", views.bmipage, name="bmipage"),
    # diet pages
    path("diet_page/", views.dietpage, name="dietpage"),
    path("dietlists/", views.dietlist, name="dietlists"),
    path("dietlists/<str:diettype>/", views.dietlist, name="dietlists"),
    path("dietcontent/<str:name>/", views.dietcontent, name="dietcontent"),
    # Contact Page
    path("contactpage/", views.contactpage, name="contactpage"),
    # leaderboard
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
