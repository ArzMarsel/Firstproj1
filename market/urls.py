from . import views
from django.urls import path

urlpatterns = [
    path('market/', views.MarketView.as_view(), name='market'),
    path('rating/', views.RatingView.as_view(), name='rating'),
    path('registrate/', views.RegistrationLogin.as_view(), name='registrate'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    path('comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('rating/create/', views.RatingCreateView.as_view(), name='rating_create'),
    path('market/create/', views.ProductCreateView.as_view(), name='create_product')
]