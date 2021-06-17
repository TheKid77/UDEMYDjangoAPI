from rest_framework import serializers
from imdb_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_len_name(self, object):
        return len(object.name)

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description should be different!")
        return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value