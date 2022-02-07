from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'Deliveries', views.DeliveriesView, basename='deliveries')
router.register(r'Truck', views.TruckView, basename='truck')
router.register(r'Users', views.UsersView, basename='users')
router.register(r'WebsiteContacts', views.WebsiteContactsView,
                basename='websiteContacts')


urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]
