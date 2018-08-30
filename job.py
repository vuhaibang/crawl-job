from bs4 import BeautifulSoup
import requests


result = []
for i in range(1,11):
	web = 'https://github.com/awesome-jobs/vietnam/issues?page={}'.format(i)
	page = requests.get(web)
	soup = BeautifulSoup(page.text, 'lxml')
	new = soup.find_all('div', class_="float-left col-9 lh-condensed p-2")
	print(new)
	for n in new:
		a = n.find('a').get('href')
		break
		result.append(a)

with open('job', 'wt') as f:
	for r in result:
		f.write(r + '\n')