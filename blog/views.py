from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def post_detail(request, post_id):
    posts = {
        1: {
            'title': 'Введение в Django',
            'date': '1 декабря 2025',
            'content': '''Django - это высокоуровневый веб-фреймворк на языке Python, который позволяет быстро разрабатывать безопасные и поддерживаемые веб-сайты.

Созданный опытными разработчиками, Django берет на себя большую часть хлопот веб-разработки, поэтому вы можете сосредоточиться на написании своего приложения без необходимости изобретать велосипед.

Основные преимущества Django:
- Быстрая разработка
- Безопасность из коробки
- Масштабируемость
- Полнофункциональность'''
        },
        2: {
            'title': 'Шаблоны в Django',
            'date': '3 декабря 2025',
            'content': '''Система шаблонов Django позволяет эффективно разделять логику и представление в веб-приложениях.

Шаблоны Django используют специальный язык разметки, который позволяет динамически генерировать HTML.

Основные возможности:
- Наследование шаблонов
- Фильтры и теги
- Автоматическое экранирование HTML
- Переиспользование компонентов'''
        },
        3: {
            'title': 'Модели и базы данных',
            'date': '5 декабря 2025',
            'content': '''ORM (Object-Relational Mapping) Django предоставляет удобный способ работы с базами данных без написания SQL-запросов.

Модели Django - это Python-классы, которые описывают структуру данных вашего приложения.

Преимущества ORM Django:
- Абстракция от конкретной СУБД
- Безопасность от SQL-инъекций
- Удобные методы для работы с данными
- Автоматическая миграция схемы базы данных'''
        }
    }

    post = posts.get(post_id, {
        'title': 'Пост не найден',
        'date': '',
        'content': 'К сожалению, запрошенный пост не существует.'
    })

    return render(request, 'blog/post_detail.html', {'post': post})


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:reviews')
    else:
        form = ReviewForm()

    approved_reviews = Review.objects.filter(is_verified=True).order_by('-created_at')

    return render(request, 'blog/reviews.html', {
        'form': form,
        'reviews': approved_reviews
    })
