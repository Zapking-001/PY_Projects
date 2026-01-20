"""
Docstring for 9.Binary to Decimal: 
            Formula: 
               We can use the conversion function of int() :
                 class int(
                    x: str | bytes | bytearray,
                    /,
                    base: SupportsIndex
                    )
            
            Efficiency: Time complexity is O(m)
                        Space complexity is O(1)


"""
n = input("Enter the binary value: ")
Dec_val = int(n, 2) 

print(f"Decimal({n}) = {Dec_val}")
