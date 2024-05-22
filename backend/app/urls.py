from . import views
from django.urls import path

urlpatterns = [
    path('users/<str:token>/', views.UserDetailsView.as_view()),
    path('contactmessage/', views.ContactMessageCreateView.as_view()),
    path('verify/', views.VerifyMessageCreateView.as_view()),
    path('properties/', views.PropertyListCreateView.as_view()),
    path('isvertrue/', views.UpdateUserVerificationView.as_view()),

    path('properties/<int:pk>/', views.PropertyRetrieveUpdateDestroyView.as_view()),
    path('bookings/', views.BookingListCreateView.as_view()),
    path('bookings/<int:pk>/', views.BookingRetrieveUpdateDestroyView.as_view()),
    path('feedback/', views.FeedbackListCreateView.as_view()),

]
