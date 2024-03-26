from datetime import datetime, timedelta

def date_now():
    today_date = datetime.now()
    num_people = int(input("请问你要查询几个人:"))
    print(f"\nToday's date: {today_date}")
    return num_people, today_date

def date_input(num_people):
    vaccine_records = []
    for i in range(num_people):
        print(f"\n您好，第{i+1}位用户")
        count = int(input("请输入已经接种了几针："))
        last_date_str = input("请输入最后一次接种日期：(格式为YYYY-MM-DD)")

        if count>0:
            last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
        else:
            num_people, today_date = date_now()    #要返回num_people是必须的，但是可以不用他
            last_date = today_date

        vaccine_records.append({"count": count, "last_date": last_date})

    return vaccine_records

def date_output(vaccine_record,today_date):
    result = []
    for record in vaccine_record:
        count = record["count"]
        last_date = record["last_date"]

        if count == 3:
            result.append({"status": False, "next_date": ""})
        elif count == 0:
            status = 1
            next_date = today_date
            result.append({"status": status, "next_date": next_date})
        elif count == 1:
            interval = 30
            next_date = last_date + timedelta(days=interval)
            status = today_date >= next_date
            result.append({"status": status, "next_date": next_date.strftime("%Y-%m-%d")})

        elif count == 2:
            interval = 180
            next_date = last_date + timedelta(days=interval)
            status = today_date >= next_date
            result.append({"status": status, "next_date": next_date.strftime("%Y-%m-%d")})

        else:
            print("只需接种三针")

    return result

num_people, today_date = date_now()
records = date_input(num_people)
results = date_output(records, today_date)

print("\nVaccination Status:")
for i, result in enumerate(results, start=1):
    print(f"\nPerson {i}:")
    print(f"{result['status']}")
    print(f"下一次接种{result['next_date']}")

















