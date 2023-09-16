from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 250)
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    description = serializers.CharField(max_length = 500)
