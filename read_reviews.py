data = []
count = 0
with open ('reviews.txt', 'r') as f: # as 當作
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 100000 == 0: # % 是用來求餘數
			print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len/len(data))	

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於 100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到 Good')
print(good[0])