from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('invite', views.invite),
    path('place-ships', views.placeShips),
    path('shoot', views.shoot),
    path('notify', views.notify),
    path('game-over', views.gameOver)
]