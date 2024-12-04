from django.urls import path 
from .views import ( CategoryListCreateView , CategoryDetailView , ListCreatePostView , PostDetailView ,
 ListCreateCommentView , CommentDetailView )
urlpatterns = [
    path( 'api' , CategoryListCreateView.as_view() , name = 'ListCreate' ) ,
    path( 'api/<int:pk>' , CategoryDetailView.as_view() , name = 'Detail' ) ,
    path( 'api/posts' , ListCreatePostView.as_view() , name = 'ListCreatePost' ) ,
    path( 'api/posts/<int:pk>' , PostDetailView.as_view() , name = 'PostDetail' ) ,
    path( 'api/posts/<int:pk>/comments' , ListCreateCommentView.as_view() , name = 'CommentView' ) ,
    path( 'api/posts/<int:post_id>/<int:comment_id>' , CommentDetailView.as_view() , name = 'CommentDetail' ) ,
]
