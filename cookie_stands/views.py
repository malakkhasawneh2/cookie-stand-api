from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookie_stands
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieSerializer


class CookieList(ListCreateAPIView):
    queryset = Cookie_stands.objects.all()
    serializer_class = CookieSerializer


class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cookie_stands.objects.all()
    serializer_class = CookieSerializer
