from django.contrib import admin
from Purpose.models import Goal_Description, Financial_Investments, Income, Expense_Categories, Expenses

# Register your models here.

admin.site.register(Goal_Description)
admin.site.register(Financial_Investments)
admin.site.register(Income)
admin.site.register(Expense_Categories)
admin.site.register(Expenses)