import csv

# 1. Write a Python program that reads a text file and prints the number of lines, words, and characters in the file.
"""
file = open('D:\\David\\001. Cursos\\015. Brainnest\\Week 3\\Project\\Beginner\\file_handling.txt', 'r')

def read_txt_file(file):
    content = file.read()
    lines = content.split('\n')
    cant_lines = len(lines)

    return(cant_lines)

print(read_txt_file(file))
file.close()
"""
#2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be a key-value pair in the dictionary.
"""
file = 'D:\\David\\001. Cursos\\015. Brainnest\\Week 3\\Project\\Beginner\\SalesJan2009.csv'

def read_csv_file(file):

    with open(file, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            return fila

print(read_csv_file(file))
"""
#3. Write a Python program that reads a binary file and converts it into a hexadecimal string. The program should output the hexadecimal string to a text file.
"""
path = 'D:\\David\\001. Cursos\\015. Brainnest\\Week 3\\Project\\Beginner\\OpenSans-Regular.bin'

def read_bin_file(path):
    with open(path, 'rb') as file:
        content = file.read()
        hex_string = content.hex()

    return hex_string

print(read_bin_file(path))
"""
#4. Write a Python program that reads a text file containing numbers and calculates the sum of all the numbers in the file.
"""
file = open('D:\\David\\001. Cursos\\015. Brainnest\\Week 3\\Project\\Beginner\\file_handling.txt', 'r')

def sum_numbers_txt_file(file):
    
    #numbers = [0,1,2,3,4,5,6,7,8,9]

    sum_of_all_numbers = 0
    content = file.read()

    for character in content:
        if character.isdigit():
            sum_of_all_numbers += int(character)

    return sum_of_all_numbers

print(sum_numbers_txt_file(file))
file.close()
"""
#5. Write a Python program that reads a text file and removes all the blank lines. The modified text should be written back to the file.

file = open('D:\\David\\001. Cursos\\015. Brainnest\\Week 3\\Project\\Beginner\\file_handling.txt', 'r')

def read_txt_file(file):
    content = file.read()
    lines = content.splitlines()
    lines_without_blanks = [line for line in lines if not line.isspace()]
    new_content = "\n".join(lines_without_blanks)

    return(new_content)

file_content = read_txt_file(file)


file_name = "new_file.txt"
file_wl = open(file_name, 'w')
file_wl.write(file_content)
file_wl.close

file.close()