from rest_framework import serializers
from ..models import WatchList, StreamPlatform, Review

#MODEL SERIALIZERS
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail'
    )
    class Meta:
        model = StreamPlatform
        fields = "__all__"


    # def get_len_title(self, object):
    #     length = len(object.title)
    #     return length
        
    # #Object level validation
    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different")
    #     return data

    # #Field level validation
    # def validate_title(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

# #SERIALIZERS
# def title_length(value):
#     if len(value) < 5:
#         raise serializers.ValidationError("Title is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(validators=[title_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     #Object level validation
#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different")
#         return data

#     #Field level validation
#     # def validate_title(self, value):
        
#     #     if len(value) < 5:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     else:
#     #         return value