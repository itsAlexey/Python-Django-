from django.db import models

# Create your models here.

# Описание цели
#     ├── название
#     ├── стоимость 
#     ├── дата создания
#     ├── дата завершения
#     ├── финансовые вложения (ссылка на таблицу "Финансовые вложения")
#     └── дополнительная информация

class Goal_Description(models.Model):
    """Описание цели"""
    name = models.CharField(verbose_name='Название', max_length=150)
    cost = models.IntegerField(verbose_name='Стоимость')
    creationDate = models.DateTimeField(verbose_name='Дата создания')
    completionDate = models.DateTimeField(verbose_name='Дата завершения')
    additionalInformation = models.TextField(verbose_name='Дополнительная информация', max_length=250)

    class Meta:
        verbose_name = 'Описание цели'
        verbose_name_plural = 'Описание целей'
        db_table = 'goal_description'

    def __str__(self):
        return self.name

# Финансовые вложения
#     ├── дата
#     ├── изменение средств
#     ├── описание за счет какого события
#     ├── описание события
#     └── итог остатка или выполнения

class Financial_Investments(models.Model):
    """Финансовые вложения"""
    financialInvestment = models.ForeignKey(Goal_Description, on_delete=models.CASCADE, verbose_name='Финансовые вложения')
    date = models.DateTimeField(verbose_name='Дата события')
    changeInFunds = models.IntegerField(verbose_name='Изменение средств')
    descriptionOfTheEvent = models.CharField(verbose_name='Описание события', max_length=150)
    balanceOrResult = models.CharField(verbose_name='Остаток/статус выполнения', max_length=150)

    class Meta:
        verbose_name = 'Финансовые вложения'
        verbose_name_plural = 'Финансовых вложений'
        db_table = 'financial_investments'

    def __str__(self):
        return self.descriptionOfTheEvent

# Доходы
#     ├── дата
#     ├── сумма
#     ├── источник дохода (например, зарплата, подработка, дивиденды)
#     └── дополнительная информация

class Income(models.Model):
    """Доходы"""
    date = models.DateTimeField(verbose_name='Дата получения')
    amount = models.IntegerField(verbose_name='Сумма')
    sourceOfIncome = models.CharField(verbose_name='Источник дохода', max_length=150)
    additionalШnformation = models.CharField(verbose_name='Дополнительная информация', max_length=150)
    
    class Meta:
        verbose_name = 'Доходы'
        verbose_name_plural = 'Доходы'
        db_table = 'income'

    def __str__(self):
        return f"{self.sourceOfIncome} {'{0:,}'.format(self.amount).replace(',', ' ')}"

# Категории расходов
#     └── название
# Expense Categories
#     └── name

class Expense_Categories(models.Model):
    """Категории расходов"""
    name = models.CharField(verbose_name='Название', max_length=150)
    
    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Название'
        db_table = 'expense_Categories'

    def __str__(self):
        return {self.name}


# Расходы
#     ├── дата
#     ├── сумма
#     ├── категория (ссылка на таблицу "Категории расходов")
#     └── дополнительная информация

class Expenses(models.Model):
    """Расходы"""
    name =  models.ForeignKey(Expense_Categories, on_delete=models.CASCADE, verbose_name='Категории расходов')
    date = models.DateTimeField(verbose_name='Дата траты')
    amount = models.IntegerField(verbose_name='Сумма')
    additionalШnformation = models.CharField(verbose_name='Дополнительная информация', max_length=150)
    
    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'
        db_table = 'expenses'

    def __str__(self):
        return f"{self.name} {'{0:,}'.format(self.amount).replace(',', ' ')}"
