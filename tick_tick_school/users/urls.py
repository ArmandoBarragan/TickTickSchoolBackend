from rest_framework.routers import SimpleRouter
from .views import UserViewSet


router = SimpleRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = router.urls
