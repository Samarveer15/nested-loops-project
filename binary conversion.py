

 

Binary_String=input( "enter the binary number:-") 
decimal_number=int(Binary_String,2)
print(f"the deciaml equivalent of binary{Binary_String} is {decimal_number}")
Binary_String=bin(decimal_number)
reconverted_decimal=int(Binary_String,2)
print(f"the Binary of {decimal_number} is {Binary_String},and its reconversion to decimal is{reconverted_decimal}.")
