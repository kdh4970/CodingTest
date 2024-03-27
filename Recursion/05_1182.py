# 부분수열의 합
# 수열의 n개의 원소에 대해 부분수열
# 각 원소에 대해 부분수열로 포함할지 말지

N,S = list(map(int,input().split()))

nums = list(map(int,input().split()))

cnt = 0
def func(curr_idx,total):
    global cnt
    if curr_idx == N:
        if total==S:
            cnt+=1
        return
    func(curr_idx+1,total)
    func(curr_idx+1,total+nums[curr_idx])


func(0,0)
print(cnt-1 if S==0 else cnt) # 공집합 예외