from django.shortcuts import render
from .models import Property
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
class PropertyViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving properties.
    """
    @method_decorator(cache_page(60 * 15))
    def property_list(self, request):
        contents = {
            "title": request.user.get_title()
            "description": request.user.get_description(),
            "price": request.user.get_price(),
            "location": request.user.get_location(),
            "created_at": request.user.get_created_at(),

        }
        return Response(contents)
      # Cache the response for 15 minutes
    
    
    
