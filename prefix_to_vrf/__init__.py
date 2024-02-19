"""App declaration for prefix_to_vrf."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class PrefixToVrfConfig(NautobotAppConfig):
    """App configuration for the prefix_to_vrf app."""

    name = "prefix_to_vrf"
    verbose_name = "Prefix To VRF"
    version = __version__
    author = "Patryk"
    description = "Prefix To VRF."
    base_url = "prefix-to-vrf"
    required_settings = []
    min_version = "2.1.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = PrefixToVrfConfig  # pylint:disable=invalid-name
