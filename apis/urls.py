from django.urls import path
from .views import *
urlpatterns = [
    path("vakan/",VakanListAPIVIEW.as_view(),name="vakan"),
    path("vakans/<int:pk>",VakanRetrieveUpdateDestroyAPIView.as_view(),name="vakans"),
    path("createvakan",VakanCreateAPIVIEW.as_view(),name="createvakan"),
    path("detailvakan/<int:pk>",VakanRetrieveAPIView.as_view(),name="detailvakan"),
    path("updatevakan/<int:pk>",VakanRetrieveUpdateAPIView.as_view(),name="updatevakan"),
    path("deletevakan/<int:pk>",VakanDestroyAPIView.as_view(),name="deletevakan"),
    
    # Worker
    path("worker",WorkerListAPIVIEW.as_view(),name="worker"),
    path("createworker",WorkerCreateAPIVIEW.as_view(),name="createworker"),
    path("detailworker/<int:pk>",WorkerRetrieveAPIView.as_view(),name="detailworker"),
    path("updateworker/<int:pk>",WorkerRetrieveUpdateAPIView.as_view(),name="updateworker"),
    path("deleteworker/<int:pk>",WorkerDestroyAPIView.as_view(),name="deleteworker"),
    path("workers/<int:pk>",WorkerRetrieveUpdateDestroyAPIView.as_view(),name="workers"),
]