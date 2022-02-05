celsius = input("Enter a Celsius temperature:\n")
try:
    fahrenheit = (int(celsius) * 9/5) + 32
except: 
    print("Something went wrong, re-run the prgram and make sure you enter the celsius temperature in numbers, thank you.")
    quit()

print("Your fahrenheit temperature is:", fahrenheit)