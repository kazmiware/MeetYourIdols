from rest_framework.generics import (CreateAPIView, RetrieveAPIView)
from rest_framework.response import Response
from  django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import datetime

from.models import Group
from .serializers import GroupSerializer


class GroupCreateApiView(CreateAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):

        if serializer.is_valid():

            # user = self.request.POST.get('user')
            # user = get_object_or_404(User, user=user)
            pk = self.request.POST.get('pk')
            user = get_object_or_404(User, pk=pk)
            date = self.request.POST.get('date')
            print(date)
            name = serializer.validated_data['name']
            serializer.save(admin=user, date=date)
        return Response(serializer.data) 


class GroupDetailApiView(RetrieveAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer           
        


