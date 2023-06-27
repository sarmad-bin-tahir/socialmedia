from api.views import CustomRegisterView, UserViewSet, GetUserData
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet, PostLikeUnlikeView
from rest_auth.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('get-user-details/', GetUserData.as_view()),
    path('register/', CustomRegisterView.as_view()),
    path('like-unlike/', PostLikeUnlikeView.as_view()),
    path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
         name='account_confirm_email'),
]
