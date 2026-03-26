mode = input("enter type of calculator: ")

def tokenize():
    a = "2x+2x^4+2"
    b=a.split('+')

    terms=[]
    coeff = []
    cons = []
    var = []

    print("the terms are:",b)

    for i in b:
        for x in i:
            terms.append(x)

    for i in range(len(terms)):
        if terms[i] == "x":
            terms[i] = "5"
    print("the digits are:",terms)

    for i in terms:
        if i.isdigit():
            i=int(i)
            cons.append(i)
            print(i,"is an int")
        
        else:
            var.append(i)
            print(i)
    print("the constants are:",cons)
    print(f"{cons[0]*cons[1]}+{cons[2]*(cons[3]**cons[4])}+{cons[5]}")
    print("the variables are:",var)

#Basic Math Functions
class Math:
    def __init__(self):
        operations = (("add", "sub", "mul", "div"),
                ("log", "fact", "square", "root"))

        for collection in operations:
            for operation in collection:
                print(operation, end= " ")
            print()
        self.a = int(input('enter a num: '))
        self.op = input('enter a operation: ')
        
    def Add(self):
        self.Add = int(input('enter a num: '))
        add = self.a + self.Add
        print(add)

    def Sub(self):
        self.Sub = int(input('enter a num: '))
        sub = self.a - self.Sub
        print(sub)

    def Mul(self):
        self.Mul = int(input('enter a num: '))
        mul = self.a * self.Mul
        print(mul)

    def Div(self):
        self.Div = int(input('enter a num: '))
        div = self.a / self.Div
        print(div)

    def Fact(self):
        factorial = 1
        for i in range(1, self.a + 1):
            factorial *= i
        print(factorial)

    def Log(self):
        def floatRange(start,stop,step):
            while start<stop:
                yield start
                start+=step

        a = (input("enter num to find the log of: "))
        x=0.0000
        logA=0

        if a.isdigit():
            v=float(a)
            for i in floatRange(0,v,0.0001):
                log = 10**x
                if log >= v:
                    logA = x
                else:
                    x+=0.00001
            print("log of",a,"is",logA)
        elif a == "^":
            a = input("enter a value: ")
            p = input("enter a value: ")
            if a.isdigit() and p.isdigit():
                v1=int(a)
                v2=int(p)
                e = v1**v2
            print("log^",e)
    
    def Power(self):
        a = input("enter a value: ")
        p = input("enter a value: ")

        if a.isdigit() and p.isdigit():
            v1=int(a)
            v2=int(p)
            e = v1**v2
            print(v1,v2,e)

        elif a.isdigit():
            v1=int(a)
            print(v1,"**",p)

        elif p.isdigit():
            v2=int(p)
            print(a,"**",v2)

        else:
            print(a,"**",p)

    def Sqrt(self):
        sqrt = self.a**0.5
        print(sqrt)

