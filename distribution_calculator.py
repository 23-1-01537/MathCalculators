def main ():
    w=float(input("Enter the Uniform Load (N/m):"))
    L=float(input("Enter the Length(m):"))
    
    F=w*L
    print(f"So the total load acting on the beam is {F:.2f} Newton.")

if __name__=="__main__":
    main()