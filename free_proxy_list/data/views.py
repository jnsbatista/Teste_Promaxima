from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .forms import DataForm
from .models import Data
from django.db.models import Count

import time

from bs4 import BeautifulSoup

from selenium import webdriver


def dataList(request):
  datas = Data.objects.all().order_by('country')
  return render(request, 'data.html', {'datas': datas})

def newProxy(request):
  
  if request.method == 'POST':
    form = DataForm(request.POST)
    
    if form.is_valid():
      data = form.save()
      data.save()
      return redirect('/')
    
    
  else:  
    form = DataForm()
    return render(request, 'addproxy.html', {'form': form})
  
def editProxy(request, id):
  data = get_object_or_404(Data, pk=id)
  form = DataForm(instance=data)
  
  if(request.method == 'POST'):
    form = DataForm(request.POST, instance=data)
    
    if(form.is_valid()):
      data.save()
      messages.info(request, 'Proxy edited successfully!')
      return redirect('/')
    else:
      return render(request, 'editdata.html', {'form': form, 'data': data})      
      
  else:
    return render(request, 'editdata.html', {'form': form, 'data': data})

def deleteProxy(request, id):
  data = get_object_or_404(Data, pk=id)
  data.delete()
  
  messages.info(request, 'Proxy deleted successfully!')
  return redirect('/')

def colectData(request):
  data_list = []
  
  url = "https://www.freeproxylists.net/"
  
  caminho = "CAMINHO" + "/geckodriver.exe"

  driver = webdriver.Firefox(executable_path=caminho)

  driver.get(url)
  time.sleep(20)
  number_of_pages = len(driver.find_elements_by_xpath("//div[@class='page']/a"))
  nb = int((number_of_pages)/2) + 1
  
  for i in range(1,nb , 1):
    driver.get(url + "?page=" + str(i))
    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find('table',  {'class': 'DataGrid'}).find_all('tr')
    
    for row in rows: 
      try: 
        ip_address = row.find_all('td')[0].get_text()
        port = row.find_all('td')[1].get_text()
        protocol = row.find_all('td')[2].get_text()
        anonymity = row.find_all('td')[3].get_text()
        country = row.find_all('td')[4].get_text()
        region = row.find_all('td')[5].get_text()
        city = row.find_all('td')[6].get_text()
        uptime = row.find_all('td')[7].get_text()
        response = row.find_all('td')[8].find('span').get('style').replace("width:", "").replace(";background:#ffd700;", "").replace(";background:#008000;","").replace(";background:#CC3300;", "")
        transfer = row.find_all('td')[9].find('span').get('style').replace("width:", "").replace(";background:#ffd700;", "").replace(";background:#008000;","").replace(";background:#CC3300;", "")
        data = {
          'ip_address': ip_address,
          'port': port,
          'protocol' : protocol,
          'anonymity': anonymity,
          'country' : country,
          'region' : region,
          'city' : city,
          'uptime' : uptime,
          'response' : response,
          'transfer' : transfer,
        }
        data_list.append(data)
        
      except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
      
    
    time.sleep(10)
      
       
  driver.close()    
  return save_function(data_list)    
  

    

def save_function(data_list):
    new_count = 0

    for data in data_list:
        try:
            Data.objects.create(
              ip_address = data['ip_address'] ,
              port = data['port'] ,
              protocol = data['protocol'] ,
              anonymity =data['anonymity'] ,
              country = data['country'] ,
              region = data['region'] ,
              city = data['city'] ,
              uptime = data['uptime'] ,
              response = data['response'] ,
              transfer = data['transfer'] ,
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
          
    for duplicates in Data.objects.values("ip_address").annotate(
    records=Count("ip_address")
    ).filter(records__gt=1):
        for tag in Data.objects.filter(ip_address=duplicates["ip_address"])[1:]:
            tag.delete()
    return redirect('/')
  
  