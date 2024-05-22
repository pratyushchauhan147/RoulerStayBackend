from rest_framework import status
from django.shortcuts import render,HttpResponse
from django.contrib.auth import get_user_model,login,authenticate
from .models import Property, Booking
from .serializers import *
from .utils import verifymail,sendmail
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django.http import Http404
from rest_framework.response import Response
from rest_framework import views
from .permissions import IsOwnerOrReadOnly
# Create your views here.
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields = ('title', 'location','description','host__username')
    def perform_create(self, serializer):
        serializer.save(host=self.request.user)
class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self):
        # Check if the current user has is_ver set to True
        is_verified = self.request.user.is_ver
        # If is_ver is True, fetch all posts; otherwise, return an empty queryset
        return Property.objects.all() if is_verified else Property.objects.none()
    
    def handle_exception(self, exc):
        # Override the handle_exception method to customize the response for unverified users
        if isinstance(exc, Http404) and not self.request.user.is_ver:
            message = "You are not verified. Access to this post is not allowed."
            return Response({'detail': message}, status=status.HTTP_403_FORBIDDEN)

        return super().handle_exception(exc)
   
  
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Booking.objects.filter(guest=self.request.user)
    
    def perform_create(self, serializer):
        
        serializer.save(guest=self.request.user)
        booker=self.request.user.email
        from app.models import User
        x=User.objects.get(id=serializer.data["owner"])
        owner=x.email
        print(owner,booker)
        message1 ="RoulerStay \nThere is a Booking on Your Property :"+str(serializer.data["property"])+"\n \n from "+str(x.username)+" "+str(x.email)+" \n Check it on ....\n*note: these mails are just for testing purpose and no real bookings are done"
        message2 ="RoulerStay \n You Booked a Property :"+str(serializer.data["property"])+"\n \n Hosted by  "+str(self.request.user.username)+" "+str(owner)+" \n Check it on ....\n*note: these mails are just for testing purpose and no real bookings are done"
        sendmail("Team RoulerStay : Recived Booking",owner,message1) 
        sendmail("Team RoulerStay Booked aproperty",booker,message2) 
        
class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    
    def get_queryset(self):
        return Booking.objects.filter(guest=self.request.user)
    
class UserDetailsView(views.APIView):
    def get(self, request, token):
        user = get_user_model().objects.get(auth_token=token)
        return Response({
            'username': user.username,
            'is_host': user.is_host
        })

class ContactMessageCreateView(generics.ListCreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
     
        serializer.save(sender=self.request.user)
        message = serializer.data["message"]
        email1 = serializer.data["email1"]
        print(message)
        sendmail("Message from :"+str(self.request.user.username),email1,message) 


class VerifyMessageCreateView(generics.ListCreateAPIView):
    queryset = VerifyMessage.objects.all()
    serializer_class = verifyMessageSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
     
        serializer.save(reciver=self.request.user.email)
        message = serializer.data["message"]
        email1 = serializer.data["reciver"]
        print(message)
        verifymail("self.request.user.username",email1,message)    
 
def isverfied(request):
    from app.models import User
    x=User.objects.get(username=request.user.username)
    x.is_ver = True
    print(request.user)
    return HttpResponse("huh")
class UpdateUserVerificationView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        usser = self.request.user;
        print(usser)
        return self.request.user

class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

