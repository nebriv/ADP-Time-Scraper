import json
import time
from datetime import date, timedelta
import requests
from settings import worker_id

start_dt = date(2016, 2, 27)
end_dt = date(2023, 12, 26)

# Scraping interval
delta = timedelta(days=7)

# Generate the list of dates
dates = []
while start_dt <= end_dt:
    # add current date to list by converting  it to iso format
    dates.append(start_dt.isoformat())
    # increment start date by timedelta
    start_dt += delta

# Load ADP cookies from file (saved from Firefox, right click save all)
with open('cookies.json', 'r') as cookies:
    cookies = json.load(cookies)
    cookies = cookies['Request Cookies']

session = requests.session()

for cookie in cookies:
    session.cookies.set(cookie, cookies[cookie])

time_off = {"vacation": [],
            "sick": []}


for date in dates:
    print(date)
    url = f"https://my.adp.com/myadp_prefix/time/v3/workers/{ worker_id }/time-off-balances?$filter=balanceAsOfDate%20eq%20%27{ date }%27"
    # print(url)
    r = session.get(url)
    # print(r.status_code)
    if r.status_code >= 200 and r.status_code < 300:
        # print(r.text)
        if "timeOffBalances" in r.json():
            for entry in r.json()['timeOffBalances'][0]['timeOffPolicyBalances']:
                if entry['timeOffPolicyCode']['codeValue'] == "Annual Leave":
                    timeoff = entry['policyBalances'][0]['totalTime']['timeValue']
                    time_off['vacation'].append({date:timeoff})
                    print("vacation", timeoff)
                if entry['timeOffPolicyCode']['codeValue'] == "Sick":
                    timeoff = entry['policyBalances'][0]['totalTime']['timeValue']
                    time_off['sick'].append({date:timeoff})
                    print("sick", timeoff)
        else:
            print("Bad JSON?")
            print(r.text)
    else:
        print("Got bad response")
        print(r.text)

    with open("output.json", 'w') as o:
        json.dump(time_off, o, indent=4)