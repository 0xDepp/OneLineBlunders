[(lambda p:print((lambda v:v if[(lambda w,x,y,z:v.__setitem__(0,v[0]+abs(w*z-x*y)/2))(*[j[0]-v[1],j[1]-v[2],k[0]-v[1],k[1]-v[2]])for j,k in zip(p[1:],p[2:])]else 0)([0,*p[0]])[0]))((lambda s:[(s[i],s[i+1])for i in range(1,(s[0]*2)+1,2)])([*map(int,input().split())]))for _ in range(int(input()))]	