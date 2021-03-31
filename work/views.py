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
    company_ = Company.objects.all()
    company_id_title_dict = {}
    for spec_ in company_:
        company_id_title_dict[spec_.id_str] = spec_.name
    # print(f"{company_id_title_dict =}")
    company_title_employee_count = {}
    for spec2 in company_:
        company_title_employee_count[spec2.name] = spec2.employee_count
    # print(f"{company_title_employee_count =}")
    # =============================================
    company_count = {}
    comp_id_title = company_id_title_dict
    for spec2 in comp_id_title.values():
        # print(f"{spec2 =}")
        code = Vacancy.objects.filter(company__name=spec2)
        # print(f"{code.count() =}")
        code_count = code.count()
        company_count[spec2] = code_count
    # print(f"{company_count =}")

    return render(request, "work/index.html", context={
        'spec_count': spec_count,
        'company_count': company_count,
    })

    # return HttpResponse("main_view здесь будут все компании или здесь будет специализация", )

def vacancies(request, ): #– Все вакансии списком   /vacancies
    vacancy_all = Vacancy.objects.all()
    # for vacancy in vacancy_all:
    #     vacancy_title = vacancy.title
    #     vacancy_skills = vacancy.skills
    #     vacancy_salary_min = vacancy.salary_min
    #     vacancy_salary_max = vacancy.salary_max
    #     vacancy_published_at = vacancy.published_at
    #     print(f"{vacancy.speciality.title=}")
    #     print(f"{vacancy.company.name=}")

    return render(request, "work/vacancies.html", context={
        'vacancy_all': vacancy_all,
    })
    # return HttpResponse("vacncies здесь будут все компании или здесь будет специализация", )


def vacancies_category(request, category):
    #– Вакансии по специализации /vacancies/cat/frontend
    # vacancy_cat = Vacancy.objects.all()
    vacancy_cat2 = Vacancy.objects.filter(speciality__code=category)

    spec = Speciality.objects.all()
    spec_dict = {}
    for spec_ in spec:
        spec_dict[spec_.code] = spec_.title
    category = spec_dict[category]
    return render(request, "work/vacancies.html", context={
        'vacancy_all': vacancy_cat2,
        'category':category,
    })
    # return HttpResponse("vacancies_cat_frontend здесь будут все компании или здесь будет специализация", )

def companies(request, id_): #– Карточка компании  /companies/345
    company_ = Company.objects.filter(id=id_)
    company_2 = []
    for group in company_:
        # company_2.append(group)
        name = group.name
        location = group.location

    company_code = Vacancy.objects.filter(company__id_str=id_)
    # print(f"{company_code.count() =}")
    # for vacancy in company_code:
    #     print(f"{vacancy.skills =}")
    #     print(f"{vacancy.text =}")
    #     print(f"{vacancy.salary_min =}")
    #     print(f"{vacancy.salary_max =}")
    #     print(f"{vacancy.published_at =}")

    return render(request, "work/company.html", context={
        'company': company_2,
        'name': name,
        'location': location,
        'company_code':company_code,
    })
    # return HttpResponse("companies здесь будут все компании или здесь будет специализация", )

def vacancy(request, id_): #– Одна вакансия /vacancies/22
    vacancy_code = Vacancy.objects.filter(id_str=id_)

    # for vacancy in vacancy_code:
    #     print(f"{vacancy.speciality.code =}")
    #     print(f"{vacancy.company.name =}")
    #     print(f"{vacancy.title =}")
    #     print(f"{vacancy.skills =}")
    #     print(f"{vacancy.text =}")
    #     print(f"{vacancy.salary_min =}")
    #     print(f"{vacancy.salary_max =}")
    #     print(f"{vacancy.published_at =}")

    return render(request, "work/vacancy.html", context={
        'vacancy_code':vacancy_code,
    })
    # return HttpResponse("vacancies_id здесь будут все компании или здесь будет специализация", )
