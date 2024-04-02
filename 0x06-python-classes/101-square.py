#!/usr/bin/python3
'''Define a Square class.'''


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def my_print(self):
        '''Print the square with the number character.'''
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        '''Define the print() representation of a Square.'''
        string_representation = ""
        if self.__size != 0:
            string_representation += "\n" * self.__position[1]
        for _ in range(self.__size):
            string_representation += " " * self.__position[0]
            string_representation += "#" * self.__size
            if _ != self.__size - 1:
                string_representation += "\n"
        return string_representation
      
