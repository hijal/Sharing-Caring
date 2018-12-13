from django.urls import path
from .views import SignUpViewPage

urlpatterns = [
    path('signup/', SignUpViewPage.as_view(), name='signup'),
]