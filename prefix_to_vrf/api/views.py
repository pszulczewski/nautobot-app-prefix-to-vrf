"""API views for prefix_to_vrf."""

from nautobot.ipam.models import VRFPrefixAssignment
from nautobot.apps.api import NautobotModelViewSet

from prefix_to_vrf import filters
from prefix_to_vrf.api import serializers


class VRFPrefixAssignmentViewSet(NautobotModelViewSet):
    queryset = VRFPrefixAssignment.objects.select_related("vrf", "prefix")
    serializer_class = serializers.VRFPrefixAssignmentSerializer
    filterset_class = filters.VRFPrefixAssignmentFilterSet
