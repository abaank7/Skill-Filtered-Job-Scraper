import requests 
from bs4 import BeautifulSoup
import time
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 1.  'posts' directory if it doesn't exist
os.makedirs('posts', exist_ok=True)

def find_jobs(unfamiliar_skills):
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation='
    response = requests.get(url,verify=False)

    if response.status_code == 200:
        print("Successfully Fetched the data...")
    else:
        print(f"Unsuccessful in fetching the data... Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs, start=1):
        # Added a try-except block just in case a job posting is missing a date
        try:
            published_date = job.find('span', class_='sim-posted').span.text
        except AttributeError:
            continue

        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text
            company_name = ' '.join(company_name.split())

            skills_element = job.find('span', class_='srp-skills') # Timesjobs uses span, not div
            if not skills_element:
                continue
                
            skills = skills_element.text
            skills = ', '.join(skills.split())
            more_info = job.header.h2.a['href']

            # convert both to lowercase to ensure 'Java' and 'java' match
            contains_unfamiliar = any(
                skill.lower() in skills.lower() 
                for skill in unfamiliar_skills
            )

            # If it DOES NOT contain an unfamiliar skill, we'll save  it
            if not contains_unfamiliar:
                with open(f"posts/{index}.txt", "w") as file:
                    file.write(f'Company Name : {company_name.upper()}\n')
                    file.write(f'Skills Required : {skills}\n')
                    file.write(f'More Info : {more_info}')
                
                print(f"Saved Job {index}: {company_name}")

if __name__ == '__main__':
    #
    unfamiliar_skills = []
    
    try:
        no_of_un_skills = int(input("How many unfamiliar skills you want to filter: "))
        for count in range(no_of_un_skills):
            temp = input(f"Enter Unfamiliar skill {count + 1}: ").strip()
            unfamiliar_skills.append(temp)
    except ValueError:
        print("Please enter a valid number.")
        exit()

    print(f"Filtering out: {unfamiliar_skills}")

    while True:
        find_jobs(unfamiliar_skills)
        time_wait = 10
        print(f'Waiting {time_wait} minutes...\n')
        time.sleep(time_wait * 60)