#NumberCalculatorEx.py
from Numbers import Numbers
from Calculator import Calculator as Cal
class Kvr:
    def kvrcal(self):
        no=Numbers() # Object Creation
        no.readvalues()
        Cal.operation(no)

#Main Program
Kvr().kvrcal()
