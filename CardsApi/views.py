from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics
from .models import Card,Product
from .serializers import ProductSerializer,CardSerializer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
import csv
import io,os
from zipfile import ZipFile ,ZIP_DEFLATED


from rest_framework.views import APIView
from rest_framework.response import Response

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CardsView(generics.ListCreateAPIView):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        user = self.request.user
        return Card.objects.filter(User=user)
  
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

class SingleCardView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows single card to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ProductsListView(generics.ListCreateAPIView):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#class ExportCards(object):
def ExportCards(request):
    
    # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv; charset=UTF-8')
        response['Content-Disposition'] = 'attachment; filename="cards.csv"'

        writer = csv.writer(response)
        writer.writerow(['number','product_name','value','is_archived'])
        writer.writerows(Card.objects.filter(User=request.user).values_list('VoucherNum','Product__name','CardValue','IsArchived'))

        return response


def getzipfiles(request):
 
    
    fieldnames = ('number','product_name','value','is_archived')
    filename = request.user.username + "_cards"

    zip_file = ZipFile("carddetails.zip", 'w',ZIP_DEFLATED)
    
    '''
    #with ZipFile("carddetails.zip", 'w') as zip_file:
    string_buffer = io.StringIO()
    csvwriter = csv.writer(string_buffer)
    #csvwriter = csv.DictWriter(string_buffer, delimiter=',',fieldnames=fieldnames)
    csvwriter.writerow(['number','product_name','value','is_archived'])
    #csvwriter.writeheader()
    csvwriter.writerows(Card.objects.filter(User=request.user).values_list('VoucherNum','Product__name','CardValue','IsArchived'))
    #cdrdata =  Card.objects.filter(User=request.user).values_list('VoucherNum','Product__name','CardValue','IsArchived')
    #for row in cdrdata:
    #    csvwriter.writerow(row)
    '''

    string_buffer = io.StringIO()
    csvwriter = csv.DictWriter(string_buffer, delimiter=',', fieldnames=['number','product_name','value','is_archived'])
    csvwriter.writeheader()
    cards = Card.objects.filter(User=request.user).values_list('VoucherNum','Product__name','CardValue','IsArchived')
    print(cards)
    #for card in cards:
    #    print(card)
    #    csvwriter.writerow(card)

    print(string_buffer.getvalue())
    zip_file.writestr('cards.csv', string_buffer.getvalue())
    print(zip_file.filelist)
    zip_file.close()

    response = HttpResponse(zip_file, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=carddetails.zip' 
    return response    