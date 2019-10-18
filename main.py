import src.Calculator as Calculator

def main():
    print("Enter your equation with tokens delimited by spaces.")
    print("For example: 1 + 2")
    print("Type EXIT to quit.")
    print("====================================================")

    c = Calculator.Calculator()
    
    while True:
        eq = input("Equation: ")

        if eq == "EXIT":
            break
        else:
            try:
                c.infix_to_postfix(eq)
                result = c.calculate()
            except:
                print("Invalid Input. Please try again.")
            else:
                print("\t= ",result)
    
if __name__=="__main__":
    main()