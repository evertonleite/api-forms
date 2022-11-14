from rest_framework.routers import DefaultRouter
from apiForm.views import UserViewSet


app_name = 'apiForm'

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
urlpatterns = router.urls