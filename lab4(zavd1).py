text = input()
print(*filter(lambda x : text.count(x) > 1 , set(text)) )
