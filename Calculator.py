class Calculator:
    def __init__(self):
        # Take the two numbers from the users
        self.__prim = int(input('Insert the first number: '))
        self.__sec = int(input('Insert the __second number: '))

        # Verify if the numbers are 0 anf if yes assign 1
        if self.__prim == 0:
            self.__prim = 1
        if self.__sec == 0:
            self.__sec = 1

        # Show the numbers to user
        print(f'This is the first number: {self.__prim}')
        print(f'This is the __second number: {self.__sec}')

        while True:
            # Show the menu to user
            print('Choose the operation that you want to do:')
            print("""
                [+] - Sum
                [-] - Subtraction
                [*] - Multiplication
                [/] - Division
                [**] - Exponentiation
                [%] - module
                [exit] - Quit
                """)

            # Ask the user about the operation that he want to do
            self.__operator: str = str(input('Insert the operation: '))

            # Starts the operation selected including quiting the program if selected
            if self.__operator.lower() != 'exit':
                if self.__operator == '+':
                    print('The sum result is:')
                    print(self.add())
                elif self.__operator == '-':
                    print('The subtraction result is:')
                    print(self.sub())
                elif self.__operator == '*':
                    print('The multiplication result is:')
                    print(self.mul())
                elif self.__operator == '/':
                    print('The division result is:')
                    print(self.div())
                elif self.__operator == '**':
                    print('The exponentiation result is:')
                    print(self.exp())
                else:
                    print('The module result is:')
                    print(self.mod())
            else:
                break

    # Define the methods of each operation
    def add(self):
        return self.__prim + self.__sec

    def sub(self):
        return self.__prim - self.__sec

    def mul(self):
        return self.__prim * self.__sec

    def div(self):
        return self.__prim / self.__sec

    def exp(self):
        return self.__prim ** self.__sec

    def mod(self):
        return self.__prim % self.__sec


# Start the class constructor method
calc = Calculator()
