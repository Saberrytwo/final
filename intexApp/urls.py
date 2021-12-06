from django.urls import path
from .views import deletePrescriberPageView, indexPageView, drugPageView, prescriberPageView, searchDrugsPageView, searchPrescribersPageView, deletePrescriberPageView, addPrescriberPageView, singlePrescriberPageView, singleDrugPageView, updatePresPageView

urlpatterns = [
    path("", indexPageView, name='index'),
    path("drug/", drugPageView, name='drug'),
    path("prescriber/",prescriberPageView, name='prescriber' ),
    path("searchDrugs", searchDrugsPageView, name='searchDrugs'),
    path("searchPrescribers/", searchPrescribersPageView, name='searchPrescribers'),
    path("deletePrescriber/<int:npifr>/", deletePrescriberPageView, name="deletePrescriber"),
    path("addPrescriber/", addPrescriberPageView, name="addPrescriber"),
    path("singlePrescriber/<int:npi>/", singlePrescriberPageView, name="singlePrescriber"),
    path("singleDrug/<str:drugname>/", singleDrugPageView, name="singleDrug"),
    path("updatePres/", updatePresPageView, name="updatePres")
]
