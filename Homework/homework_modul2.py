# 1) Prove "and" operation takes precedence over "or" operation by setting
# parentheses in the following expression (False or False and True or True)
# print ((False or (False and True) or True))


# 2) Get from input two different times in the format dd:hh:mm:ss and print
# the difference in seconds between them. The convert the result back to the initial
# format and print that also
# dd is number of days
# hh si number of hours (00-23)
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)

#
# date_1=input('Enter first date:')
# date_2=input('Enter second date:')
# date_1d=int(date_1[:2])
# date_1h=int(date_1[3:5])
# date_1m=int(date_1[6:8])
# date_1s=int(date_1[9:])
# date1_conv_sec= (86400*date_1d)+(3600*date_1h)+(60*date_1m)+date_1s
# date_2d=int(date_2[:2])
# date_2h=int(date_2[3:5])
# date_2m=int(date_2[6:8])
# date_2s=int(date_2[9:])
# date2_conv_sec=(86400*date_2d)+(3600*date_2h)+(60*date_2m)+date_2s
#
# #calculate time difference
# time_difference= date1_conv_sec-date2_conv_sec
# print(time_difference)
#
# # converting the result to it's initial value
# secs=time_difference
#
# day=secs//86400
# hour=secs//3600%24
# minutes=secs//60%60
# seconds=secs%60
# print(f'{day}:{hour}:{minutes}:{seconds}')
#



# #3 Calculate the diagonal of a rectangle with sides 10 and 15
lenght=15
width=10
result=(lenght**2+width**2)**0.5
print(int(result))
