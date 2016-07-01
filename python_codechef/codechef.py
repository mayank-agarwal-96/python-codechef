import requests
from bs4 import BeautifulSoup

class Codechef:

	@staticmethod
	def get_html(url):
		page = requests.get(url)
		plain_text = page.text
		soup = BeautifulSoup(plain_text,"html.parser")

		return soup

	@staticmethod	
	def get_problems(type):

		url = "https://www.codechef.com/problems"+'/' + type
		soup = Codechef.get_html(url)

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
		soup = Codechef.get_html(url)

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
				

	@staticmethod
	def get_problem_details(code):
		url = "https://www.codechef.com/problems/"+ code
		soup = Codechef.get_html(url)

		content = soup.findAll('div',{'class' : 'content'})
		remove_string = "All submissions for this problem are available. Read problems statements in Mandarin Chinese , Russian and Vietnamese as well."
		statement = content[1].text.encode('utf-8')
		statement = statement.replace(remove_string,"")
		print type(statement)
		data = {
			'statement': statement,
		}

		return data
X = Codechef.get_problem_details('ACBALL')
print X['statement']