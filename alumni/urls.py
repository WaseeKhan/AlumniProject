from django.urls import path
from . import views
#alumni/urls.py

urlpatterns = [
    path('',views.home,name='home'),
    path('alumnies/',views.alumnies,name='alumnies'),
    path('addalumni/',views.add_alumni_details,name='add_alumni_details'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('update_profile/<str:pk>/',views.updateProfile,name='updateProfile'),
]

