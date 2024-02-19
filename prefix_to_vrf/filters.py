"""Filtering for prefix_to_vrf."""
from nautobot.core.filters import NaturalKeyOrPKMultipleChoiceFilter
from nautobot.ipam.models import Prefix, VRF, VRFPrefixAssignment
from nautobot.apps.filters import NautobotFilterSet


class VRFPrefixAssignmentFilterSet(NautobotFilterSet):
    prefix = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        to_field_name="pk",
        label="Prefix (ID or name)",
    )
    vrf = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=VRF.objects.all(),
        to_field_name="name",
        label="VRF (ID or name)",
    )

    class Meta:
        model = VRFPrefixAssignment
        fields = ["id", "vrf", "prefix"]
