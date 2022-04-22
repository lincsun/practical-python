<<<<<<< HEAD
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
=======
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
>>>>>>> c3b3606b64174eb1de08a843a8ae3b06bdb6414d