#Algebraic Equations
class Algebra:
    def __init__(self):
        self.op = input("enter type of equation: ")

    def linear(self):
        #ax+b-c=0
        a=int(input("enter a: "))
        b=int(input("enter b: "))
        c=int(input("enter c: "))

        print(f"{a}x + {b} = {c}")

        for x in range(-1000,1000):
            if a*x+b-c == 0:
                print(f"the value of x is: {x}")
                print(f"{a}*({x}) + {b} - {c} = 0")

    def Quadractic(self):
        #ax**2+b*x+c=0
        a=int(input("enter a: "))
        b=int(input("enter b: "))
        c=int(input("enter c: "))

        d = b**2-(4*a*c)

        if d == 0:
            x1 = ((-b)+(d**0.5))/2*a
            print("x1 is: ",x1)
            x2 = ((-b)-(d**0.5))/2*a
            print("x2 is: ",x2)
            
        elif d < 0:
            print("roots are imaginary")
            d = f"{(b**2-(4*a*c))*0.5}i"
            dnom = 2*a
            px = f"{-b}+{d}/{dnom}"
            nx = f"{-b}-{d}/{dnom}"
            print(px)
            print(nx)
        else:
            #y = ax^2 + bx +c
            #y = (ax + b/2)^2 +c - (b/2)^2
            x = int(input("enter value of x: "))
            a1 = (x+b/2)**2
            a2 = (c) - ((b/2)**2)
            a3 = a1 + a2
            print(f"y = (x + {b/2})^2 + {c} - ({b/2})^2")
            print("the value of y is:",a3)

    def Simultaneous(self):
        print("Simultaneous in X and Y")
        a1 = int(input("enter coeff of x1: "))
        b1 = int(input("enter coeff of y1: "))
        print(f"{a1}x+{b1}y=0")
        a2 = int(input("enter coeff of x2: "))
        b2 = int(input("enter coeff of y2: "))
        print(f"{a2}x+{b2}y=0")

        op = input("enter the arithmetic function you want to perform: ")
        if op == "add":
            print(f"{a1+a2}x+{b1+b2}y=0")
        if op == "sub":
            print(f"{a1-a2}x+{b1-b2}y=0")

    def Equation(self):
        a = input("enter your equation: ")
        terms=a.split('+')

        digits = []
        coeff = []
        cons = []
        var = []
        solved_t = []
        seq = []
        print("the terms are:",terms)

        s_terms=[]
        #index preceding x
        for i in terms:
            for x in i:
                #splitting terms
                s_terms.append(x)
        print("")
        #print("split terms:",s_terms)

        #seperating the digits and texts
        for i in terms:
            for x in i:
                digits.append(x)
        #replacing the value of x
        sub_X = input("enter the value of x: ")
        for i in range(len(digits)):
            if digits[i] == "x":
                digits[i] = sub_X
        print("substituting x:",digits)
        #seperating variables and constants
        for i in digits:
            if i.isdigit():
                i=int(i)
                cons.append(i)
            else:
                var.append(i)
                print("")
        #finding the previous middle and next term to x in the list
        for i in range(len(digits)-2):
            if digits[i] == sub_X:
                digits[i]=int(digits[i])
                sub_x = digits[i]
                if digits[i] == sub_x:
                    prevTerm = digits[i-1] if i-1 >= 0 else None
                    midTerm = digits[i+1]
                    nextTerm = digits[i+2]
                    eq=(f"(+{prevTerm}*({sub_X})^{nextTerm})")
                    if prevTerm and nextTerm:
                        if str(prevTerm).isdigit() and str(nextTerm).isdigit():
                            nextTerm=int(nextTerm)
                            prevTerm=int(prevTerm)                 
                        if midTerm == "^":
                            pwr = sub_x ** nextTerm
                            pTerm = int(prevTerm*pwr)
                            seq.append(eq)
                            solved_t.append(pTerm)
        sumS = sum(solved_t)
        print(f"{seq}={sumS}")

    def differential(self):
        a = input("enter your equation: ")
        terms=a.split('+')
        digits = []
        dTerms = []
        print("the terms are:",terms)
        #seperating the digits and texts
        for i in terms:
            for x in i:
                digits.append(x)
        #differentiation formulae for trig terms
        for i in range(len(terms)):
            if terms[i] == "log(x)":
                nTerm = f"d/dx(log(x))=(1/log(x))"
                print(nTerm)
            if terms[i] == "e^x":
                nTerm = f"d/dx(e^x)=(e^x)"
                print(nTerm)
            if terms[i] == "sin(x)":
                nTerm = f"d/dx(sin(x))=(cos(x))"
                print(nTerm)
            if terms[i] == "cos(x)":
                nTerm = f"d/d(cos(x))=(x-sin(x))"
                print(nTerm)
            if terms[i] == "tan(x)":
                nTerm = f"d/dx(tan(x))=(sec(x)^2)"
                print(nTerm)
            if terms[i] == "cot(x)":
                nTerm = f"d/dx(cot(x))=(-cosec(x)^2)"
                print(nTerm)
            if terms[i] == "sec(x)":
                nTerm = f"d/dx(sec(x))=(sec(x)tan(x))"
                print(nTerm)
            if terms[i] == "cosec(x)":
                nTerm = f"d/dx(cosec(x))=(-cosec(x)cot(x))"
                print(nTerm)
        for i in dTerms:
            print(i)
        for i in range(len(digits)-2):
            if digits[i] == "x":
                x_index = digits[i]
                prevTerm = digits[i-1] if i-1 >= 0 else None
                midTerm = digits[i+1]
                nextTerm = digits[i+2]
                if prevTerm and nextTerm:
                    if str(prevTerm).isdigit() and str(nextTerm).isdigit():
                        nextTerm=int(nextTerm)
                        prevTerm=int(prevTerm)                 

                    if midTerm == "^" and nextTerm == "l":
                        nTerm = f"{prevTerm}*(1/logx)*x^log(x)-1"
                        print(nTerm)
                        break
                    
                    if midTerm == "^":
                        nTerm = f"d/dx({prevTerm*nextTerm}*x^{nextTerm-1})"
                        dTerms.append(nTerm)   
        for i in dTerms:
            print(i)

