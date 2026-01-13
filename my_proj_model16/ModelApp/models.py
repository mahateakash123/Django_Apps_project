from django.db import models

# Create your models here.
# passsword : Akash@123
# username: akash

class  Emp(models.Model):    # Create a table named emp in the database.”
    eno=models.IntegerField()
    ename = models.CharField(max_length=20)# Every field you define inside the class becomes a column in the table.
    sal=models.FloatField()
    sex=models.CharField(max_length=20)
    dno=models.IntegerField()

    def __str__(self):
        return self.ename