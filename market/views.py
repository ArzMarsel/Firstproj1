from django.contrib.auth.models import User
from django.shortcuts import render
from django_rest.http import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product, Comment, Rating
from .serializers import ProductImageSerializer, RatingSerializer, CommentSerializer, ProfileSerializer
from .permissions import IsEditor


class MarketView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = []


class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []


class RatingView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = []


class RegistrationLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                    "user_id": user.id,
                    "message": "User registered successfully."
                }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


class CommentCreateView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsEditor]