from django.urls import path

from .views import IndexPageView, ContactPageView


urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact')
]