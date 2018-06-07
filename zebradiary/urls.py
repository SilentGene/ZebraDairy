'''定义zebradiary的URL模式'''

from django.urls import path
from . import views

app_name = 'zebradiary'
urlpatterns = [
	# 主页
	path('', views.index, name = 'index'),
	# 主题页
	path('topics/', views.topics, name = 'topics'),
	#特定主题的详情页
	path('<int:topic_id>/', views.topic, name = 'topic'),
	#添加新文章
	path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry')
]
