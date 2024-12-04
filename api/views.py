from django.shortcuts import render , get_object_or_404
from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category , Post , Comment
from .serializers import CategorySerializer , PostSerializer , CommentSerializer
# Create your views here.


class CategoryListCreateView( APIView ) :
    serializer_class = CategorySerializer 
    def get( self , request : Request ) :
        categories = Category.objects.all()
        serializer = self.serializer_class( categories , many = True ) 
        response = {
            'message' : 'Categories' , 
            'data' : serializer.data 
        }
        return Response( data = response , status = status.HTTP_200_OK )
    
    def post( self , request : Request ) :
        serializer = self.serializer_class( data = request.data ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'Category Created' ,
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED )
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )

class CategoryDetailView( APIView ) :
    serializer_class = CategorySerializer
    
    def get( self , request : Request , pk : int ) :
        category = get_object_or_404( Category , pk = pk ) 
        serializer = self.serializer_class( category ) 
        response = {
            'message' : 'Category' ,
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , pk : int ) :
        category = get_object_or_404( Category , pk = pk ) 
        serializer = self.serializer_class( category , data = request.data ) 
        if serializer.is_valid():
            serializer.save()
            response = {
                'message' : 'Category Updated' ,
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_200_OK )
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
    def delete( self , request : Request , pk : int ) :
        category = get_object_or_404( Category , pk = pk ) 
        category.delete()
        response = {
            'message' : 'Category Deleted' , 
            'data' : pk 
        }
        return Response( data = response , status = status.HTTP_410_GONE ) 
    
class ListCreatePostView( APIView ) :
    serializer_class = PostSerializer
    def get( self , request : Request ) :
        category_name = request.query_params.get( 'category' , None ) 
        search = request.query_params.get( 'search' , None ) 
        posts = Post.objects.all() 
        
        if category_name :
            posts = posts.filter( category__icontains = category_name )
        if search :
            posts = posts.filter( title__icontains = search )
        serializer = self.serializer_class( posts , many = True ) 
        response = {
            'message' : 'Posts In Category' ,
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def post( self , request : Request ) :
        serializer = self.serializer_class( data = request.data ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'updated' , 
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED )
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
class PostDetailView( APIView ) :
    serializer_class = PostSerializer 
    
    def get( self , request : Request , pk : int ) :
        post = get_object_or_404( Post , pk = pk ) 
        serializer = self.serializer_class( post ) 
        response = {
            'message' : 'post' ,
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , pk : int ) :
        post = get_object_or_404( Post , pk = pk ) 
        serializer = self.serializer_class( post , data = request.data ) 
        if serializer.is_valid() :
            serializer.save()
            response = {
                'message' : 'updated' ,
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_200_OK ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
    def delete( self , request : Request , pk : int ) :
        post = get_object_or_404( Post , pk = pk ) 
        post.delete()
        response = {
            'message' : 'deleted' ,
            'data' : pk 
        }
        return Response( data = response , status = status.HTTP_410_GONE ) 
    
class ListCreateCommentView( APIView ) :
    serializer_class = CommentSerializer
    def get( self , request : Request , pk : int ) :
        post = get_object_or_404( Post , pk = pk ) 
        serializer = self.serializer_class( post.comments , many = True ) 
        response = {
            'message' : 'comments on post' ,
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK )
    
    def post( self , request : Request , pk : int ) :
        post = get_object_or_404( Post , pk = pk ) 
        serializer = self.serializer_class(post , data = request.data ) 
        if serializer.is_valid() :
            serializer.save(  )
            response = {
                'message' : 'comment added' ,
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_201_CREATED ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST )
    
    
class CommentDetailView( APIView ) :
    serializer_class = CommentSerializer 
    def get( self , request : Request , post_id : int , comment_id : int ) :
        post = get_object_or_404( Post , post_id ) 
        comment = get_object_or_404( post , comment_id ) 
        serializer = self.serializer_class( comment ) 
        response = {
            'message' : 'comment' ,
            'data' : serializer.data
        }
        return Response( data = response , status = status.HTTP_200_OK ) 
    
    def put( self , request : Request , post_id : int , comment_id : int ) :
        post = get_object_or_404( Post , post_id ) 
        comment = get_object_or_404( post , comment_id ) 
        serializer = self.serializer_class( comment , data = request.data ) 
        if serializer.is_valid() :
            serializer.save() 
            response = {
                'message' : 'updated' ,
                'data' : serializer.data
            }
            return Response( data = response , status = status.HTTP_200_OK ) 
        return Response( data = serializer.errors , status = status.HTTP_400_BAD_REQUEST ) 
    
    def delete( self , request : Request , post_id : int , comment_id : int ) :
        post = get_object_or_404( Post , post_id )
        comment = get_object_or_404( post , comment_id ) 
        comment.delete()
        response = {
            'message' : 'deleted' , 
            'data' : comment_id
        }