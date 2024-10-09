from django.db import models


NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Product Name",
        help_text="Enter the name of the product",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Product Description",
        help_text="Enter the description of the product",
    )
    image = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Product Image",
        help_text="Upload the image of the product",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Product Category",
        help_text="Enter the category of the product",
        related_name="products",
        **NULLABLE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Product Price",
        help_text="Enter the price of the product",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of Creation",
        help_text="Enter the date of creation of the product",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date of Last Update",
        help_text="Enter the date of last update of the product",
    )


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Category Name",
        help_text="Enter the name of the category",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Category Description",
        help_text="Enter the description of the category",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Product",
        help_text="Enter the product",
        related_name="versions",
    )
    number = models.CharField(
        max_length=100,
        verbose_name="Version Number",
        help_text="Enter the number of the version",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Version Name",
        help_text="Enter the name of the version",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Is Active",
        help_text="Enter the active version of the product",
    )

    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versions"
        ordering = ["product", "number"]

    def __str__(self):
        return self.number
