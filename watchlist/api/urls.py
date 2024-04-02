from django.urls import path
from ..api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate

urlpatterns = [
    path('watch/', WatchListAV.as_view(), name='movie-list'),
    path('watch/<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
