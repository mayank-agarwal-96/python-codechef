import requests
from bs4 import BeautifulSoup

class Codechef:


	@staticmethod	
	def get_beginner_problems():
		url = "https://www.codechef.com/problems/school"
		page = requests.get(url)
		plain_text = page.text
		soup = BeautifulSoup(plain_text,"html.parser")

		table = soup.findAll('table',{'class' : 'dataTable'})[0]
		rows = table.findAll('tr',{'class' : 'problemrow'})
		
		problems = []
		for row in rows:
			data = row.findAll('a')

			problem_data = {
				'name' : str(data[0].text).strip('\n'),
				'url' : str(url+data[0].get('href')),
				'code' : str(data[1].text),
				'submit_url' : str(url+data[1].get('href')),
				'status' : str(data[2].text)
			}
			problems.append(problem_data)

		return problems

	
	@staticmethod
	def get_easy_problems():
		url = "https://www.codechef.com/problems/easy"
		page = requests.get(url)
		plain_text = page.text
		soup = BeautifulSoup(plain_text,"html.parser")

		table = soup.findAll('table',{'class' : 'dataTable'})[0]
		rows = table.findAll('tr',{'class' : 'problemrow'})
		
		problems = []
		for row in rows:
			data = row.findAll('a')

			problem_data = {
				'name' : str(data[0].text).strip('\n'),
				'url' : str(url+data[0].get('href')),
				'code' : str(data[1].text),
				'submit_url' : str(url+data[1].get('href')),
				'status' : str(data[2].text)
			}
			problems.append(problem_data)

		return problems 


	@staticmethod
	def get_medium_problems():
		url = "https://www.codechef.com/problems/medium"
		page = requests.get(url)
		plain_text = page.text
		soup = BeautifulSoup(plain_text,"html.parser")

		table = soup.findAll('table',{'class' : 'dataTable'})[0]
		rows = table.findAll('tr',{'class' : 'problemrow'})
		
		problems = []
		for row in rows:
			data = row.findAll('a')

			problem_data = {
				'name' : str(data[0].text).strip('\n'),
				'url' : str(url+data[0].get('href')),
				'code' : str(data[1].text),
				'submit_url' : str(url+data[1].get('href')),
				'status' : str(data[2].text)
			}
			problems.append(problem_data)

		return problems


	@staticmethod
	def get_hard_problems():
		url = "https://www.codechef.com/problems/hard"
		page = requests.get(url)
		plain_text = page.text
		soup = BeautifulSoup(plain_text,"html.parser")

		table = soup.findAll('table',{'class' : 'dataTable'})[0]
		rows = table.findAll('tr',{'class' : 'problemrow'})
		
		problems = []
		for row in rows:
			data = row.findAll('a')

			problem_data = {
				'name' : str(data[0].text).strip('\n'),
				'url' : str(url+data[0].get('href')),
				'code' : str(data[1].text),
				'submit_url' : str(url+data[1].get('href')),
				'status' : str(data[2].text)
			}
			problems.append(problem_data)

		return problems  