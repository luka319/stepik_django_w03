from django.shortcuts import render, HttpResponse
from work.models import Company, Speciality,Vacancy
# Create your views here.

"""
– Главная  / 
– Все вакансии списком   /vacancies
– Вакансии по специализации /vacancies/cat/frontend
– Карточка компании  /companies/345
– Одна вакансия /vacancies/22

Выведите на каждой страничке надпись типа 
«здесь будут все компании или здесь будет специализация» 
– дальше вы замените этот вывод на шаблоны и содержательный вывод.

"""
def main_view(request): # – Главная  /
    """5.    Выведите    список    специализаций    на    главной
    странице    Получите    специализации    типа «фронтенд» или «бекенд» из
    базы, выведите    их    на    главной.    Вместо    картинок    храните
    в    базе    данных    https: // place - hold.it / 100    x60
    """
    # Company, Speciality, Vacancy
    # from work.models import Speciality, Vacancy# есть наверху
    spec = Speciality.objects.all()
    spec_dict = {}
    for spec_ in spec:
        spec_dict[spec_.code] = spec_.title
    """    
    >>> spec_dict={'frontend': 'Фронтенд', 'backend': 'Бэкенд', 'gamedev': 'Геймдев', 'devops': '
    Девопс', 'design': 'Дизайн', 'products': 'Продукты', 'management': 'Менеджмент', 'testing': '
    Тестирование'}
    """
    spec_count = {}
    for spec2 in spec_dict.keys():
        # print(f"{spec2 =}")
        code = Vacancy.objects.filter(speciality__code=spec2)
        # print(f"{code.count() =}")
        code_count = code.count()
        spec_count[spec2] = code_count
        # spec_count.setdefault(code, 0)
        # spec_count[code] = spec_count[code] + 1
    # print(f"{spec_count =}")
    # company_ = Company.objects.all()
    # spec_dict = {}
    # for spec_ in spec:
    #     spec_dict[spec_.code] = spec_.title

    return render(request, "work/index.html", context={
        'spec_count': spec_count,
    })

    # return HttpResponse("main_view здесь будут все компании или здесь будет специализация", )

def vacancies(request, ): #– Все вакансии списком   /vacancies

    return render(request, "work/vacancies.html", )
    # return HttpResponse("vacncies здесь будут все компании или здесь будет специализация", )


def vacancies_category(request, category): #– Вакансии по специализации /vacancies/cat/frontend

    return render(request, "work/vacancies.html", )
    # return HttpResponse("vacancies_cat_frontend здесь будут все компании или здесь будет специализация", )

def companies(request, id_): #– Карточка компании  /companies/345

    # return render(request, "companies_id.html", )
    return HttpResponse("companies здесь будут все компании или здесь будет специализация", )

def vacancy(request, id_): #– Одна вакансия /vacancies/22

    return render(request, "work/vacancy.html", )
    # return HttpResponse("vacancies_id здесь будут все компании или здесь будет специализация", )
