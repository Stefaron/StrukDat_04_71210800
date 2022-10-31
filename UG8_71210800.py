class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 
    def __init__(self): #konstruktor
        self.data = []
        self.capacity = Kasir.DEFAULT_CAPACITY
        self.size = 0
        # self.front = 0
      
       
    def __len__(self): #mengembalikan ukuran Queue
        return self.size
        

    def is_empty(self): #mengecek apakah Queue kosong ?
        return self.size == 0
        

    def dequeue(self): #menghapus data paling depan (front)
        # if self.is_empty():
        #     print('Empty')
        # answer = self.data[self.front]
        # self.data.remove(answer)
        # # self.data[self.front] = None
        # # self.data = (self.front + 1) % len(self.data)
        # self.size -= 1
        # return answer
        data = self.data[0]
        self.data.remove(data)
        print(f"### Pelanggan {data} Selesai Membayar ### \n")
        self.size -= 1

    def enqueue(self, namaPelanggan): #menambah data ke list
        # if self.size == len(self.data):
        #     self.resize(2*len(self.data))
        # self.data.append(namaPelanggan)
        # # avail = (self.front + self.size) % len(self.data)
        # # self.data[avail] = namaPelanggan
        # self.size += 1
        self.data.append(namaPelanggan)
        self.size += 1

    def resize(self, cap): #mengubah ukuran queue pada list
        # old = self.data
        # self.data = [None] * cap
        # walk = self.front
        # for k in range(self.size):
        #     self.data[k] = old[walk]
        #     walk = (1 + walk) % len(old)
        # self.front = 0
        print(f"### Melakukan Resize ### \n")
        self.capacity = self.capacity * cap
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        # for i in range (0,len(self.data)):
        #     print(self.data[i], end=" ")
        # print()
        if len(self.data) > self.capacity:
                self.resize(2)
        print("=== Kasir ===")
        c = len(self.data)-1
        n = 1
        for i in range(0, (self.capacity)):            
            if i <= c:
                print(n,".",self.data[i], end=' ')
                print()
            else:
                print(n,". Kosong")
            n += 1
                
        # else:
        #     n = 1
        #     for i in range(0, (self._capacity)):
        #         print(n,".",self._data[i], end=' ')
        #         n += 1
        #         print()
            
        print()
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

