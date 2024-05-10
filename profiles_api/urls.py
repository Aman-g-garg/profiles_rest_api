from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSets, base_name = 'hello_viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello_api/',views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),  # Token Obtain Pair View
    path('', include(router.urls)),
]