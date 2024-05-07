
import sys
input = sys.stdin.readline

t = int(input())

while t > 0 :
    t -= 1
    n = int(input())
    stocks = list(map(int,input().split()))
    ans = 0

    max_stock_price = 0
    for i in range(len(stocks)-1,-1,-1) :
        
        if stocks[i] > max_stock_price :
            max_stock_price = stocks[i]
        else :
            ans += max_stock_price - stocks[i]
        

    print(ans)
