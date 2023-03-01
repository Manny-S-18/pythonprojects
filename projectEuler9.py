def pythag():
    n=500
    pyth = [(a,b,c) for a in range(1,n+1) for b in range(a,n+1) for c in [1000-a-b] if a**2 + b**2 == c**2]
    print(pyth)
pythag()
