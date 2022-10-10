class Node:
    def __init__(self,element,n):
        self._element = element
        self._next = n

class PrefixConverter:
    def __init__(self):
        self.stackList = []
        self._top = -1                  
        # self._kapasitas = kapasitas     
        self._array = []                # Deklarasi array untuk stack kosong
        self._outputArray = []          # Deklarasi array untuk stack output nanti
        self._operator = {'+':1, '-':1, '*':2, '/':2, '^':3} # Deklarasi operasi hitung yang akan keluar

    def isEmpty(self):          # Cek apakah stack kosong
        if self._top == -1 :    
            return True
        else:
            return False

    # method untuk menambahkan expression baru
    def push(self,expression):
        self.stackList.append(expression)

    # method untuk melihat expression paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    # method untuk menghapus expression palin atas
    def pop(self):
        if self.stackList:
            expression = self.stackList.pop(-1)
            return expression
        else:
            return "Isi Stack Kosong"

    def isCommand(self, opp):     # Fungsi memeriksa apakah karakter yang 
        return opp.isalpha()

    def cekValidExpression(self, expression):
        for i in expression:
            if i.isalpha() or i == "(":
                return False
        return True

    def infixToPrefix(self, expression):

            if " " in expression:
                expression = expression.split()

            if not self.cekValidExpression(expression):
                return "Expresi Infix yang anda masukkan tidak valid !!"
            
            op = []
            angka = []



# Test Case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))