import requests

url = 'https://footballapi.pulselive.com/football/fixtures?comps=1&teams=2&compSeasons=418&page=0&pageSize=40&sort=asc&statuses=U,L&altIds=true'

aurl = 'https://footballapi.pulselive.com/football/fixtures?comps=1&teams=1,2,130,131,43,4,6,7,9,26,10,11,12,23,14,20,21,33,25,38&compSeasons=418&page=0&pageSize=40&sort=asc&statuses=U,L&altIds=true'

headers = { 
    "Authority": "footballapi.pulselive.com",
    "Method": "GET",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.premierleague.com",
    "Referer": "https://www.premierleague.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

epl_fix = requests.get(url, headers=headers)
epl = requests.get(aurl, headers=headers)


print(epl.url)

