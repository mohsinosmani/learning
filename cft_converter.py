
print("welcome to the celsius to fahrenheit converter")


def celsius_to_fahrenheit(celsius):
    fahrenheit = float((celsius * 9/5) + 32)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = float((fahrenheit - 32) * 5/9)
    return celsius

while True:
    celsius_fahrenheit = str(input("if you want to convert celsius write 'C' and if you want to convert fahrenheit write 'F' \n" )).strip().lower()
    if celsius_fahrenheit == "c":
        user_temperature_c = input ('please add the celsius temperature to conver: \n')
        celsius_num = float(user_temperature_c)
        print('the result is: ', celsius_to_fahrenheit(celsius_num), ' celsius')
        print('you have successfully converted celsius to fahrenheit ')
        another_1 = input("Do you want to convert Fahrenheit to Celsius? (yes/no): \n").strip().lower()
        if another_1 == "yes":
            user_temperature_f = input ('please add the fahrenheit temperature to conver: \n')
            fahrenheit_num = float(user_temperature_f) 
            print('the result is: ', fahrenheit_to_celsius(fahrenheit_num))
            print('you have successfully converted fahrenheit to celsius ')
        elif another_1 == "no":
            print('thank you for the using the system')
        else:
            print('you have not selcted the right value,')
        break
            
    elif celsius_fahrenheit == "f":
        user_temperature_f = input ('please add the fahrenheit temperature to conver: \n')
        fahrenheit_num = float(user_temperature_f) 
        print('the result is: ', fahrenheit_to_celsius(fahrenheit_num))
        print('you have successfully converted fahrenheit to celsius ')   
        another_2 = input("Do you want to convert Celsius to Fahrenheit? (yes/no): \n").strip().lower()
        if another_2 == "yes":
            user_temperature_c = input ('please add the celsius temperature to conver: \n')
            celsius_num = float(user_temperature_c)
            print('the result is: ', celsius_to_fahrenheit(celsius_num), ' celsius')
            print('you have successfully converted celsius to fahrenheit ')
        elif another_2 == "no":
            print('thank you for the using the system')
        else:
            print('you have not selcted the right value,')
        break  

    else: 
        print('you have not selcted the right value, Please try again \n')





