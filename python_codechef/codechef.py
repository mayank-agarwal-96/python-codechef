import requests
from bs4 import BeautifulSoup

class Codechef:


	@staticmethod	
	def get_problems(type):

		url = "https://www.codechef.com/problems"+'/' + type
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
	def get_contests(time):

		url = "https://www.codechef.com/contests"
		page = requests.get(url)
		plain_text = page.text
		soup = BeautifulSoup(plain_text,"html.parser")

		tables = soup.findAll('table',{'class' : 'dataTable'})

		if time == 'present':
			table = tables[0]
		elif time == 'future':
			table = tables[1]

		rows = table.findAll('tr')
		rows = rows[1:]

		contests=[]
		for row in rows:
			data = row.findAll('td')
			link = row.findAll('a')[0]
			
			contest_data = {
				'name' : str(data[0].text),
				'url' : url + str(link.get('href')),
				'start_date' : str(data[2].text),
				'end_date' : str(data[3].text)
			}
			print contest_data
			contests.append(contest_data)
				