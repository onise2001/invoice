from django.urls import path, include
from .views import AllInvoiceView, CreateInvoiceView, CreateDraftView, EditInvoiceView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(r"", CreateInvoiceView, basename="create")

urlpatterns = [
    #path("list/",AllInvoiceView.as_view()),
    path("invoice/draft/", CreateDraftView.as_view(), name="draft"),
    path("invoice/mark_as_paid/<str:id>", EditInvoiceView.as_view(), name="edit"),
    path("invoice/",include(router.urls)),
   
]