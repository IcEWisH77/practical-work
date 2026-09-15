from django.shortcuts import render
from .models import UserName

def index(request):
    greeting, error = None, None

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if not name:
            error = 'Пожалуйста, введите имя'
        elif len(name) > 100:
            error = 'Имя слишком длинное'
        else:
            UserName.objects.create(name=name)
            greeting = name

    return render(request, 'greeting/index.html',
                  {'greeting': greeting, 'error': error})