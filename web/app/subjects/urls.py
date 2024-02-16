from rest_framework.routers import SimpleRouter
from .views import SubjectViewSet

router = SimpleRouter()
router.register(r'', SubjectViewSet, basename="subjects")

urlpatterns = router.urls
