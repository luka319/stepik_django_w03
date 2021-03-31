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
comp_id_title = company_id_title_dict
for spec2 in comp_id_title.values():
    print(f"{spec2 =}")
    code = Vacancy.objects.filter(company__name=spec2)
    print(f"{code.count() =}")
    code_count = code.count()
    company_count[spec2] = code_count

    #spec_count.setdefault(code, 0)
    #spec_count[code] = spec_count[code] + 1

print(f"{company_count =}")

#print(f"{company_title_employee_count =}")
print("=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#print(f"{company_id_title_dict =}")

vacancy_all = Vacancy.objects.all()
for vacancy in vacancy_all:
    print(f"{vacancy.title=}")
    print(f"{vacancy.skills=}")
    print(f"{vacancy.salary_min=}")
    print(f"{vacancy.salary_max=}")
    print(f"{vacancy.published_at=}")
    print(f"{vacancy.speciality=}")
    print(f"{vacancy.company=}")
    print(f"{vacancy.speciality.title=}")
    print(f"{vacancy.company.name=}")


#vacancy_cat = Vacancy.objects.all()
vacancy_cat = Vacancy.objects.filter(speciality__code=="backend")
#Team.objects.filter(name="Tutshill Tornados")
for vacancy in vacancy_cat:
    #if vacancy.speciality.title=="backend":
       print(f"{vacancy.title=}")            
       print(f"{vacancy.skills=}")           
       print(f"{vacancy.salary_min=}")       
       print(f"{vacancy.salary_max=}")       
       print(f"{vacancy.published_at=}")     
       print(f"{vacancy.speciality=}")       
       print(f"{vacancy.company=}")          
       print(f"{vacancy.speciality.title=}") 
       print(f"{vacancy.company.name=}")     
    

back = Vacancy.objects.filter(speciality__code="backend")
print(f"{back =}")
print(f"{back.count() =}")

company_ = Company.objects.filter(id=1)
"""
company_id_title_dict = {}
for spec_ in company_:
     company_id_title_dict[spec_.id_str] = spec_.name

print(f"{company_id_title_dict =}")
"""
print(f"{company_ =}")
for z in company_:
    print(f"{z=}")
    print(f"{z.name=}")

#company_code = Vacancy.objects.filter(company__id_str=id_)
company_code = Vacancy.objects.filter(company__id_str="1")

#back = Vacancy.objects.filter(speciality__code="backend")

print(f"{company_code.count() =}")        

for vacancy in company_code:
    print(f"{vacancy.speciality.code =}")         
    #print(f"{vacancy.skills =}")         
    #print(f"{vacancy.text =}")           
    #print(f"{vacancy.salary_min =}")     
    #print(f"{vacancy.salary_max =}")     
    #print(f"{vacancy.published_at =}")   







