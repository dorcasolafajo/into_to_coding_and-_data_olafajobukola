
while True:

      city= input("enter your city:") 
      temp_f_str= int (input("Enter the current temperature in fahrenheit:" ))
      
      temp_f=float(temp_f_str)
      
      
      
      temp_c=(temp_f-32)*5/9
    
      if temp_c<0:
         print ("Alert:temp in munich is below freezing point.")

      else:
         print("The temperature is above the freezing point")

         print(f"The current temperature in{city}is{temp_c:.1f}degrees celsius")
         break
         print("invalid input.please enter a valid number,")
