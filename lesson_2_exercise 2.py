""""""
#ask the user for the city names
city1 = input("enter the name of the first city: ") 
city2 = input(" enter the name of the second city: ") 

#ask the user for the current temperature in fahrenheit 
temp_f1_str= input(f"please enter the current temperature for {city1}in fahrenheit:")
temp_f2_str= input(f"please enter the current temperature for {city2}in fahrenheit:")

#convert the temperatures to float
temp_f1=float(temp_f1_str)
temp_f2=float(temp_f2_str)

#convert the temperature to celcius
temp_c1=(temp_f1-32)* 5 / 9
temp_c2=(temp_f2-32)* 5 / 9


if temp_c1<0 and temp_c2<0:
    print ("Alert:the temperatures in both cities are below freezing point.")
    

elif temp_c1<0 or temp_c2<0:
    print("Alert: The temperatures in one of the cities is below freezing point. ")
else:
    print("The temperatures in both cities are above the freezing point.")


#print the user input in formatted string
    print(f"the current temperature in {city1} is {temp_c1:.1f}degrees celsius")
    print(f"the current temperature in {city2} is {temp_c2:.1f}degrees celsius")


    