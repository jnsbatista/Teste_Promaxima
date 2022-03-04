from bs4 import BeautifulSoup


import requests

def getDataList():
  data_list = []

  url = "https://economizaalagoas.sefaz.al.gov.br/exibicaoPrecoCombustivel.htm?codTipoCombustivel=1"

  res = requests.get(url)

  html_page = res.text
  soup = BeautifulSoup(html_page, 'html.parser')
  soup.prettify()

  gasolinas = soup.find("div", {"class":"page-content"}).find("div", attrs={"style":"width:auto; display:table"}).find_all("div", {"class" : "cartao mdl-card mdl-shadow--2dp"})


  for gasolina in gasolinas:
    
    titulo = gasolina.find("h6", {"class":"cartao_titulo_texto mdl-card__title-text"}).get_text()
    
    litro = gasolina.find("div", {"class":"bloco_venda_esquerdo"}).find("span" , {"class":"valor_unitario"}).get_text().replace("  ", "")
    
    ultima_venda = gasolina.find("div", {"class":"bloco_venda_direito"}).find("span" , {"class":"valor_ultima_venda"}).get_text().replace("  ", "")
    
    tempo_ultima_venda = gasolina.find("div", {"class":"bloco_venda_direito"}).find("span" , attrs={"style":'font-size:x-small'}).next_sibling.next_sibling.next_sibling.get_text()
    
    nome_empresa = gasolina.find("div", {"cartao_contribuinte_bloco_esquerdo"}).br.previous_sibling.get_text().replace("  ", "")
    
    endereco = gasolina.find("div", {"class":"cartao_contribuinte_bloco_esquerdo"}).br.next_sibling.get_text().replace("  ", "")
    
    cidade = gasolina.find("div", {"class":"cartao_contribuinte_bloco_esquerdo"}).br.next_sibling.next_sibling.next_sibling.get_text().replace("  ", "")
    
    data = {
              'titulo': titulo,
              'litro': litro,
              'ultima_venda' : ultima_venda,
              'tempo_ultima_venda': tempo_ultima_venda,
              'nome_empresa' : nome_empresa,
              'endereco' : endereco,
              'cidade' : cidade,
            }

    data_list.append(data)
  print(data_list)
  return data_list
