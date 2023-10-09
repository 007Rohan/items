import uuid

from django.db import models


class items(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    item_name = models.CharField(max_length=30,null=False)
    item_body = models.CharField(max_length=300,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.item_name
                
    class Meta:
        db_table = 'items'