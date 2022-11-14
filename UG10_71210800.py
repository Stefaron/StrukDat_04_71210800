def mergesort(data):
    if len(data) > 1:
        tengah = len(data) // 2
        kiri = data[:tengah]
        kanan = data[tengah:]

        mergesort(kiri)
        mergesort(kanan)

        i = 0
        j = 0
        k = 0

        while i < len(kiri) and j < len(kanan):
            if kiri[i] >= kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1
        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1
        while j < len(kanan):
            data[k]= kanan[j]
            j += 1
            k += 1
        return data

lst1 =[1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56] 
lst2 =[20,21,22,23,24,25,26,27] 
lst3 =[30,29,31,33,19,20,31,21,59] 
print(mergesort(lst1))
print(mergesort(lst2)) 
print(mergesort(lst3))