"""Django API urlpatterns declaration for prefix_to_vrf app."""
from nautobot.ipam.api.views import IPAMRootView
from nautobot.ipam.api.urls import OrderedDefaultRouter

from prefix_to_vrf.api import views

router = OrderedDefaultRouter()
router.APIRootView = IPAMRootView
router.register("vrf-prefix-assignments", views.VRFPrefixAssignmentViewSet)

urlpatterns = router.urls
