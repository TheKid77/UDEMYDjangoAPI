from rest_framework import serializers
from imdb_app.models import WatchList, StreamPlatform, Review
        
class ReviewSerializer(serializers.ModelSerializer):

    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review 
        # fields = "__all__"
        exclude = ('watchlist', 'active',)
        
class WatchListSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)
    # platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList 
        # fields = "__all__"
        exclude = ('active',)


class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)
    #  watchlist = serializers.StringRelatedField(many=True, read_only=True)
    #  watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )
    
    class Meta:
        model = StreamPlatform 
        fields = "__all__"


