from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.pic_views import Pics, PicDetail
from .views.like_views import Likes, LikeDetail

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('pics/', Pics.as_view(), name='pics'),
    path('pics/<int:pk>/', PicDetail.as_view(), name='pic_detail'),
    path('likes/', Likes.as_view(), name='likes'),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like_detail')
]
