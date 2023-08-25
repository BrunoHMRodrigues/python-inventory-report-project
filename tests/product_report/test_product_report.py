from inventory_report.product import Product


def test_product_report() -> None:
    product_data = {
        "id": "123",
        "company_name": "Company Name",
        "product_name": "Product Name",
        "manufacturing_date": "2023-08-25",
        "expiration_date": "2024-08-25",
        "serial_number": "SN123456",
        "storage_instructions": "Store in a cool place."
    }

    product = Product(**product_data)

    expected_output = (
        f"The product {product.id} - {product.product_name}"
        " with serial number "
        f"{product.serial_number} manufactured on {product.manufacturing_date}"
        " by the "
        f"company {product.company_name} valid until {product.expiration_date}"
        " must be stored "
        f"according to the following instructions: "
        f"{product.storage_instructions}."

    )

    assert str(product) == expected_output
