from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {
                "name": "Product 1",
                "description": "Description of Product 1",
                "price": 100.00,
            },
            {
                "name": "Product 2",
                "description": "Description of Product 2",
                "price": 200.00,
            },
            {
                "name": "Product 3",
                "description": "Description of Product 3",
                "price": 300.00,
            },
        ]

        category_list = [
            {
                "name": "Category 1",
            },
            {
                "name": "Category 2",
            },
            {
                "name": "Category 3",
            },
        ]

        products_for_create = []
        for product in product_list:
            products_for_create.append(Product(**product))
        Product.objects.bulk_create(products_for_create)

        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))
        Category.objects.bulk_create(category_for_create)



