from django.contrib import admin
from tools.models import Tool,Technician, ToolCheckout

admin.site.register(Tool)
admin.site.register(Technician)
admin.site.register(ToolCheckout)
