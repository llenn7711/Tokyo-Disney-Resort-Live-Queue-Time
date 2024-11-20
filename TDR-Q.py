import requests
from bs4 import BeautifulSoup
#ディズニーランドの待ち時間URL
url = 'https://tokyodisneyresort.info/realtime.php?park=land&order=area'
#サイトの情報更新時間を取得
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# アトラクション名と状態のリストをそれぞれ取得
names = [name.text.strip() for name in soup.find_all("div", class_="realtime-attr-name")]
times = []
for time in soup.find_all("div", class_="realtime-attr-condition"):
    greeting_timetable = time.find("div", class_="greeting_timetable")
    if greeting_timetable:
        greeting_timetable.extract()  # greeting_timetableのクラスを削除
    times.append(time.text.strip())  # 状態情報をリストに追加

print('ディズニーランドのアトラクション待ち時間')
genzailand = soup.find("h2")
print(genzailand.text)

# アトラクション名と状態を交互に表示
for name, time in zip(names, times):
    print(name)
    print(time)

#ディズニーシーの待ち時間URL
url = 'https://tokyodisneyresort.info/realtime.php?park=sea&order=area'
#サイトの情報更新時間を取得
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# アトラクション名と状態のリストをそれぞれ取得
names = [name.text.strip() for name in soup.find_all("div", class_="realtime-attr-name")]
times = []
for time in soup.find_all("div", class_="realtime-attr-condition"):
    greeting_timetable = time.find("div", class_="greeting_timetable")
    if greeting_timetable:
        greeting_timetable.extract()  # greeting_timetableのクラスを削除
    times.append(time.text.strip())  # 状態情報をリストに追加

print('\n')

print('ディズニーシーのアトラクション待ち時間')
genzailand = soup.find("h2")
print(genzailand.text)

# アトラクション名と状態を交互に表示
for name, time in zip(names, times):
    print(name)
    print(time)


