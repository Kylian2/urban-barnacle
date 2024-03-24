def string_to_hex(input_string):
    hex_list = []
    for char in input_string:
        hex_list.append(hex(ord(char))[2:]) 
    return hex_list

def write_to_file(hex_list, filename):
    with open(filename, 'w') as file:
        file.write('v2.0 raw\n')
        file.write(hex(len(hex_list))[2:]+'\n')
        for hex_code in hex_list:
            file.write(hex_code + '\n')

if __name__ == "__main__":
    input_string = input("Entrez une chaîne de caractères : ")
    filename = input("Entrez le nom du fichier de sortie : ")
    
    hex_list = string_to_hex(input_string)
    write_to_file(hex_list, filename)
    
    print("Les codes ASCII en hexadécimal ont été écrits dans le fichier", filename)
