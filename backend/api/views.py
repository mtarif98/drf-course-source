# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerialiser, UserSerialiser
from django.contrib.auth.models import User

# Create your views here.
class ArticleList(ListCreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerialiser


class ArticleDetail(RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerialiser
	permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerialiser
	permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerialiser
	permission_classes = (IsSuperUserOrStaffReadOnly,)