import json
words_for_technology = [
    "it technician",
    'information',
    "engineer",
    "tester",
    "developer",
    "security",
    "security specialist",
    "computer",
    "system",
    "network",
    "software",
    "graphic designer",
    'designer'
    "database",
    "data",
    "data scientist",
    "cloud",
    "management information systems",
]

words_administration_business_management = [
    "Administrator", "Business development", "Civil service administrative",
    "Compliance officer", "European Union official", "Health service manager",
    "government", "Management consultant", "Operational researcher",
    "Receptionist", "Scrum Master", "officer", "rental", "agent", "Civil",
    "Health and safety adviser", "adviser", "Human resources adviser",
    "Local government officer", "Medical secretary", "Procurement Manager",
    "Recruitment", "Secretary", "Charity fundraiser", "secretary", "Health records clerk",
    "Member of Parliament (MP)", "Project manager"
]


def catagorise_jobs():
    json_file = open(
        "/Users/asilbekturgunboev/Desktop/upwork/second_project/telegram_hr_bot/test.json")

    data = json.load(json_file)
    for j in words_for_technology:
        for i in data['jobs']:
            for k, v in i.items():
                if j in v.lower():
                    print(i)
                else:
                    pass
                # print(any(job_list) == "food")
                # if j in words_for_technology:
                #     print(j)


catagorise_jobs()
