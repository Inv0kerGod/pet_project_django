import pytest

from django.core.cache import cache

from amocrm.cache.catalog_id import get_catalog_id
from amocrm.exceptions import AmoCRMCacheException
from amocrm.types import AmoCRMCatalog

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.single_thread,
]


@pytest.fixture
def products_catalog():
    return AmoCRMCatalog(id=333, name="Products", type="products")


@pytest.fixture
def catalogs(products_catalog):
    return [products_catalog, AmoCRMCatalog(id=123, name="Useless", type="meh")]


@pytest.fixture(autouse=True)
def mock_get_catalogs(mocker, catalogs):
    return mocker.patch("amocrm.client.AmoCRMClient.get_catalogs", return_value=catalogs)


def test_return_catalog_if_in_cache(products_catalog, mock_get_catalogs):
    cache.set("amocrm_products_catalog_id", products_catalog.id)

    got = get_catalog_id(catalog_type="products")

    assert got == products_catalog.id
    mock_get_catalogs.assert_not_called()


def test_return_catalog_from_response_if_not_in_cache(products_catalog, mock_get_catalogs):
    cache.clear()

    got = get_catalog_id(catalog_type="products")
    assert got == products_catalog.id
    assert cache.get("amocrm_products_catalog_id") == products_catalog.id
    mock_get_catalogs.assert_called_once()


def test_fail_if_not_in_cache_and_not_in_response(mock_get_catalogs):
    cache.clear()
    mock_get_catalogs.return_value = [AmoCRMCatalog(id=111, name="NotWhatINeed", type="sad-story")]

    with pytest.raises(AmoCRMCacheException):
        get_catalog_id(catalog_type="products")