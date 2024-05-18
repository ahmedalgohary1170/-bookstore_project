from django.urls import path
from .views import BookList,BookDetail,BookUpdate,BookCreate


urlpatterns = [
    path('list',BookList.as_view()),
    path('list/<int:pk>/',BookDetail.as_view()),
    path('list/<int:pk>/edit',BookUpdate.as_view()),
    path('list/create',BookCreate.as_view()),
]
