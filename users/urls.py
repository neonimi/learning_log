"""users用URLパターン定義"""

from django.urls import path, include
from . import views

# Create your views here.
app_name = 'users'

urlpatterns = [
	#デフォルトの認証URLを取り込む
	path('', include('django.contrib.auth.urls')),
	#ログアウト
	path('logout/', views.logout, name='loggedout'),
	#ユーザー登録ページ
	path('register/', views.register, name='register'),
]