from django.shortcuts import render


def home(request):
    """Контроллер главной страницы"""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Контроллер страницы 'Контакты'"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message, sep='\n')
        print(f"Имя: {name}\nТелефон: {phone}\nСообщение: {message}\n", sep='\n', file=open('file.txt', 'a'))
    return render(request, 'catalog/contacts.html')
