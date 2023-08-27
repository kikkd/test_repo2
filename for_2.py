from time import localtime, strftime

class timest:
    def time_strt():
        tm = localtime()
        print("시간시간 : "+strftime('%Y-%m-%d %I:%M:%S %p', tm))
    def time_end():
        tm = localtime()
        print("종료시간 :" +strftime('%Y-%m-%d %I:%M:%S %p', tm))

if __name__ == "__main__":
    list1 = ["제주", "제제", "한량"]
    # tm = localtime()
    # print(strftime('%Y-%m-%d %I:%M:%S %p', tm))

    timest.time_strt()
    i = 10
    while i > 0:
        for a in list1:
            print(f"{a=}")  
        i -= 1  
    # for i in range(1,10):
    #     for a in list1:
    #         print(f"{a=}")

    timest.time_end()