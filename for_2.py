from time import localtime, strftime

class timest:
    def time_st(st):
        tm = localtime()
        print(st+strftime('%Y-%m-%d %I:%M:%S %p', tm))
    def time_strt():
        timest.time_st("시작 시간 : ")
    def time_end():
        timest.time_st("종료 시간 : ")

if __name__ == "__main__":
    list1 = ["제주", "제제", "한량"]
    # tm = localtime()
    # print(strftime('%Y-%m-%d %I:%M:%S %p', tm))

    timest.time_strt()
    for i in range(1,10):
        for a in list1:
            print(a)

    timest.time_end()