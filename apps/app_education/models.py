from django.db import models
from dotenv import load_dotenv
import os

load_dotenv()
DB_TABLE = os.getenv('DB_TABLE')

class IspKeywords(models.Model):
    term = models.CharField(max_length=100, primary_key=True)
    searches = models.IntegerField()
    orders = models.IntegerField()
    sales = models.DecimalField(max_digits=2, decimal_places=2)

    class Meta:
        db_table = DB_TABLE
        
