from django.urls import path, include
from . import views

app_name = 'learning_logs'
urlpatterns = [
	path('', views.index, name='index'),
	#全てのトピックを表示する
	path('topic/', views.topic, name='topic'),
	#個別トピックの詳細ページ
	path('topic/<int:topic_id>/', views.topic_child, name='topic_child'),
	#新しいトピック作成ページ
	path('new_topic/', views.new_topic, name='new_topic'),
	#新しい記事作成ページ
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	#ユーザーが追加した記事(entry)の編集ページ
	path('edit/<int:entry_id>/', views.edit, name='edit'),
]