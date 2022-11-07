class Node:
    def __init__(self,data,priority) -> None:
        self.data = data
        self.priority = priority

class PriorityQueueSortedList:
    def __init__(self) -> None:
        self.data = []
        self.size = 0


    def peek(self):
        if self.size != 0:
            x = 9999
            data = ''
            # index = 0
            for i in range(len(self.data)): 
                if self.data[i][1] > x:
                    pass 
                else:
                    x = self.data[i][1] 
                    data = self.data[i][0] 
                    # index = i
            print('Data Prioritas tertinggi : (',data,',', x,')') 
        else:
            print('Priority Queue Kosong')

    def add(self,data,priority):
        self.data.append((data, priority))
        self.data=sorted(self.data, key=lambda x:x[1])
        self.size += 1

    def update(self,prio,new_data):
        if self.size == 0:
            print('Priority Queue kosong')
        for i in range(len(self.data)):
            if self.data[i][1] == prio:
                self.data[i] = (new_data, prio)

    def remove(self):
        if self.size != 0:
            x = 9999 
            index = 0
            data = 0
            for i in range(len(self.data)):
                if self.data[i][1] > x: 
                    pass
                else:
                    x = self.data[i][1] 
                    index = i
                    data += 1
            del self.data[index]
            self.size -= 1
        else:
            print("Priority Queue Kosong!")
        

    def removePriority(self,prio):
        if self.size == 0:
            print('Priority Queue kosong')
        else:
            x = 9999
            index = []
            for i in range(len(self.data)):
                if self.data[i][1] == prio:
                    index.append(self.data[i]) 
            for i in index:
                self.data.remove(i)
            self.size -= 1


    def printIsiQueue(self):
        print('Isi semua Queue : ', end=' ')
        for i in range(len(self.data)):
            print(self.data[i], end=' ')
        print()


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()