from work.models import Speciality, Vacancy, Company

print(f"{Speciality.objects.count() =}")
spec = Speciality.objects.all()

print(f"{type(spec)=}")

#spec_dict = dict(spec) # так не хочет
spec_dict = {}
for spec_ in spec:
    spec_dict[spec_.code] = spec_.title


print(f"{type(spec_dict)=}")
print(f"{spec_dict=}")

"""
>>> >>> Speciality.objects.count() =8
>>> >>> >>> type(spec)=<class 'django.db.models.query.QuerySet'>
>>> >>> >>> >>> ... ... >>> >>> type(spec_dict)=<class 'dict'>
>>> spec_dict={'frontend': 'Фронтенд', 'backend': 'Бэкенд', 'gamedev': 'Геймдев', 'devops': '
Девопс', 'design': 'Дизайн', 'products': 'Продукты', 'management': 'Менеджмент', 'testing': '
Тестирование'}
"""
back = Vacancy.objects.filter(speciality__code="backend")
print(f"{back =}")
print(f"{back.count() =}")

spec_count = {}
for spec2 in spec_dict.keys():
    #print(f"{spec2 =}")
    code = Vacancy.objects.filter(speciality__code=spec2)
    #print(f"{code.count() =}")
    code_count = code.count()
    spec_count[spec2] = code_count

    #spec_count.setdefault(code, 0)
    #spec_count[code] = spec_count[code] + 1

print(f"{spec_count =}")

#==================================================
company_ = Company.objects.all()
company_id_title_dict = {}
for spec_ in company_:
     company_id_title_dict[spec_.id_str] = spec_.name

print(f"{company_id_title_dict =}")

company_title_employee_count = {}
for spec2 in company_:
     company_title_employee_count[spec2.name] = spec2.employee_count

print(f"{company_title_employee_count =}")

#=============================================
company_count = {}
for spec2 in spec_dict.keys():
    print(f"{spec2 =}")
    code = Vacancy.objects.filter(company__name=spec2)
    print(f"{code.count() =}")
    code_count = code.count()
    company_count[spec2] = code_count

    #spec_count.setdefault(code, 0)
    #spec_count[code] = spec_count[code] + 1

print(f"{company_count =}")

print(f"{company_title_employee_count =}")


"""
company_spec_count = {}
for spec2 in company_id_title_dict.keys():
    print(f"{spec2 =}")
    code = Vacancy.objects.filter(company__name=spec2)
    print(f"{code.count() =}")
    employee_count = code.employee_count
    company_spec_count[spec2] = employee_count

    #spec_count.setdefault(code, 0)
    #spec_count[code] = spec_count[code] + 1

print(f"{company_spec_count =}")
"""




