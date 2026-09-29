def ConvertsTemperature(value, unit):
    if unit == 'c':
        return (value * 9/5) + 32
    elif unit == 'f':
        return (value - 32) * 5/9
    else:
        print("tidak ada unit")

InputValue = int(input("Masukan Suhu: "))
InputUnit = input("Masukan unit (c/f): ")

konversi = ConvertsTemperature(InputValue, InputUnit)
print(konversi)

    
