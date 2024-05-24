from django.urls import path
from .views import BookList,BookDetail,BookUpdate,BookCreate,DeleteBook
from . import api
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('api',api.CreateUpdateDetailDelete)

urlpatterns = [

    path('',BookList.as_view()),
    path('<int:pk>/',BookDetail.as_view()),
    path('<int:pk>/edit',BookUpdate.as_view()),
    path('<int:pk>/delete',DeleteBook.as_view()),
    path('list/create',BookCreate.as_view()),

    # api
#     path('api/list' , api.BookListAPI.as_view()),
#     path('api/list/<int:pk>' , api.BookDetailAPI.as_view()),
]


urlpatterns += router.urls