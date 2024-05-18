from django.shortcuts import render
from .models import Invoice,Status
from .serializers import InvoiceSerializer, StatusSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from django.core import serializers
from rest_framework import status
# Create your views here.


class AllInvoiceView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class CreateInvoiceView(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer



class CreateDraftView(CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        draft_id = Status.objects.filter(name="Draft")
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():           
            serializer.validated_data['status'] = draft_id[0]
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)
               
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        

class EditInvoiceView(UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        invoice = self.get_object()
        status = Status.objects.get(name="Paid")

        if invoice.status.name == "Pending":
            invoice.status = status
            serializer = self.serializer_class(invoice, data={"invoice":invoice}, partial=True)
            if serializer.is_valid():     
                self.perform_update(serializer)
                return Response(serializer.data)
            return Response(serializer.errors)
        
        return Response(data={"Error": "You can't change the status of a draft."})

        
        
        
           
