from django.urls import path, include
from .views import HomePageRender,Login, Register, Logout, SwimmerPage,Search, createswimmer, renderadd

urlpatterns = [
    path('', HomePageRender, name="Home"),
    path('Register', Register, name = 'Register'),
    path('Login', Login, name='Login'),
    path('Logout/', Logout, name='Logout'),
    path('Swimmer/<int:id>/', SwimmerPage, name='SingleSwimmer'),
    path('Search/', Search, name='Search'),
    path('Add/', renderadd, name="Add"),
    path('create/', createswimmer, name='create')
]