from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('search' , views.SearchView.as_view() , name='search'),
    path('post/<slug:slug>' , views.detail_view , name='post_detail'),
    path('category/<slug>' , views.CategoryPostList.as_view() , name='posts_by_category'),
    path('tags/<slug>',views.TagsPostListView.as_view(),name='posts_by_tag')
]