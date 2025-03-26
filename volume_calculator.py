def main ():
    L=float(input("Enter the Length (m):"))
    W=float(input("Enter the Width (m):"))
    D=float(input("Enter the Depth(m):"))
    
    V=L*W*D
    print(f"So you need {V:.2f} cubic meters of concrete")

if __name__=="__main__":
    main()