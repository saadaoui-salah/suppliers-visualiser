from rest_framework.generics import ListAPIView
from .models import BusinessInformation
from .serializers import BusinessInformationSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import BusinessInformation
from .serializers import BusinessInformationSerializer

class BusinessInformationPagination(PageNumberPagination):
    page_size = 100 # Number of records per page
    page_size_query_param = 'page_size'  # Allow clients to control page size
    max_page_size = 100  # Maximum page size allowed

class BusinessInformationListView(ListAPIView):
    queryset = BusinessInformation.objects.all()
    serializer_class = BusinessInformationSerializer
    pagination_class = BusinessInformationPagination


class BusinessInformationSearchView(ListAPIView):
    queryset = BusinessInformation.objects.all()
    pagination_class = BusinessInformationPagination
    serializer_class = BusinessInformationSerializer
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')  # Get the search query from the request
        if query:
            return BusinessInformation.objects.filter(
                Q(abn__icontains=query) |
                Q(business_name__icontains=query) |
                Q(category__icontains=query) |
                Q(description__icontains=query) |
                Q(location__icontains=query)
            )
        return BusinessInformation.objects.none()  # Return an empty queryset if no query provided


def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')