#trignometric functions
class Trignometric:
    def __init__(self):
        print("Trignometric value finder.")
        self.op = input("enter trignometric term: ")

    def sin(self):
        x = float(input("enter x: "))
        sinx = (x * 3.14159265/180)
        print(sinx)

    def cos(self):
        x = float(input("enter x: "))
        sinx = round(x * 3.14/180,3)
        cosx = round(1-(sinx**2)*x,3)
        print(cosx)

    def tan(self):
        x = float(input("enter x: "))
        sinx = round(x * 3.14/180,3)
        cosx = round(1-(sinx**2)*x,3)
        tanx = round(sinx/cosx,3)
        print(tanx)
    
    def sec(self):
        x = float(input("enter x: "))
        sinx = round(x * 3.14/180,3)
        cosx = round(1-(sinx**2)*x,3)
        secx = 1/cosx
        print(secx)

    def cosec(self):
        x = float(input("enter x: "))
        sinx = (x * 3.14159265/180)
        cosecx = 1/sinx
        print(cosecx)
    
    def cot(self):
        x = float(input("enter x: "))
        sinx = round(x * 3.14/180,3)
        cosx = round(1-(sinx**2)*x,3)
        tanx = round(sinx/cosx,3)
        cotx = 1/tanx
        print(cotx)

if mode == "math":
    obj1 = Math()
    if obj1.op == "add":
        obj1.Add()

    if obj1.op == "sub":
        obj1.Sub()

    if obj1.op == "mul":
        obj1.Mul()

    if obj1.op == "div":
        obj1.Div()

    if obj1.op == "fact":
        obj1.Fact()

    if obj1.op == "pwr":
        obj1.Power()

    if obj1.op == "log":
        obj1.Log()

    if obj1.op == "sqrt":
        obj1.Sqrt()

elif mode == "algebra":
    obj2 = Algebra()
    if obj2.op == "linear":
        obj2.linear()

    if obj2.op == "quadratic":
        obj2.Quadractic()

    if obj2.op == "simultaneous":
        obj2.Simultaneous()

    if obj2.op == "equation":
        obj2.Equation()

    if obj2.op == "diff":
        obj2.differential()

elif mode == "trignometric":
    obj3 = Trignometric()
    if obj3.op == "sin":
        obj3.sin()

    if obj3.op == "cos":
        obj3.cos()

    if obj3.op == "tan":
        obj3.tan()

    if obj3.op == "sec":
        obj3.sec()

    if obj3.op == "cosec":
        obj3.cosec()

    if obj3.op == "cot":
        obj3.cot()
