from typing import List
from resources.products.models import ProductOut
from data.repos import product_repo as repo


def validate_product_name():
    ...


async def get_products(limit: int) -> List[ProductOut]:
    return []
