# import datetime
# d=datetime.datetime.now()
# print(d)
#     #---------
# print(datetime.datetime(2023,12,28))

#     %b,%B,%m,%y,%Y,%H,%I,%p,%M
import datetime
d=datetime.datetime.now()
m=d.strftime("%p")
print(m)
print(d)
# #     practice
# # import datetime
# # f=datetime.datetime.now()
# # print(f)
# # s=f.strftime("%p")
# # print(s)