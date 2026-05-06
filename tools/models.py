from django.db import models

class Tool(models.Model):
    TOOL_CONDITION = [('good', 'Good state'),
                      ('mild', 'Mild state'),
                      ('Bad', 'Bad State')]

    name = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=50, unique=True)
    condition = models.CharField(max_length=10, choices= TOOL_CONDITION, default='good')
    location = models.CharField(max_length=30)

    def __str__(self) ->str:
        return f"{self.name} - {self.serial_number} - {self.condition}"

class Technician(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone} - {self.email}"

class ToolCheckout(models.Model):
    which_tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    which_technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField(blank=True,null=True)
    notes = models.TextField(max_length= 100)

    def __str__(self) -> str:
        return f"{self.which_tool} - {self.which_technician} - {self.checkout_date}"



