import csv
import pandas as pd
import sys
import itertools
import math
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("待ち時間").sheet1

# Extract and print all of the values
rows = sheet.get_all_records()

df = pd.DataFrame.from_records(rows)
print(df)

atraction_name = ["美女と野獣_魔法の物語", "スプラッシュマウンテン", "ベイマックスのハッピーランド",
                  "ビッグサンダーマウンテン", "ホーンテッドマンション", "プーさんのハニーハント",
                  "バズ・ライトイヤーのアストロブスター", "スペース・マウンテン", "ピーターパン空の旅",
                   "空飛ぶダンボ", "モンスターズ・インク_ライド&ゴーシーク!", "ロジャーラビットのカートゥーンスピン",
                   "イッツ・ア・スモールワールド", "ジャングルクルーズ"]

df = pd.read_csv('time.csv')
df_map = pd.read_csv("map.csv", index_col = 0)
print("現在の時刻を入力してね")
hour = input("何時? ")
minute = input("何分? ")
print("現在位置付近のアトラクションを1つ、乗りたいアトラクションを3つ選んでね")
print("美女と野獣_魔法の物語 1", end = "  ")
print("スプラッシュマウンテン 2")
print("ベイマックスのハッピーランド 3", end = "  ")
print("ビッグサンダーマウンテン 4")
print("ホーンテッドマンション 5", end = "  ")
print("プーさんのハニーハント 6")
print("バズ・ライトイヤーのアストロブスター 7", end = "  ")
print("スペース・マウンテン 8")
print("ピーターパン空の旅 9", end = "  ")
print("空飛ぶダンボ 10")
print("モンスターズ・インク_ライド&ゴーシーク! 11", end = "  ")
print("ロジャーラビットのカートゥーンスピン 12")
print("イッツ・ア・スモールワールド 13", end = "  ")
print("ジャングルクルーズ 14")

present_location = atraction_name[int(input()) - 1]
atraction_1 = atraction_name[int(input()) - 1]
atraction_2 = atraction_name[int(input()) - 1]
atraction_3 = atraction_name[int(input()) - 1]

df_atraction = df.loc[:, ["time", atraction_1, atraction_2, atraction_3]]
go_atraction = [atraction_1, atraction_2, atraction_3]
df_atraction_permutation = list(itertools.permutations(go_atraction, 3))

current_time = int(hour) + float(minute) / 60.0

min_wait = 10000
best_atraction = 0

time_index = df_atraction.index[(df_atraction["time"] - current_time).abs().argsort()][0].tolist()

for i in df_atraction_permutation:
    store_wait = 0.0
    current_time = int(hour) + float(minute) / 60.0
    map_number = 0
    map_point = 0.0
    store_map = atraction_1
    sum = 0.0

    for j in i:
        map_number += 1
        current_time += store_wait / 60.0
        time_index = df_atraction.index[(df_atraction["time"] - current_time).abs().argsort()][0].tolist()
        store_wait += df_atraction.loc[time_index][j]
        
        if map_number == 1:
            map_point += math.sqrt((df_map.loc["x", j] - df_map.loc["x", present_location]) ** 2 + (df_map.loc["y", j] - df_map.loc["y", present_location]) ** 2)

        if map_number > 1:
            map_point += math.sqrt((df_map.loc["x", j] - df_map.loc["x", store_map]) ** 2 + (df_map.loc["y", j] - df_map.loc["y", store_map]) ** 2)
        store_map = j

    sum = store_wait + map_point / 10.0
    if(sum < min_wait):
        min_wait = sum
        best_atraction = i
    
    print(store_wait," ",  map_point, " ", sum)
    print
    print(i)
    
current_time = int(hour) + float(minute) / 60.0

print("現在時刻 " + str(int(current_time)) + ":" + str(int(((current_time - int(current_time)) * 60))))
print("現在位置 " + present_location)
print("回る順番")
number = 1
for i in best_atraction:
    time_index = df_atraction.index[(df_atraction["time"] - current_time).abs().argsort()][0].tolist()
    print(str(number) + "番目 " + str(i), end = " ")
    print("待ち時間" +  str(int(df_atraction.loc[time_index][i])) + "分", end = " ")
    print("アトラクション終了時刻" +str(int(current_time + df_atraction.loc[time_index][i] / 60.0)) + ":" + str(int((current_time + df_atraction.loc[time_index][i] / 60.0 - int(current_time + df_atraction.loc[time_index][i] / 60.0)) * 60)))
    current_time += df_atraction.loc[time_index][i] / 60.0
    number += 1

