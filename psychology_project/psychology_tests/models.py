from django.db import models

"""test category"""
class ProductTypes(models.Model):
    name = models.CharField(max_length=1000)
    
    class Meta:
        db_table = 'product_types'
    
    def __str__(self):
        return self.name
    
    
    """admin pass """
    """"admin@mail.com workready7"""  
    
    """rogin id"""
    """test@mail.com workready7"""
    
    
      
"""test detail"""
class Quiz(models.Model):
    title = models.CharField(max_length=1000)
    product_type = models.ForeignKey(
        ProductTypes, on_delete=models.CASCADE
    )
    # title = models.CharField(max_length=200)
    detail = models.TextField()
    template_name = models.CharField(max_length=100, default='default_quiz_template.html')  # デフォルトテンプレート名

    
    class Meta:
        db_table = 'quiz'
   
    def __str__(self):
        return self.title

    
"""test image"""
class ProductPictures(models.Model):
    picture = models.FileField(upload_to='product_pictures/')
    product = models.ForeignKey(
        Quiz, on_delete=models.CASCADE
    )
    # order = models.IntegerField()
    
    order = models.CharField(max_length=50, blank=True, null=True) 

    
    class Meta:
        db_table = 'product_pictures'
        ordering = ['order'] 
        
    def __str__(self):
        return self.product.name + ':' +str(self.order)
        
