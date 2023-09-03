from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData,name='get-data'),
    path('reviews/',views.getReviewData,name='get-review data'),
    path('add/',views.addItem,name='add-data'),
    path('revupdate/<str:pk>/',views.reviewUpdate,name='review-update'),
    path('revdelete/<str:pk>/',views.reviewDelete,name='review-delete'),
]

                                                                         