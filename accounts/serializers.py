from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review


class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = (
            'pk',
            'title', 
            'content', 
            'movie_title', 
            'rank'
            )

    like_reviews = ReviewSerializer(many=True)
    user_reviews = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = (
            'pk',
            'username',
            'like_reviews',
            'user_reviews',
        )