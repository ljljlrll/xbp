from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

event_date = input("YYYY-MM-DD TI:MEでイベントの日付を入力してください")#入力例 2023-11-06 15:45
today = input("YYYY-MM-DDで今日の日付を入力してください") #入力例 2023-12-25

# イベントまでの日数を計算
time_until_event = event_date - today
print(f"イベントまで {time_until_event} 残り")

# イベント日を変更
new_event_date = event_date + relativedelta(days=7)
print(f"イベント日を変更: {new_event_date}")
