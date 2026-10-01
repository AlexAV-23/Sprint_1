time_value = '1h 45m,360s,25m,30m 120s,2h 60s'
sum_of_time = 0

list_of_time = time_value.replace(',', ' ').split()
for value in list_of_time:
    if 'h' in value:
        sum_of_time += int(value.replace('h', '')) * 60
    elif 'm' in value:
        sum_of_time += int(value.replace('m', ''))
    else:
        sum_of_time += int(value.replace('s', '')) // 60
        

print(sum_of_time)