from django.urls import path
from vendors import views

urlpatterns = [
    path(
        "",
        views.VendorListCreateAPIView.as_view(),
        name="vendor_list_create",
    ),
    path(
        "/<int:pk>",
        views.VendorDetailUpdateDeleteAPIView.as_view(),
        name="vendors_detail_update_delete",
    ),
    path(
        "/<int:pk>/performace",
        views.VendorPerformanceAPIView.as_view(),
        name="vendore_performace",
    ),
]
