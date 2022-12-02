import fah_converter

if __name__ == '__main':
    print("Enter a celcius value : ")
    celius = float(input())
    
    fah = fah_converter.convert_c_to_f(celius)
    print("That's {0} degrees Fahrenheit".format(fah))
    
