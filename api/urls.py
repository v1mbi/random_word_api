from django.urls import path
from .views import get_word , post_word , delete_all, get_n_words,get_definition, get_index

urlpatterns = [
    path('random/', get_word),
    path('post/', post_word),
    path('delete/', delete_all),
    path('random/<int:pk>', get_n_words),
    path('definition/<str:pk>',get_definition),
    path('',get_index,name="")
]