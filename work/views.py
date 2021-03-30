from django.shortcuts import render, HttpResponse

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

    return render(request, "work/index.html", )
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
