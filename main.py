from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://www.gov.br/receitafederal/pt-br/assuntos/agenda-tributaria/agenda-tributaria-2022/janeiro-2022/dia-05-01-2022")

bs = BeautifulSoup(html, 'html.parser')
lines = bs.find_all('tr',{'class':'even'})

# print(bs.prettify())
for i in lines:
    print(i.text)
    
codigo, descricao, periodo = [], [], []
for i in lines:
    children = i.findChildren("td")
    codigo.append(children[0].text)
    descricao.append(children[1].text)
    periodo.append(children[2].text)
    
df = pd.DataFrame({'Código': codigo, 'Descrição': descricao, 'Período': periodo})
df.head()
df.to_excel('plan.xlsx')