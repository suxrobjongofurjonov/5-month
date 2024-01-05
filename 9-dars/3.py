from datetime import datetime
def func(data):

    date=datetime.strptime(data,"%d-%m-%Y")

    start=datetime(date.year, 1, 1)

    diferrence=(date-start).days
    return diferrence

son="17-02-2024"
res= func(son)
print(res)