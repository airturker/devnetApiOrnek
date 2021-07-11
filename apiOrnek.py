import requests
import json
usr="cisco"
pswd="Cisco123!"

base_URL="http://library.demo.local/api/v1/"

def tokenAl():
    resp=(requests.post(base_URL+'loginViaBasic',auth=(usr,pswd)).json())
    return(resp['token'])

def Kitaplar():
    r=requests.get(base_URL+'books').json()
    for kitap in r:
        print(kitap['title'])

def KitapEkle(token,kitap):
    baslik={"content-type":"application/json","X-API-KEY":token}
    veri=json.dumps(kitap)
    r=requests.post(base_URL+'books',headers=baslik,data=veri)
    if r.status_code==200:
        print("kitap eklendi...")
    else:
        print(r.text)

k1={"id":665,"title":"siber guvenlik","author":"mujdat erenler"}
jeton=tokenAl()

KitapEkle(jeton,k1)
Kitaplar()
