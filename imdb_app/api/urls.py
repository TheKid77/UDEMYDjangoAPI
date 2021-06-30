from django.urls import path, include

# from imdb_app.api.views import movie_list, movie_details
from rest_framework.routers import DefaultRouter
from imdb_app.api.views import (ReviewList, ReviewDetail, ReviewCreate, WatchListAV, 
                                WatchDetailAV, StreamPlatformVS, StreamPlatformAV, 
                                StreamPlatformDetailAV, UserReview, WatchList)


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),   
#    path('list2/', WatchList.as_view(), name='watch-list'),    
    
    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    # FILTERING
    # path('review/<str:username>', UserReview.as_view(), name='user-review-detail'),

    # FILTERING VIA QUERY PARAM
    path('reviews/', UserReview.as_view(), name='user-review-detail'),

]