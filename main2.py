from bs4 import BeautifulSoup
import requests
import time

print("Enter a skill you are not familiar with")
non_skill = input('> ')
print(f"Filtering out {non_skill}...")

def find_jobs():
      html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text
      soup = BeautifulSoup(html_text, 'lxml')

      jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
      for index, job in enumerate(jobs):
            date_posted = job.find('span', class_ = 'sim-posted').span.text
            if 'few' in date_posted:
                  company = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '') # instead of using soup.find, we can use job.find since we're only trying to find a specific element found in that specific job
                  # the .replace is used to get rid of the extra white space and exchange them with nothing
                  skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
                  link = job.header.h2.a['href'] # nesting between elements to access a speific element inside the container
                  if non_skill not in skills:
                        with open(f'posts/{index}.txt', 'w') as f:
                              f.write(f'Company Name: {company.strip()}\nSkills Needed: {skills.strip()}\nDate Posted: {date_posted}\nLink: {link}')
                        print(f'File saved: {index}')      
                        
if __name__ == '__main__':
      while True:
            find_jobs()
            time_wait = 10
            print(f"Waiting {time_wait} minutes...")
            time.sleep(time_wait *60)