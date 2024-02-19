# Prefix To VRF

```
curl -X POST \
-H "Authorization: Token $TOKEN" \
-H "Content-Type: application/json" \
-H "Accept: application/json; version=2.0; indent=2" \
http://localhost:8080/api/plugins/prefix-to-vrf/vrf-prefix-assignments/ \
--data '{
    "vrf": {"name": "MyVrf", "namespace": {"name": "Global"}},
    "prefix": {"prefix": "10.0.1.0/24", "namespace": {"name": "Global"}}
}'
{
  "id": "06aef89d-b695-46bd-bf7a-b2a2a19d74f7",
  "object_type": "ipam.vrfprefixassignment",
  "display": "Global: (MyVrf): 10.0.1.0/24",
  "pk": "06aef89d-b695-46bd-bf7a-b2a2a19d74f7",
  "vrf": {
    "id": "11517a56-0621-414e-8f07-f0f31cf439e7",
    "object_type": "ipam.vrf",
    "url": "http://localhost:8080/api/ipam/vrfs/11517a56-0621-414e-8f07-f0f31cf439e7/"
  },
  "prefix": {
    "id": "aa2f1257-d9dd-4035-b096-f541279469cb",
    "object_type": "ipam.prefix",
    "url": "http://localhost:8080/api/ipam/prefixes/aa2f1257-d9dd-4035-b096-f541279469cb/"
  }
}%
```

<p align="center">
  <img src="https://raw.githubusercontent.com/pszulczewski/nautobot-app-prefix-to-vrf/develop/docs/images/icon-prefix-to-vrf.png" class="logo" height="200px">
  <br>
  <a href="https://github.com/pszulczewski/nautobot-app-prefix-to-vrf/actions"><img src="https://github.com/pszulczewski/nautobot-app-prefix-to-vrf/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/"><img src="https://readthedocs.org/projects/nautobot-plugin-prefix-to-vrf/badge/"></a>
  <a href="https://pypi.org/project/prefix-to-vrf/"><img src="https://img.shields.io/pypi/v/prefix-to-vrf"></a>
  <a href="https://pypi.org/project/prefix-to-vrf/"><img src="https://img.shields.io/pypi/dm/prefix-to-vrf"></a>
  <br>
  An <a href="https://www.networktocode.com/nautobot/apps/">App</a> for <a href="https://nautobot.com/">Nautobot</a>.
</p>

## Overview

> Developer Note: Add a long (2-3 paragraphs) description of what the App does, what problems it solves, what functionality it adds to Nautobot, what external systems it works with etc.

### Screenshots

> Developer Note: Add any representative screenshots of the App in action. These images should also be added to the `docs/user/app_use_cases.md` section.

> Developer Note: Place the files in the `docs/images/` folder and link them using only full URLs from GitHub, for example: `![Overview](https://raw.githubusercontent.com/pszulczewski/nautobot-app-prefix-to-vrf/develop/docs/images/app-overview.png)`. This absolute static linking is required to ensure the README renders properly in GitHub, the docs site, and any other external sites like PyPI.

More screenshots can be found in the [Using the App](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/user/app_use_cases/) page in the documentation. Here's a quick overview of some of the app's added functionality:

![](https://raw.githubusercontent.com/pszulczewski/nautobot-app-prefix-to-vrf/develop/docs/images/placeholder.png)

## Try it out!

> Developer Note: Only keep this section if appropriate. Update link to correct sandbox.

This App is installed in the Nautobot Community Sandbox found over at [demo.nautobot.com](https://demo.nautobot.com/)!

> For a full list of all the available always-on sandbox environments, head over to the main page on [networktocode.com](https://www.networktocode.com/nautobot/sandbox-environments/).

## Documentation

Full documentation for this App can be found over on the [Nautobot Docs](https://docs.nautobot.com) website:

- [User Guide](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/user/app_overview/) - Overview, Using the App, Getting Started.
- [Administrator Guide](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/admin/install/) - How to Install, Configure, Upgrade, or Uninstall the App.
- [Developer Guide](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/dev/contributing/) - Extending the App, Code Reference, Contribution Guide.
- [Release Notes / Changelog](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/admin/release_notes/).
- [Frequently Asked Questions](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/user/faq/).

### Contributing to the Documentation

You can find all the Markdown source for the App documentation under the [`docs`](https://github.com/pszulczewski/nautobot-app-prefix-to-vrf/tree/develop/docs) folder in this repository. For simple edits, a Markdown capable editor is sufficient: clone the repository and edit away.

If you need to view the fully-generated documentation site, you can build it with [MkDocs](https://www.mkdocs.org/). A container hosting the documentation can be started using the `invoke` commands (details in the [Development Environment Guide](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/dev/dev_environment/#docker-development-environment)) on [http://localhost:8001](http://localhost:8001). Using this container, as your changes to the documentation are saved, they will be automatically rebuilt and any pages currently being viewed will be reloaded in your browser.

Any PRs with fixes or improvements are very welcome!

## Questions

For any questions or comments, please check the [FAQ](https://docs.nautobot.com/projects/prefix-to-vrf/en/latest/user/faq/) first. Feel free to also swing by the [Network to Code Slack](https://networktocode.slack.com/) (channel `#nautobot`), sign up [here](http://slack.networktocode.com/) if you don't have an account.
