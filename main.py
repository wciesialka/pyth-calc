import src.Calculator as Calculator
import sys

def main(args):
    if len(args) == 1:
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
    else:
        equation = " ".join(args[1:])
        c = Calculator.Calculator()
        try:
            c.infix_to_postfix(equation)
            result = c.calculate()
        except Exception as ex:
            print("Invalid Input:\n\t",ex,"\nMake sure your equation is balanced and space delimited.")
        else:
            print(result)
    
if __name__=="__main__":
    main(sys.argv)