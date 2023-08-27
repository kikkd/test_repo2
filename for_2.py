from time import localtime, strftime

class timest:
    def time_st(str1):
        stra = str(str1)
        tm = localtime()
        print(stra+strftime('%Y-%m-%d %I:%M:%S %p', tm))

if __name__ == "__main__":
    list1 = ["제주", "제제", "한량"]
    # tm = localtime()
    # print(strftime('%Y-%m-%d %I:%M:%S %p', tm))

    time_st1 = timest.time_st
    time_st1("코드 시작시간 : ")
    for i in range(1,10):
        for a in list1:
            print(a)

    time_st1("코드 종료시간 : ")