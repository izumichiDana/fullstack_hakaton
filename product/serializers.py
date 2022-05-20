from rest_framework import serializers
from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'description', 'made_in', )

    def validate_name(self, name):
        if Product.objects.filter(slug=name.lower().replace(' ', '-')).exists():
            raise serializers.ValidationError('Product with such name already exists')
        return name

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.category:
            representation['category'] = instance.category.name
        representation['likes'] = instance.likes.all().count()
        action = self.context.get('action')
        if action == 'retrieve':
            # детализация
            representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        else:
            representation['comments'] = instance.comments.all().count()
        return representation

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['user'] = instance.user.email
        return representation