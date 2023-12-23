# from collections import namedtuple

# color=namedtuple('color',['red','green','blue'])
# rgb_colors=color(235,64,52)
# print(rgb_colors)
# rgb_color={'red':235,'green':64,'blue':52}
# print(rgb_color['red'])

# user=namedtuple('User',['name','age','location'])
# def get_user():
#     return[
#         user('Boburjon',25,'Fergana'),
#         user('Suxrob',16,'Toshkent'),
#         user('Diyorbek',16,'Kirgili')
#     ]
    
# for i in get_user():
#     print(f'{i.name} is {i.age} years old from {i.location}')

### DATETIME ###
import datetime
# data=datetime.date.today()
# #weekday bn isoweekdaydi farqi weekday 0dan boshlanadi yakshanba=6, isoweekday 1dan  boshlanadi yakshanba=7
# print(data.isoweekday())
# data=datetime.date.today()
########################
# tdelta=datetime.timedelta(days=7)
# print(data-tdelta)
########################
# tkun=datetime.date(2024,2,17)
# print(tkun-data)
########################
# data=datetime.datetime(2023,12,19,17,8,48,100)
# print(data)
# data=datetime.datetime.now()
# print(data)
import pytz
# data=datetime.datetime.now(tz=pytz.timezone('Asia/Tashkent'))
# eng_date='December 19, 2023'
# date=datetime.datetime.strptime(eng_date, '%B %d, %Y')
# print(date)

# print(data.strftime('%B %d, %Y - %H-%M-%S, %A, %w'))
# dt_now=datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)
# for i in pytz.all_timezones:
#     print(i)
# dt_utc=dt_now.astimezone(pytz.timezone('Asia/Samarkand'))
# print(dt_utc)
# dt_today=datetime.datetime.today()
# dt_now=datetime.datetime.now(tz=pytz.UTC)
# dt_utc=datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utc)