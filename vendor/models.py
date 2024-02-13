from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_id = models.PositiveIntegerField()
    website = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_no = models.PositiveIntegerField()
    product_category = models.CharField(max_length=50)
    detailed_description = models.CharField(max_length=500)
    company_name = models.CharField(max_length=50)
    software_name = models.CharField(max_length=50)
    company_established = models.PositiveIntegerField()
    location_countries = models.CharField(max_length=500)
    location_cities = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    internal_professional_services = models.CharField(max_length=3)
    last_reviewed_date = models.CharField(max_length=20)
    business_areas = models.CharField(max_length=200)
    modules = models.CharField(max_length=50)
    financial_services_client_types = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=500)
    doc_to_attach = models.CharField(max_length=3)

    def __str__(self):
        return f'Vendor: {self.product_name} {self.product_category}' 
