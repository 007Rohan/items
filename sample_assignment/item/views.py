from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import items
from .serializers import ItemSerializer
from datetime import datetime

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = items.objects.all()
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        self.serializer_class = ItemSerializer
        return super().list(request, *args, **kwargs)
    
    
    def retrive(self, request, *args, **kwargs):
        request_data = request.data
        self.queryset = self.queryset.filter(id = request_data.get('id'))
        return super().list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        request_data = request.data.copy()
        serializer_obj = self.serializer_class(data=request_data)
        if serializer_obj.is_valid():       
            serializer_obj.save()
            return Response(status=200,data={'status':'SUCCESS','data':serializer_obj.data})
        return Response(status=400,data={'status':'Failed','data':serializer_obj.errors})
    
    
    def put(self, request, *args, **kwargs):
        request_data = request.data.copy()
        item_obj = self.queryset.filter(id=request_data.get('id','')).first()
        request_data['updated_at'] = datetime.now()
        serializer_obj = self.serializer_class(item_obj,data=request_data)
        if serializer_obj.is_valid():       
            serializer_obj.save()
            return Response(status=200,data={'status':'SUCCESS','data':serializer_obj.data})
        return Response(status=400,data={'status':'Failed','data':serializer_obj.errors})
    
    
    def delete(self, request, *args, **kwargs):
        request_data = request.data
        item_obj = self.queryset.filter(id=request_data.get('id','')).first()
        item_obj.delete()
        return Response(status=200,data={'status':'SUCCESS','data':'item sucessfully deleted'})