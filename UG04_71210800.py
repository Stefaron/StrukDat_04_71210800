import json

with open('mahasiswa.json','r') as datafile:
    data = json.load(datafile)

    kosong = {}
    masukan = int(input('Masukkan jumlah mahasiswa baru : '))
    list_nama = []
    for i in range(masukan):
        nama = input('Masukkan nama anda : ')
        list_nama.append(nama)
        jmlh_hobi = int(input('Masukkan jumlah hobi : '))
        list_hobi = []
        for i in range(jmlh_hobi):
            
            hobi = input(f'Masukkan Hobi ke-{i+1} : ')
            list_hobi.append(hobi)
        prestasi = input('Masukkan Prestasi Anda : ')

        print('Data berhasil ditambahkan')
        print()


        kosong[nama] = [{'Biodata' : {'Hobi' : hobi, 'Prestasi' : prestasi}}]
    
    data.update(kosong)
    
    with open('mahasiswa.json','w') as datafile:
        json.dump(data,datafile)
            
