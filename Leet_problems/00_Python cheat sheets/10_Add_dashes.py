import time

start_time = time.time()


def dashes(line, symbol="x", replace="--"):
    new_line = ""
    if len(line) > 0:
        for i in range(len(line)):
            if line[i] == symbol:
                pre = replace + line[i]
            else:
                pre = line[i]
            new_line = new_line + pre
    else:
        print("Empty string")
    print(new_line)


test_1 = ""
test_2 = "x"
test_3 = "xx1"
test_4 = "erwer"
test_5 = "xAwwxeexpx"
test_6 = "xeexwewerexxxxxxxxxxxeexxxxxxxxxxx32343eeexxxxxxxxxeex"

dashes(test_5)

print("--- %s seconds ---" % (time.time() - start_time))
