from django.urls import path
from .views import *

urlpatterns = [
    path('api/list/', BusinessInformationListView.as_view(), name='business-information-list'),
    path('api/search/', BusinessInformationSearchView.as_view(), name='business_search'),
    path('', home, name='home'),
    path('search/', search, name='search'),
]