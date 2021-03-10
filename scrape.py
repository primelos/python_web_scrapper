import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
  # print('HERE IT IS', job_elem, end='\n'*2)
  title_elem = job_elem.find('h2', class_='title')
  company_elem = job_elem.find('div', class_='company')
  location_elem = job_elem.find('div', class_='location')
  if None in (title_elem, company_elem, location_elem):
      # print('?|?|?||?|?|?|?|?|?|?|?||?|?|?', job_elem)
      continue
  print('HERE IT IS ->',title_elem.text.strip())
  print('company_elem ++++++>', company_elem.text.strip())
  print('location_elem ++++++>', location_elem.text)
  print()
  # python_jobs = results.find_all('h2', string='Python Developer')
python_jobs = results.find_all('h2', string=lambda text: 'manager' in text.lower())
print('python_jobs', len(python_jobs))
# print('python_jobs', python_jobs)

for p_job in python_jobs:
  link = p_job.find('a')['href']
  print('text -> ',p_job.text.strip())
  print(f'apply here: {link}\n')
# print(job_elems)
# print(results.prettify())


# print(soup)
