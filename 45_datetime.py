import datetime

DT = datetime.datetime
print(DT.now())                         # 2021-09-20 14:18:02.000000
print(DT.now().date())                  # 2021-09-20
print(DT.now().time())                  # 14:18:02.000000
print(DT.now().year)                    # 2021
print(DT.now().month)                   # 9
print(DT.now().day)                     # 20
print(DT.now().hour)                    # 14
print(DT.now().minute)                  # 18
print(DT.now().second)                  # 2
print(DT.now().microsecond)             # 0
print(DT.now().isoformat())             # 2021-09-20T14:18:02.000000
print(DT.now().ctime())                 # Mon Sep 20 14:18:02 2021
print(DT.now().strftime("%Y-%m-%d %H:%M:%S"))       # 2021-09-20 14:18:02