from django.urls import path
# from .views import playlist, create_play, get_play
from .views import PlayList, CreatePlay, GetPlay, MainPlayView


urlpatterns = [
    path('list', PlayList.as_view()),
    path('create', CreatePlay.as_view()),
    path('<int:id>', GetPlay.as_view()),
    path('add_main', MainPlayView.as_view()),
]