"""定义learning_lofs 的url模式"""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有的类型
    url(r'^topics/$', views.topics, name='topics'),
    # 特定类型的详细Case
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #添加新case 的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]
