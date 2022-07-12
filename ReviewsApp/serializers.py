from  rest_framework  import serializers
from ReviewsApp.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('ReviewId',
        'ReviewBook',
        'ReviewBody',
        'ReviewRating')