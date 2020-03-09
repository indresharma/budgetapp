from django.db import models
from django.urls import reverse
from django.forms import DateInput

trans_type = [
    ('Income', 'Income'),
    ('Expense', 'Expense')
]

category_types= [
    ('Bills', 'Bills'),
    ('Rent', 'Rent'),
    ('Transportation', 'Transportation'),
    ('Shopping', 'Shopping'),
    ('Grocery', 'Grocery'),
    ('Daily Needs', 'Daily Needs'),
    ('Medical', 'Medical'),
    ('Other Expense', 'Other expense'),
    ('Salary', 'Salary'),
    ('Other Income', 'Other Income'),

]


class Transaction(models.Model):
    date = models.DateField()
    t_type = models.CharField(choices=trans_type, max_length=20)
    category = models.CharField(choices=category_types, max_length=50)
    amount = models.FloatField()
    
    def __str__(self):
        return self.t_type

    def get_absolute_url(self):
        return reverse('home')