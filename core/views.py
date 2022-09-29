from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ListSerializer
from .models import ListaCompras


class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ListaCompras.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
