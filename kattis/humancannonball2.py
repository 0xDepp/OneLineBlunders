(lambda M:[(lambda v,w,x,y,z:print((''if y+1<=(lambda t:(v*t*M.sin(w*M.pi/180))-(0.5*9.81*(t**2)))(x/(v*M.cos(w*M.pi/180)))<=z-1 else'Not ')+'Safe'))(*list(map(float,input().split())))for _ in range(int(input()))])((__import__('math')))