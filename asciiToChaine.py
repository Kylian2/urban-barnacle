def hex_to_string(hex_string):
    hex_list = hex_string.replace(" ", "").split()
    hex_str = ''.join(hex_list)
    byte_data = bytes.fromhex(hex_str)
    ascii_string = byte_data.decode('ascii')
    return ascii_string

if __name__ == "__main__":
    filename = input("Entrez le nom du fichier contenant les codes ASCII en hexadécimal : ")
    with open(filename, 'r') as file:
        file.readline()
        output = ""
        for line in file :
            ascii_input = line.strip()
            part = hex_to_string(ascii_input)
            output += part
        print("Chaîne de caractère correspondante :", output[1:])
