from data import jobs, companies, specialties 

for job in jobs:
    #print( f"{job =}")
    print( f'{job["id"] } \
             {job["title"]} \
             {job["specialty"]} \
             {job["company"]}   \
             {job["salary_from"]}\
             {job["salary_to"]} \
             {job["posted"]}    \
             {job["skills"]}    \
             {job["description"]}')


for firm in companies:
    group = Company()
    group.id_str = firm["id"]
    group.name   = firm["title"]
    group.location = firm["location"]
    #group.logo = firm["logo"]
    group.description == firm["description"]
    group.employee_count = int(firm["employee_count"])
    group.save()

