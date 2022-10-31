def bouncing_ball(h, bounce, window):
    count = 1
    if h>0 and 1>bounce>0 and window<h:
        while h > window:
            h = h*bounce
            count +=2
        print(count-2)
    else:
        print(-1)

    # seen = -1
    #
    # if 0 < bounce < 1:
    #     while h > window > 0:
    #         seen += 2
    #         h *= bounce
    #
    # return seen

bouncing_ball(30, 0.66, 1.5)