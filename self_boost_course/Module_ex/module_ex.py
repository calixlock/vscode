# import fah_converter as fah
from fah_converter import convert_c_to_f as cf 
if __name__ == "__main__" :
    print("Enter a celcius value:")
    c = float(input())
    # f = fah.convert_c_to_f(c)
    f = cf(c)
    print(f"That's {f} degrees fahrenheit ") 
