from msilib.schema import ServiceInstall
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review, Comment
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from .serializers.review import (
    ReviewListSerializer,
    ReviewSerializer
)
from .serializers.comment import (
    CommentSerializer
)



@api_view(['GET', 'POST'])
def review_list_or_create(request):

    def review_list():
        reviews = Review.objects.order_by('-pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    def review_create():
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, HTTP_201_CREATED)
    
    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return review_create()

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def review_update():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        
    def review_delete():
        if request.user == review.user:
            review.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        return review_update()
    elif request.method == 'DELETE':
        return review_delete()


@api_view(['POST'])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)

        # comments = review.comments.all()
        # serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def comment_update():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
    
    def comment_delete():
        if request.user == comment.user:
            comment.delete()
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()


@api_view(['POST'])
def comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        comment.like_users.add(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
