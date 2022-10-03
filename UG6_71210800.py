class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def insert_head(self,norek,nama,saldo):
        baru = NodeTabungan(norek,nama,saldo)
        if self._head == None:
            self._head = baru
            self._tail = baru
        else:
            baru.next = self._head
            self._head = baru
        self._size += 1


    def deleteHead(self):
        if self._size == 0:
            return False
        elif self._size == 1:
            helper = self._head
            self._head = None
            self._tail = None
            del helper
            self._size -= 1
            return True
        else:
            helper = self._head
            self._head = self._head.next
            del helper
            self._size -= 1
            return True

    def deleteTail(self):
        if self._size == 0:
            return False
        elif self._size == 1:
            delete = self._tail
            self._tail = None
            self._head = None
            del delete
            self._size -= 1
        else :
            helper = self._head
            while helper.next != self._tail:
                helper = helper.next
            delete = self._tail
            self._tail = helper
            self._tail.next = None
            del delete
            self._size -= 1
            return True
    
    def delete(self,position):
        if self._size == 0:
            return False
        elif position == 0:
            self.deleteHead()
        elif position + 1 >= self._size:
            self.deleteTail()
        else:
            delete_node = self._head
            for i in range(position):
                delete_node = delete_node.next
            helper = self._head
            while helper.next != delete_node:
                helper = helper.next
            helper.next = delete_node.next
            del delete_node
            self.size = self.size - 1

    def print(self):
        bantu = self._head
        while bantu != None:
            print(f'Norek : {bantu.no_rekening}')
            print(f'Nama : {bantu.nama}')
            print(f'Saldo : {bantu.saldo}')
            bantu = bantu.next
        print()

    def filter(self,batas):
        jumlah = 0
        bantu = self._head
        while bantu != None:
            if bantu.saldo == batas:
                jumlah += 1
                del bantu
            bantu = bantu.next
            print(f'Rekening yang berhasil di hapus sebanyak : {jumlah} buah')

    # def update(self,ubah):

        

slnc=SLNC() 
slnc.insert_head(201,"Hanif", 250000) 
slnc.insert_head(110,"Yudha", 150000) 
slnc.print()
slnc.filter(100)
# slnc.update(200)
# slnc.update(50)
# slnc.print()
        
