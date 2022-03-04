from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .forms import DataForm
from .models import Data
from django.db.models import Count

from bs4 import BeautifulSoup

import requests as rq



def dataList(request):
  datas = Data.objects.all().order_by('tipo')
  return render(request, 'data.html', {'datas': datas})

def newGasolina(request):
  
  if request.method == 'POST':
    form = DataForm(request.POST)
    
    if form.is_valid():
      data = form.save()
      data.save()
      return redirect('/')
    
    
  else:  
    form = DataForm()
    return render(request, 'addgasolina.html', {'form': form})
  
def editGasolina(request, id):
  data = get_object_or_404(Data, pk=id)
  form = DataForm(instance=data)
  
  if(request.method == 'POST'):
    form = DataForm(request.POST, instance=data)
    
    if(form.is_valid()):
      data.save()
      messages.info(request, 'Gasolina editada com sucesso!')
      return redirect('/')
    else:
      return render(request, 'editdata.html', {'form': form, 'data': data})      
      
  else:
    return render(request, 'editdata.html', {'form': form, 'data': data})

def deleteGasolina(request, id):
  data = get_object_or_404(Data, pk=id)
  data.delete()
  
  messages.info(request, 'Gasolina deletada com sucesso!')
  return redirect('/')

def colectData(request):
  data_list = []
  
  for ti in range(1, 7, 1):
    url = "https://economizaalagoas.sefaz.al.gov.br/exibicaoPrecoCombustivel.htm?codTipoCombustivel=" + str(ti)

    print(url)
    res = rq.get(url)

    html_page = res.text
    soup = BeautifulSoup(html_page, 'html.parser')
    soup.prettify()

    gasolinas = soup.find("div", {"class":"page-content"}).find("div", attrs={"style":"width:auto; display:table"}).find_all("div", {"class" : "cartao mdl-card mdl-shadow--2dp"})


    for gasolina in gasolinas:
      try:
        tipo = gasolina.find("h6", {"class":"cartao_titulo_texto mdl-card__title-text"}).get_text()
        
        litro = gasolina.find("div", {"class":"bloco_venda_esquerdo"}).find("span" , {"class":"valor_unitario"}).get_text().replace("  ", "").replace("R$", "")
        
        ultima_venda = gasolina.find("div", {"class":"bloco_venda_direito"}).find("span" , {"class":"valor_ultima_venda"}).get_text().replace("  ", "").replace("R$", "")
        
        tempo_ultima_venda = gasolina.find("div", {"class":"bloco_venda_direito"}).find("span" , attrs={"style":'font-size:x-small'}).next_sibling.next_sibling.next_sibling.get_text()
        
        nome_empresa = gasolina.find("div", {"cartao_contribuinte_bloco_esquerdo"}).br.previous_sibling.get_text().replace("  ", "")
        
        endereco = gasolina.find("div", {"class":"cartao_contribuinte_bloco_esquerdo"}).br.next_sibling.get_text().replace("  ", "")
        
        cidade = gasolina.find("div", {"class":"cartao_contribuinte_bloco_esquerdo"}).br.next_sibling.next_sibling.next_sibling.get_text().replace("  ", "")
        
        data = {
                  'tipo': tipo,
                  'litro': litro,
                  'ultima_venda' : ultima_venda,
                  'tempo_ultima_venda': tempo_ultima_venda,
                  'nome_empresa' : nome_empresa,
                  'endereco' : endereco,
                  'cidade' : cidade,
                }
        data_list.append(data)
        
      except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
    
  return save_function(data_list)  

def save_function(data_list):
    new_count = 0

    for data in data_list:
      try:
        Data.objects.create(
          tipo = data['tipo'],
          litro = data['litro'],
          ultima_venda = data['ultima_venda'],
          tempo_ultima_venda =data['tempo_ultima_venda'],
          nome_empresa = data['nome_empresa'],
          endereco = data['endereco'],
          cidade = data['cidade'],
        )
        new_count += 1
      except Exception as e:
        print('failed at latest_article is none')
        print(e)  
        
    for duplicates in Data.objects.values("nome_empresa", "tipo").annotate(
    records=Count("nome_empresa" and "tipo")
    ).filter(records__gt=1):
      for tag in Data.objects.filter(nome_empresa=duplicates["nome_empresa"], tipo=duplicates["tipo"])[1:]:
          tag.delete()
    return redirect('/')
  
  