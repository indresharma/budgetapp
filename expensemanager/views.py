from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, TodayArchiveView
from .models import Transaction
from .forms import TransactionForm
import datetime
from django.urls import reverse_lazy
from django.db.models import Sum


# Create your views here.

def home(request):
    transactions = Transaction.objects.all().order_by('date')[:25]
    return render(request, 'expensemanager/home.html', {'transactions': transactions})


class TransactionTodayArchiveView(TodayArchiveView):
    queryset = Transaction.objects.all()
    date_field = "date"
    allow_future = True
    

def daily_transactions(request):
    pass


def monthlyView(request):
    today = datetime.datetime.now()
    cm = today.month
    transactions = Transaction.objects.filter(date__year=today.year, date__month=today.month)
    cm_total_income = transactions.filter(t_type="Income").aggregate(Sum('amount'))['amount__sum']
    cm_total_expense = transactions.filter(t_type="Expense").aggregate(Sum('amount'))['amount__sum']
    
    cm_total = cm_total_income + cm_total_expense
    
    ### Last Month Transactions ###
    if cm<2:
        py = today.year - 1
        pm = 12 - today.month
    else:
        py = today.year
        pm = today.month-1
    
    pm_transactions = Transaction.objects.filter(date__year=py, date__month=pm)
    pm_total_income = pm_transactions.filter(t_type="Income").aggregate(Sum('amount'))['amount__sum']
    pm_total_expense = pm_transactions.filter(t_type="Expense").aggregate(Sum('amount'))['amount__sum']
    # pm_total = pm_total_income + pm_total_expense

    return render(request, 'expensemanager/monthly_transaction.html', {
        'transactions': transactions, 
        'pm_transactions':pm_transactions, 
        'cm_total':cm_total,
        # 'pm_total':pm_total,
        })



####################################CRUD VIEWS######################################################  

class TransactionCreateView(CreateView):
    model = Transaction
    # fields = ['date', 't_type', 'category', 'amount']
    form_class = TransactionForm


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    redirect_field_name = 'expensemanager/home.html'

class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = reverse_lazy('home')




    


    

