from work.models import Company, Speciality,Vacancy

# сохранение данных в бд
from data import jobs, companies, specialties 


for firm in companies:
    group = Company()
    group.id_str = firm["id"]
    group.name   = firm["title"]
    group.location = firm["location"]
    #group.logo = firm["logo"]
    group.description == firm["description"]
    group.employee_count = int(firm["employee_count"])
    group.save()

for specia in specialties:
    spec = Speciality()
    spec.code =  specia["code"]
    spec.title = specia["title"]
    #spec.picture =
    spec.save()

"""
weGotId = PlaceType.objects.get(id=id) #и сделать так
info_to_db = Place(place_name = cinema,
                   place_type = weGotId)

ValueError: Cannot assign "'3'": "Vacancy.company" must be a "Company" instance

weGotId = Company.objects.get(id=id)
"""

for job in jobs:
    person = Vacancy()                         
    person.id_str = job["id"]                  
    person.title = job["title"]                  
    person.specialty = job["specialty"]          
    #
    #
    # !!! error ================== 
    #weGotId = Company.objects.get(id_str=person.id_str)
    #print(f"{weGotId=}")
    person.company = job["company"]
    #person.weGotId = int( job["company"])
    #
    # !!! error ================== 
    #
    person.salary_min = int(job["salary_from"])  
    person.salary_max = int(job["salary_to"])    
    person.published_at = job["posted"]          
    person.skills = job["skills"]    
    person.text = job["description"]
    person.save()                              


