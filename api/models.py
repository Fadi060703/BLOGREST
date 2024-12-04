from django.db import models

# Create your models here.


class Category( models.Model ) :
    name = models.CharField( max_length = 20 , unique = True ) 
    def __str__( self ) :
        return self.name 
    

class Post( models.Model ) :
    title = models.CharField( max_length = 30 )
    content = models.TextField()
    category = models.ForeignKey( Category , on_delete = models.CASCADE , related_name = 'posts' ) 
    created_at = models.DateTimeField( auto_now_add = True )
    def __str__( self ) :
        return self.title
    

class Comment( models.Model ) :
    post = models.ForeignKey( Post , on_delete = models.CASCADE , related_name = 'comments' ) 
    content = models.TextField()
    created_at = models.DateTimeField( auto_now_add = True )