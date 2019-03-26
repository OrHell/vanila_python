import requests, bs4
from os import system


def main():
	s=requests.get('https://orhell.github.io')
	b=bs4.BeautifulSoup(s.text, "html.parser")
	p3=b.select('.pon')
	poned=p3[0].getText()
	print(poned)
	system("pause")
if __name__ == '__main__':
    main()



