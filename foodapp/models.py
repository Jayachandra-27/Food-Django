from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    image_food=models.ImageField(upload_to='uploads/%Y/%m%d', null=True, blank=True)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural='Category'

    def __str__(self):
        return self.category_name
    
class Menu(models.Model):
    item_name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    price=models.IntegerField()
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural='Menu'

    def __str__(self):
        return self.item_name
class Make(models.Model):
    item_p=models.ForeignKey(Menu,on_delete=models.CASCADE, null=True, blank=True)
    image_food=models.ImageField(upload_to='uploads/%Y/%m%d', null=True, blank=True)
    short_description=models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural='item description'

    def __str__(self):
        return self.item_p.item_name if self.item_p else "No Item"