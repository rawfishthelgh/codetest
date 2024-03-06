def solution(n, left, right):
    nums = []
    for i in range(left,right+1):
        idx = i % n
        cnt = i // (n)
        # print("i:",i)
        # print("idx:",idx)
        # print("cnt:",cnt)
        if cnt <= idx :
            nums.append(idx+1)
        else:
            # print("go")
            nums.append(cnt+1)
        
        
    return nums