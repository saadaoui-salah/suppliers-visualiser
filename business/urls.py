from django.urls import path
from .views import BusinessInformationListView, BusinessInformationSearchView

urlpatterns = [
    path('list/', BusinessInformationListView.as_view(), name='business-information-list'),
    path('search/', BusinessInformationSearchView.as_view(), name='business_search'),
]