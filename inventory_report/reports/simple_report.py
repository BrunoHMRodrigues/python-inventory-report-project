from typing import List
from datetime import datetime, timedelta
from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory, Product


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing_date = None
        closest_expiration_date = None
        largest_inventory_company = None
        largest_inventory_count = 0

        current_date = datetime.now()

        for inventory in self.inventories:
            for product in inventory.data:
                manufacturing_date = datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                )
                expiration_date = datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                )

                if (
                    oldest_manufacturing_date is None
                    or manufacturing_date < oldest_manufacturing_date
                ):
                    oldest_manufacturing_date = manufacturing_date

                if current_date <= expiration_date and (
                    closest_expiration_date is None
                        or expiration_date < closest_expiration_date
                ):
                    closest_expiration_date = expiration_date

                inventory_count = len(inventory.data)
                if inventory_count > largest_inventory_count:
                    largest_inventory_count = inventory_count
                    largest_inventory_company = product.company_name

        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date.strftime('%Y-%m-%d')}\n"
            f"Closest expiration date: {closest_expiration_date.strftime('%Y-%m-%d')}\n"
            f"Company with the largest inventory: {largest_inventory_company}"
        )

        return report
