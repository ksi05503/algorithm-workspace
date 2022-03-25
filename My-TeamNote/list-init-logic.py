#리스트 초기화
list1 = [0] * 10
list2 = [1,2,3]

print("list1: ",list1)
print("list2: ",list2)

print("list2[-1]: ",list2[-1])
print("list2[1:4]: ",list2[1:4])  # 끝인덱스를 표시할때는 1 더해서 사용 (컨벤션)

#리스트 컴프리헨션
list3 = [i*3 for i in range (20) 
            if i % 2 == 0]  #리스트 Comprehension (이중리스트에 유용)
print("list3: ",list3)

list4 = [[0]*3 for _ in range(3)]
print("list4: ", list4)
