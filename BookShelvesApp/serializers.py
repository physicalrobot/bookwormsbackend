from  rest_framework  import serializers
from BookShelvesApp.models import BookShelf

class BookShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookShelf
        fields = ('BookShelfId',
        'user',
        'books',
        )
