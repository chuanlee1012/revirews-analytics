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


# 文字計數

wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典
for word in wc:
	print(word, wc[word])

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過哦!')

print('感謝使用此查詢功能')

