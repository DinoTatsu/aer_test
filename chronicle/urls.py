from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import EventList, ChronicleList, ChronicleWithDaysView

router = DefaultRouter()
router.register(r'events', EventList, basename='events')
router.register(r'chronicles', ChronicleList, basename='chronicles')
urlpatterns = router.urls
urlpatterns += [
    path('chronicles/<str:unique_id>/check-events/<int:n>/', ChronicleWithDaysView.as_view(), name='chronicle_events'),
    path('chronicles/<str:unique_id>/check-events/', ChronicleWithDaysView.as_view(), name='chronicle_events'),
]
