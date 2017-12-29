from django.conf.urls import url
from . import views

# 这个如果不加的话会报错：django.urls.exceptions.NoReverseMatch: 'blog' is not a registered namespace
app_name = "post"

# 为每一个应用创建单独的urls.py文件是最好的方法，可以保证你的应用能给别的项目再度使用
urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),  # 旧的列表页
    # url(r'^$', views.PostListView.as_view(), name='post_list'),
    # year：需要四位数
    # month：需要两位数。不及两位数，开头带上0，比如 01，02
    # day：需要两位数。不及两位数开头带上0
    # post：可以由单词和连字符组成
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
]
