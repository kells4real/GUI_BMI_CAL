from tkinter import *
from tkinter import messagebox 
top = Tk() 
top.title("Web Dreams BMI Calculator") 
top.geometry("350x340")


def bmi(x, y, z): # Function to calculate the BMI
    return round(x / y / z) 


num1 = IntVar() # Variable to hold height in ft 
num2 = IntVar() # Variable to hold height in inches 
weight = IntVar() # variable to hold weight
sex = IntVar() # Not used yet



def main(): # Main function to execute the programme 
 
    result1 = num1.get() * 0.305
    result2 = num2.get() * 0.0254    

    grand_meter = result1 + result2
    grand_bmi = bmi(weight.get(), grand_meter, grand_meter)

    #print('Your height in metres =', round(grand_meter, 2))

    if grand_bmi < 19:
        messagebox.showinfo('BMI', 'Your BMI =' + str(grand_bmi) + ': You are under weight and below the recommended Body Mass Index (BMI), consume about 1500 and 2500 calories daily and do only light exercises daily to achieve the recommended body weight and BMI. If you dont attain the recommended weight and BMI within six months, please do see a doctor.')
    
    elif grand_bmi >= 19 and grand_bmi <= 25:
        messagebox.showinfo('BMI','Your BMI =' + str(grand_bmi) + ': You are at your ideal weight and Body Mass Index (BMI), BMIs between 19 and 24.9 are considered optimum by most professionals. To maintain this ideal weight and BMI, consume between -10% to 10% more the calories you expel.')
    elif grand_bmi > 25 and grand_bmi <= 30:
        messagebox.showinfo('BMI','Your BMI =' + str(grand_bmi) + ': You are over weight and over the recommended Body Mass Index (BMI) which is between 19 and 24.9, loose between 1000 and 2000 calories daily by exercising, and reduce your general calories intake to attain the recommended weight and BMI for a healthy living.')
    elif grand_bmi > 30:
        messagebox.showinfo('BMI','Your BMI =' + str(grand_bmi) + ': You are obese and way over your ideal Body Mass Index (BMI) which is between 19 and 24.9, loose between 2000 and 4000 calories daily, and reduce your calories intake by 80% to attain a healthy life. If you are above 40 years, please see your doctor immediately for a health consult on how to reduce your weight as you may be prone to numerous heart complications. You should definitely make an appointment with a jym instructor as soon as possible.')


''' # These are just a bunch of code I wrote for the command line version, that i might still get to use later here.
      Not used yet.      
def agge():
    age = int(input('Enter your age: '))
    if age >= 18:
        main()
    else:
        print('You must be 18 and above to calculate BMI')
        agge()


def sex_t():
    sex = input("m/f: ")
    if sex == 'f' or sex == 'm' or sex == 'F' or sex == 'M':
        agge()
    else:
        print('Invalid input, please enter either m for male, or f for female.')
        sex_t()


if sex == 'f' or sex == 'm' or sex == 'M' or sex == 'F':
    agge()
else:
    print('Invalid input, please enter either m for male, or f for female.')
    sex_t()'''



L0 = Label(top, text="Height(Ft)", font=("forte",20,"italic"))

L1 = Label(top, text="Height(inch)", font=("forte",20,"italic"))

L2 = Label(top, text= "Weight(kg)", font=("forte",20,"italic"))

E0 = Entry(top, bd =10, textvariable = num1, width=53)

E1 = Entry(top, bd =10, textvariable = num2, width=53)

E2 = Entry(top, bd =10, textvariable = weight, width=53)

B1 = Button(top, text  = "Calculate", command = main, font=(50))

B2 = Button(top, text = "Quit", command = top.quit, font = (50))

L20 = Label(top, text= "", )

L0.grid(row=0, column=2)
L1.grid(row=3, column=2)
L2.grid(row=5, column=2)
E0.grid(row=1, column=2)
E1.grid(row=4, column=2)
E2.grid(row=6, column=2)
L20.grid(row=7)
B1.grid(row=8,column=2)
L20.grid(row=9)
B2.grid(row=10, column=2)

top.mainloop()



