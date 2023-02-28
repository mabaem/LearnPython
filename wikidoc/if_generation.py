year = int(input('당신의 출생년도를 입력하세요 : '))

print('당신은 ')

if year <= 1924:
    print('가장 위대한 세대')
elif year <= 1945:
    print('침묵 세대')
elif year <= 1980:
    print('X세대')
elif year <= 1996:
    print('밀레니얼')
else:
    print('Z세대')
    
print('입니다')
