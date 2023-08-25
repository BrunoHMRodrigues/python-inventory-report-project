from typing import List, Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None):
        if data is None:
            self._data = []
        else:
            self._data = data

    def add_data(self, data: List[Product]) -> None:
        self._data.extend(data)

    @property
    def data(self) -> List[Product]:
        return self._data.copy()
