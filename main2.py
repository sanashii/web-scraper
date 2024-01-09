from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '') # instead of using soup.find, we can use job.find since we're only trying to find a specific element found in that specific job
# the .replace is used to get rid of the extra white space and exchange them with nothing
skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
date_posted = job.find('span', class_ = 'sim-posted').text

print(f'''
Company Name: {company}
Skills Needed: {skills}
Date Posted: {date_posted}
      ''')
