from time import localtime, strftime

list1 = ["제주", "제제", "한량"]
# tm = localtime()
# print(strftime('%Y-%m-%d %I:%M:%S %p', tm))


for i in range(1,10):
    tm = localtime()
    print(strftime('%Y-%m-%d %I:%M:%S %p', tm))
    for a in list1:
        print(a)
        
tm = localtime()
print("종료 시간 : "+strftime('%Y-%m-%d %I:%M:%S %p', tm))