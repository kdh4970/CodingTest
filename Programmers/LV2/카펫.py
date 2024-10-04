### Attempt 1 : 24.10.04
### Time : 2122 ~ 2147 (25m)

### solution
# w,h 타일에 대해, 전체 면적은 wh
# 브라운 면적은 2w + 2h - 4, 옐로 면적은 전체 - 브라운 = wh-b
# b = 2w + 2h - 4, y = wh - b
# w=(y+b)/h, w= (b-2h+4)/2
# 2y+2b=hb-2h^2+4h -> 2h^2-(4+b)h+2y+2b =0
# h 근의 공식 -> h= ((4+b)-sqrt((4+b)**2)-8(2y+2b)))/4
from math import sqrt

def solution(b, y):
    h1=((4+b)-sqrt(((4+b)**2)-8*(2*y+2*b)))//4
    h2=(((4+b)+sqrt(((4+b)**2)-8*(2*y+2*b)))//4)
    if h1>=h2: return [h1,h2]
    else: return [h2,h1]