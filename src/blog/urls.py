from django.urls import path
from blog.views import *

urlpatterns = [
    path('', TopView.as_view(), name='top'),
]
