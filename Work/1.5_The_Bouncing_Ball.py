# The Bouncing Ball
#
# exercise 1.5

def bounce_cal(init_height, bounce_cnt):
    cnt = 0
    while cnt < bounce_cnt:
        init_height *= 3 / 5
        cnt += 1
        print(cnt, round(init_height, 4))


if __name__ == '__main__':
    bounce_cal(100.0, 10)
