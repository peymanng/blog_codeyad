from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view() , name='post_list'),
]