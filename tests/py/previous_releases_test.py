from unittest.mock import Mock

import pytest

from qiskit_sphinx_theme.previous_releases import extend_html_context, get_previous_versions_url


@pytest.mark.parametrize(
    "docs_url_prefix,expected",
    [
        ("documentation", "/documentation/stable/0.5/index.html"),
        ("ecosystem/finance", "/ecosystem/finance/stable/0.5/index.html"),
    ]
)
def test_get_previous_versions_url(docs_url_prefix: str, expected: str) -> None:
    """Check that we redirect to `/<prefix>/stable/<version>/index.html`."""
    assert get_previous_versions_url(docs_url_prefix, "0.5") == expected


def test_docs_url_prefix_validation() -> None:
    """Check that we error if `docs_url_prefix` is not set when `version_list` is.

    But, we should no-op if `version_list` is not set.
    """
    valid_config_with_versions = Mock(
        html_context={"version_list": [0.1]}, docs_url_prefix="ecosystem/finance"
    )
    extend_html_context(Mock(), valid_config_with_versions)

    valid_config_no_versions = Mock(html_context={}, docs_url_prefix=None)
    extend_html_context(Mock(), valid_config_no_versions)

    invalid_config = Mock(html_context={"version_list": [0.1]}, docs_url_prefix=None)
    with pytest.raises(Exception):
        extend_html_context(Mock(), invalid_config)
