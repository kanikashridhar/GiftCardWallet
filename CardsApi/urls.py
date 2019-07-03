from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='mysignup'),
    path('cardDetails/', views.CardsView.as_view(), name='cardDetails'),
    path('cardDetails/<int:pk>', views.SingleCardView.as_view(),name='updatecard'),
    path('products/', views.ProductsListView.as_view(), name='Productdetails'),
    path('exportCSV/', views.getzipfiles, name='ExportCSV'),
    path('login/', TemplateView.as_view(template_name="login.html"),name='login'),
    path('user-details/',TemplateView.as_view(template_name="user_details.html"),name='user-details'),

]