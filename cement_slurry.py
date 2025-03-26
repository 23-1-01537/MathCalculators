def main ():
    V2=float(input("Enter the Volume 2 of the slurry(L):"))
    C2=float(input("Enter the Cement concentration 2 of the slurry(g/L):"))
    C1=float(input("Enter the Cement concentration 1 of the slurry(g/L):"))
    
    V=(C2*V2)/C1
    print(f"So you need {V:.2f} Liters of the original slurry")

if __name__=="__main__":
    main()