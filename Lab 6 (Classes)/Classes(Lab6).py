# Ray Sahi
# CIS 298
# Class

class FractionHandler:
    # Init Function
    def __init__(self):
        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2
   
    # GCD Function
    def gcd(self, a, b):
        if (a == 0):
            return b
        return self.gcd(b % a, a)

    # Simplest Form  Function
    def simplest(self, num, den):

        # if numerator is 0 
        if (num == 0):
            print(num)
            return

        # Reduce
        common = self.gcd(abs(num), den)
        den = int(den / common)
        num = int(num / common)
        
        # Whole number
        if (den == 1):
            print(num)
        else:  
            print(num, "/", den)

    # Add Function
    def addFraction(self, num1, den1, num2, den2):
        
        # Find GCD of denominators
        den3 = self.gcd(den1, den2)
        # LCM = a * b / GCD
        den3 = (den1 * den2) / den3
        num3 = ((num1) * (den3 / den1) + (num2) * (den3 / den2))

        # Convert to simplest form
        self.simplest(num3, den3)

    # Subtract Function
    def subtractFraction(self, num1, den1, num2, den2):
        
        # Find GCD of denominators
        den3 = self.gcd(den1, den2)
        # LCM = a * b / GCD
        den3 = (den1 * den2) / den3
        num3 = ((num1) * (den3 / den1) - (num2) * (den3 / den2))

        # Convert to simplest form
        self.simplest(num3, den3)

    # Multiplication Function
    def multiplyFraction(self, num1, den1, num2, den2):

        # Multiply numerators and denominators
        num3 = num1 * num2
        den3 = den1 * den2

        # Convert to simplest form
        self.simplest(num3, den3)

    # Division Function
    def divideFraction(self, num1, den1, num2, den2):

        # Flip the guy and multiply
        num3 = num1 * den2
        den3 = den1 * num2

        # Convert to simplest form
        self.simplest(num3, den3)
  
  
    def findFraction(self, frac):
  
        # Index = /
        index = frac.find('/')

        # Index automatically assigned -1
        if (index != -1):
            num = frac[:index]
            den = frac[index+1:]

            # Negative check
            ind1 = num.find('-')
            ind2 = den.find('-')
            
            # Non-negative
            if (ind1 == -1 and ind2 == -1):
                num = int(num)
                den = int(den)
            
            # Negative numerator
            elif (ind1 != -1 and ind2 == -1):
                num = int(num[ind1+1:])
                num = -1 * num
                den = int(den)

            # Negative denominator   
            elif (ind1 == -1 and ind2 != -1):
                num = int(num)
                num = -1 * num
                den = int(den[ind2+1:])

            # Both Negative
            else:
                num = int(num[ind1+1:])
                den = int(den[ind2+1:])

        # Whole number
        else:
            num = frac
            den = 1
            # Negative check
            ind=num.find('-')
            if (ind != -1):
                num = int(num[ind+1:])
                num = -1 * num
            else:
                num = int(num)           
        return num, den


test1 = FractionHandler()

# while loop goes until user quits
loop_control = True
while (loop_control):
    try:
        choice=input("Press any number to continue, press 0 to exit.")
        if (choice == '0'):
            print("Thanks for using the fraction calculator!\n")
            loop_control = False
        elif (choice.isalpha()):
            raise ValueError("Please only use numbers keys to continue, 0 to quit.\n")
        else:
            frac1=input("Enter the first fraction:\n")
            frac2=input("Enter the second fraction:\n")

            # Splicing String to get numerator and denominator for both fractions
            test1.num1, test1.den1 = test1.findFraction(frac1)
            test1.num2, test1.den2 = test1.findFraction(frac2)


            print("Enter which operation would you like to perform?")
            fmenu = input("Enter any of these char for specific operation +,-,*,/: ")
      
            if fmenu == '+':
                print(test1.num1, "/", test1.den1, " + ", test1.num2, "/", test1.den2, " == ")
                test1.addFraction(test1.num1, test1.den1, test1.num2, test1.den2)
            elif fmenu == '-':
                print(test1.num1, "/", test1.den1, " - ", test1.num2, "/", test1.den2, " == ")
                test1.subtractFraction(test1.num1, test1.den1, test1.num2, test1.den2)
            elif fmenu == '*':
                print(test1.num1, "/", test1.den1, " * ", test1.num2, "/", test1.den2, " == ")
                test1.multiplyFraction(test1.num1, test1.den1, test1.num2, test1.den2)
            elif fmenu == '/':
                print(test1.num1, "/", test1.den1, " / ", test1.num2, "/", test1.den2, " == ")
                test1.divideFraction(test1.num1, test1.den1, test1.num2, test1.den2)
            else:
                print("Invalid Input.")

    except ValueError as excpt_val:
        print("Please only use the number keys within your fraction.")