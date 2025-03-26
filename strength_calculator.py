def main ():
    force=float(input("Enter Force applied to the beam (N):"))
    area=float(input("Enter the Cross-sectional Area (mm^2):"))
    
    
    stress=force/area
    print(f"So the stress on the beam is: {stress:.2f} Pascals")

if __name__=="__main__":
    main()