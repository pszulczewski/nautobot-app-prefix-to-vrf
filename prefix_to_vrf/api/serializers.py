"""API serializers for prefix_to_vrf."""
from nautobot.ipam.models import VRFPrefixAssignment
from nautobot.core.api import ValidatedModelSerializer, BaseModelSerializer


class VRFPrefixAssignmentSerializer(ValidatedModelSerializer):
    class Meta:
        model = VRFPrefixAssignment
        fields = (
            "pk",
            "vrf",
            "prefix",
        )
