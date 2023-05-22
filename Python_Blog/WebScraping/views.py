from django.shortcuts import redirect, render
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    
    URL = "https://www.amazon.in/stores/page/preview?isPreview=1&isSlp=1&asins=B0C21DZ698%2CB0C21K8Y61%2CB0C21LK788%2CB0BW5PZSGJ%2CB0BW5RN77W%2CB0BW5NJR3J%2CB0BW5P7LRW%2CB0BW5NB4J5%2CB0B3MWYCHQ%2CB0BF57RN3K%2CB0BRQFF4HN%2CB0B3RRWSF6%2CB0BJ72WZQ7%2CB0B5LVS732%2CB0C1VSRMSB%2CB0BP18W8TM%2CB0&pf_rd_r=9FS9KNN2NJNCYRB22M05&pf_rd_t=Events&pf_rd_i=deals&pf_rd_p=56e15f58-339a-4d78-b416-b9e8f4b87a90&pf_rd_s=slot-15&ref=dlx_deals_gd_dcl_img_0_cfb977ed_dt_sl15_90"
    
    '''HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})'''
            
            
    ''' results = soup.find_all('a')
    data=[]
    for result in results:
        data.append(result.get('href'))'''
    
    page = requests.get(URL)

    soup =  BeautifulSoup(page.content, "html.parser")          
    
    results = soup.find('ul', attrs={"class":'ProductGrid__grid__f5oba'})  
    data={}
    for result in results:
         data['price'] = result.find('span', attrs={'class':'Price__whole__mQGs5'}).string
         data['title'] = result.find('a', attrs={'data-testid':'product-grid-title'}).string
      
    #return HttpResponse(data.values())
    
    return render(request,'WebScrapping\scrap-data.html',{'data':data.values()})
