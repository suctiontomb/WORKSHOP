from rest_framework.routers import DefaultRouter
from tools.views import ToolViewSet, TechnicianViewSet, ToolCheckoutViewSet


router = DefaultRouter()

router.register('tool', ToolViewSet)
router.register('technician', TechnicianViewSet)
router.register('toolcheckout', ToolCheckoutViewSet)

urlpatterns = router.urls