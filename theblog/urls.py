from django.urls import path
from .views import HomeView, details,createview,update,delete,categoryform,article_category,like_view,commentview
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>/', details.as_view(), name='details'),
    # path('profile_details/<int:pk>/', profile_view.as_view(), name='profile_view'),
    path('addpost/', createview.as_view(), name='create'),
    path('details/<int:pk>/addcomment/', commentview.as_view(), name='comments'),
    path('category/', categoryform.as_view(), name='category'),
    path('update/<int:pk>/', update.as_view(), name='update'),
    path('article_category/<str:cats>/', article_category, name='Article-category'),
    path('delete/<int:pk>/', delete.as_view(), name='delete'),
    path('like/<int:pk>/', like_view, name='like'),
]