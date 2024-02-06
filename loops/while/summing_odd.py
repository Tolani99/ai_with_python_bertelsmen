num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
sum = 0
count = 0
for i in range(len(num_list)):
	if num_list[i] % 2 != 0 and count < 5:
		sum += num_list[i]
		count += 1
print(sum)
		
