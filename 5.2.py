import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
print('Day:', t1.day)
print('Month:', t1.month)
print('Minute:', t1.minute)
print('Second:', t1.second)
t2 = dt.datetime.now()
diff = t2 - t1
print('Difference:', diff)
print('Difference in days:', diff.days)
print('Difference in seconds:', diff.total_seconds())
print("HÁI QUANG DUY")
