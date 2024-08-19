from django.db import models

# Create your models here.
class ETF(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)  # This might be a foreign key to a User model
    etfs = models.ManyToManyField(ETF, through='PortfolioAllocation')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PortfolioAllocation(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    etf = models.ForeignKey(ETF, on_delete=models.CASCADE)
    allocation_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 50.00 for 50%

    def __str__(self):
        return f"{self.portfolio.name} - {self.etf.symbol}: {self.allocation_percentage}%"
