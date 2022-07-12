from ReviewsApp.models import Review
from ReviewsApp.serializers import ReviewSerializer
from  django.http  import HttpResponse 

from django.core.files.storage import  default_storage
from rest_framework import viewsets




class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class =  ReviewSerializer

    def post(self,request, *args,**kwargs):
        rating  =  request.data['ReviewRating']
        body = request.data['ReviewBody']
        title  =  request.data['ReviewBook']

        Review.objects.create(ReviewBody=body, ReviewBook=title,ReviewRating= rating)

        return  HttpResponse({'message':'Review created'},  status=200)