from string import digits,punctuation,ascii_letters
from random import choices
class password_generator:
    def __init__(self):
        self.data = digits+punctuation+ascii_letters
    def generate(self):
        length = int(input("Enter the length of the password : "))
        weight = [3]*(len(digits)) + [2]*(len(punctuation)) + [1]*(len(ascii_letters))
        rpass = choices(self.data,weights=weight,k=length)
        random_pass = ''.join(str(i) for i in rpass)
        print("Suggested password =",random_pass)

def main():
    ob = password_generator()
    ob.generate()
main()
