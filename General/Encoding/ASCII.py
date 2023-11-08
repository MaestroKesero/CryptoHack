def numberToAscii():
    
    number_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

    ascii_result = ""
    
    for number in number_list:
        
        character_ascii = chr(number)
        ascii_result += character_ascii
        
    print("La cadena ascii asociada es: ", ascii_result)
    
    
numberToAscii()
