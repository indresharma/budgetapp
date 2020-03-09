from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, TodayArchiveView
from .models import Transaction
from .forms import TransactionForm
import datetime
from django.urls import reverse_lazy
from django.db.models import Sum


# Create your views here.

def home(request):
    transactions = Transaction.objects.all().order_by('date').reverse()[:25]
    return render(request, 'expensemanager/home.html', {'transactions': transactions})


class TransactionTodayArchiveView(TodayArchiveView):
    queryset = Transaction.objects.all()
    date_field = "date"
    allow_future = True
    

def date_range_view(request):
    if request.method == 'POST':
        start_month = int(request.POST.get('startmonth')[5:])
        start_year = int(request.POST.get('startmonth')[:4])
        end_month = int(request.POST.get('endmonth')[5:])
        end_year = int(request.POST.get('endmonth')[:4])

        select_transactions = Transaction.objects.filter(date__year__gte=start_year, date__month__gte=start_month, date__year__lte=end_year, date__month__lte=end_month).order_by('date')
        return render(request, 'expensemanager/date_range.html', {'select_transactions':select_transactions})
    

def last_month_view(request):
    
    today = datetime.datetime.now()
    cm = today.month
    
    ############# Last Month Transactions ##################
    if cm<2:
        py = today.year - 1
        pm = 12 - today.month
    else:
        py = today.year
        pm = today.month-1
    
    pm_transactions = Transaction.objects.filter(date__year=py, date__month=pm).order_by('date')
    pm_total_income = pm_transactions.filter(t_type="Income").aggregate(Sum('amount'))['amount__sum']
    pm_total_expense = pm_transactions.filter(t_type="Expense").aggregate(Sum('amount'))['amount__sum']

    #string formatting for large numbers 
    pm_total_income = f'{pm_total_income:,}'
    pm_total_expense = f'{pm_total_expense:,}'

    return render(request, 'expensemanager/monthly_transaction.html', {
        'transactions': transactions, 
        'pm_transactions':pm_transactions, 
        'pm_total_income':pm_total_income,
        'pm_total_expense':pm_total_expense,
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


######################### Charts  ##############################

def expense_chart(request):
    labels = []
    data = []
    chart_month = int(request.POST.get("chartinput")[5:])
    chart_year = int(request.POST.get("chartinput")[:4])

    queryset = Transaction.objects.filter(date__year=chart_year, date__month=chart_month, t_type='Expense').values(
        'category').annotate(total_amount = Sum('amount')).order_by('category')
    # result is a dictionary
    for value in queryset:
        labels.append(value.get('category'))
        data.append(value.get('total_amount'))

    return render(request, 'expensemanager/expense_chart.html', {
        'labels': labels,
        'data': data,
    })



    


    

