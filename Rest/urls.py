
from django.urls import path
from .views import *

urlpatterns = [
     path('get-all-data/', GetAllData.as_view()),
     path('all-data/', allAPI),
     path('get-fav-data/', GetFavData.as_view()),
     path('update_fav_data/<int:pk>', UpdateFavData.as_view()),
     path('post_model_data', PostModelData.as_view()),     
]