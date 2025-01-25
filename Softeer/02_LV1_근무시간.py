import sys

sum = 0
for _ in range(5):
    w_start,w_end = input().split(" ")
    w_start_h,w_start_m = w_start.split(":")
    w_end_h,w_end_m = w_end.split(":")
    sum += (int(w_end_h) - int(w_start_h)) * 60 + (int(w_end_m) - int(w_start_m))
print(sum)