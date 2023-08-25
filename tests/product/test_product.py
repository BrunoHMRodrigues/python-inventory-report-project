from inventory_report.product import Product


def test_create_product() -> None:
    product_data = {
        "id": "123",
        "company_name": "Company Name",
        "product_name": "Product Name",
        "manufacturing_date": "2023-08-25",
        "expiration_date": "2024-08-25",
        "serial_number": "SN123456",
        "storage_instructions": "Store in a cool place."
    }

    product = Product(**product_data)  # ** Desempacota dados de um dicionários

    assert product.id == "123"
    assert product.company_name == "Company Name"
    assert product.product_name == "Product Name"
    assert product.manufacturing_date == "2023-08-25"
    assert product.expiration_date == "2024-08-25"
    assert product.serial_number == "SN123456"
    assert product.storage_instructions == "Store in a cool place."
