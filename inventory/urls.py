from django.urls import path
from .views import BookList,BookDetail,BookUpdate,BookCreate
from . import api

urlpatterns = [
    path('',BookList.as_view()),
    path('<int:pk>/',BookDetail.as_view()),
    path('<int:pk>/edit',BookUpdate.as_view()),
    path('list/create',BookCreate.as_view()),

    # api
    path('api/list' , api.BookListAPI.as_view()),
    path('api/list/<int:pk>' , api.BookDetailAPI.as_view()),
]
