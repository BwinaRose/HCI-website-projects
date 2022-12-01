import requests as requests

pics = []
call2 = "https://api.waifu.pics/sfw/waifu"
call5 = "https://api.waifu.pics/sfw/bully"
call6 = "https://api.waifu.pics/sfw/cuddle"
call7 = "https://api.waifu.pics/sfw/cry"
call8 = "https://api.waifu.pics/sfw/hug"
call9 = "https://api.waifu.pics/sfw/smug"
call10 = "https://api.waifu.pics/sfw/bonk"
call10 = "https://api.waifu.pics/sfw/smile"
call11 = "https://api.waifu.pics/sfw/yeet"
call12 = "https://api.waifu.pics/sfw/wave"
call13 = "https://api.waifu.pics/sfw/nom"
call14 = "https://api.waifu.pics/sfw/dance"
call15 = "https://api.waifu.pics/sfw/cringe"
response2 = requests.get(call2)
response5 = requests.get(call5)
response6 = requests.get(call6)
response7 = requests.get(call7)
response8 = requests.get(call8)
response9 = requests.get(call9)
response10 = requests.get(call10)
response11 = requests.get(call11)
response12 = requests.get(call12)
response13 = requests.get(call13)
response14 = requests.get(call14)
response15 = requests.get(call15)
jsonData2 = response2.json()
jsonData5 = response5.json()
jsonData6 = response6.json()
jsonData7 = response7.json()
jsonData8 = response8.json()
jsonData9 = response9.json()
jsonData10 = response10.json()
jsonData11 = response11.json()
jsonData12 = response12.json()
jsonData13 = response13.json()
jsonData14 = response14.json()
jsonData15 = response15.json()
pics.append(jsonData2["url"])
pics.append(jsonData5["url"])
pics.append(jsonData6["url"])
pics.append(jsonData7["url"])
pics.append(jsonData8["url"])
pics.append(jsonData9["url"])
pics.append(jsonData10["url"])
pics.append(jsonData11["url"])
pics.append(jsonData12["url"])
pics.append(jsonData13["url"])
pics.append(jsonData14["url"])
pics.append(jsonData15["url"])
