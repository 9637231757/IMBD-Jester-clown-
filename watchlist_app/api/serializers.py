from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = WatchList
        fields = "__all__" 
        
class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        
        model = StreamPlatform
        fields = "__all__" 
        
    
  
  
"""class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField() 
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # to update instance update data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('descripton', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance 
    
    # object level validation implemented 
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and description should be different!")
        else:
            return data
    
    # single field validation 
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too Short")
        else:
            return value  """
         
        
        